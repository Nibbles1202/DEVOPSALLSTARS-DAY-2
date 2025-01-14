import os
import json
import urllib.request
import boto3
from datetime import datetime, timedelta, timezone

def format_game_data(game):
    # Extract needed values from data
    away_team = game.get("AwayTeam", {}).get("TeamName", "N/A")
    home_team = game.get("HomeTeam", {}).get("TeamName", "N/A")
    status = game.get("Status", "N/A")
    final_score = game.get("FinalScore", "N/A")
    start_time = game.get("StartTime", "N/A")
    channel = game.get("Channel", "N/A")
    
    
    #Format Innings & Update Score after Every Inning
    innings = game.get("Innings", [])
    away_total = 0
    home_total = 0
    inning_scores = []
    
    for i in innings:
        away_total += i.get('AwayScore', 0) #Adds away score to from current inning to current total
        home_total += i.get('HomeScore', 0) #Same as above but for home score
        inning_scores.append(f"Inning {i['Number']}: {away_total}-{home_total}") # Creates a string with cumulative scores for the current inning
        
    #Combine all scores into a string
    inning_scores_str = ','.join(inning_scores)
    
    #Format message based on game status 
    if status == "InProgress":
        last_play = game.get("LastPlay", "N/A")
        return (
            f"Game Status: {status}\n"
            f"{away_team} vs {home_team}\n"
            f"Current Score: {final_score}\n"
            f"Last Play: {last_play}\n"
            f"Channel: {channel}\n"
            f"Inning Scores: {inning_scores_str}\n"
        )
    elif status == "Scheduled":
        return (
            f"Game Status: {status}\n"
            f"{away_team} vs {home_team}\n"
            f"Start Time: {start_time}\n"
            f"Channel: {channel}\n"
        )
    else: 
        return (
            f"Game Status: {status}\n"
            f"{away_team} vs {home_team}\n"
            f"Details are unavailable at the moment.\n"
        )
    #inning_scores = ','.join([f"Inning {i['Number']}: {i.get('AwayScore', 'N/A')}-{i.get('HomeScore', 'N/A')}" for i in innings])
    
def lambda_handler(event, context):
    # Environment Variables
    api_key = os.getenv("MLB_API_KEY")
    sns_topic_arn = os.getenv("SNS_TOPIC_ARN")
    sns_client = boto3.client("sns")
    
    # Adjust for Eastern Time (UTC-5)
    utc_now = datetime.now(timezone.utc)
    eastern_time = utc_now - timedelta(hours=5) # Eastern Time is UTC-5
    today_date = eastern_time.strftime("%Y-%m-%d")
    
    print(f"Fetching games for data: {today_date}")
    
    # Fetch data from the API 
    api_url = f"https://api.sportsdata.io/v3/mlb/scores/json/GamesByDate/{today_date}?key={api_key}"
    print(today_date)
    
    try:
        with urllib.request.urlopen(api_url) as response:
            data = json.loads(response.read().decode())
            print(json.dumps(data, indent=4)) #Debugging: log the raw data 
    except Exception as e:
        print(f"Error fetching data from API: {e}")
        return {"statusCode": 500, "body": "Error fetching data"}
    
    #Include InProgress and Scheduled Game
    scheduled_games = [game for game in data if game ["Status"] == "Scheduled"]
    
    messages = [format_game_data(game) for game in scheduled_games]
    scheduled_message = "\n---\n".join(messages) if messages else "No games available for today"
    
    # Publish to SNS 
    try:
        sns_client.publish(
            TopicArn=sns_topic_arn,
            Message=scheduled_message,
            Subject="MLB Game Updates"
        )
        print("Message published to SNS successfully.")
        return {"statusCode": 200, "body": "Message published to SNS successfully"}
    except Exception as e:
        print(f"Error publishing to SNS: {e}")
        return {"statusCode": 500, "body": "Error publishing to SNS"}
    
    