# Explanation

away_total and home_total are initialized to 0. These variables will keep track of the cumulative scores for the away and home teams.
For each inning in innings:
The scores for the away and home teams are added to the cumulative totals (away_total and home_total).
A formatted string is created that shows the inning number and the cumulative scores up to that inning.
inning_scores is a list that holds the formatted strings for each inning. At the end, we join these strings into a single string using ', '.join(inning_scores)


# NBA Game Day Notifications / Sports Alerts System
A real-time notification system designed for sports enthusiasts, providing live NBA game updates via SMS and email. This project leverages AWS services, Python, and the NBA Game API to create a secure, automated, and user-friendly alert system.

## Project Highlights
🔹 Real-Time Game Updates: Fetches live NBA game scores using an external API.

🔹 Multi-Channel Notifications: Sends formatted score updates to subscribers via SMS and Email using Amazon SNS.

🔹 Automated Scheduling: Utilizes Amazon EventBridge to automate regular notifications during game hours.

🔹 Secure Architecture: Designed with security best practices, implementing least privilege access for IAM roles.

## Features
🏀 Live Score Updates: Stay updated with the latest NBA scores and stats in real time.

📩 Customizable Alerts: Receive notifications via your preferred channel—SMS or Email.

⚙️ Scheduled Updates: Automatically sends updates at key intervals, ensuring fans never miss critical game moments.

🔒 Secure Infrastructure: Adheres to cloud security principles for robust and reliable operations.

## Prerequisites
1️⃣ Sports API Key: Create a free account at sportsdata.io to access NBA game data.

2️⃣ AWS Account: Set up an AWS account with basic knowledge of AWS services like SNS, Lambda, and EventBridge.

3️⃣ Python Skills: Familiarity with Python for setting up API integration and notification logic.

## Why This Project Matters
This system combines cloud computing and real-world application of APIs to deliver timely sports alerts, making it a perfect example of leveraging modern technology for fan engagement.

## Technical Architecture
![image](https://github.com/user-attachments/assets/5d2ba02e-a743-4d41-af13-3b54ccb212d6)

## Technologies Used
Cloud Provider: AWS

Core AWS Services:

Amazon SNS: Sends notifications to subscribers.

AWS Lambda: Executes notification logic.

Amazon EventBridge: Automates scheduled updates.

External API: NBA Game API (SportsData.io)

Programming Language: Python 3.x

IAM Security: Follows the principle of least privilege for roles and policies.

## Project Structure

![image](https://github.com/user-attachments/assets/8c7454fa-fd4e-4829-8d6a-1821f0c9b89d)

## Setup Instructions
1. Clone the Repository
- git clone https://github.com/princemaxi/Game-Day-Notifications
- cd game-day-notifications
3. Create an SNS Topic
- Navigate to the SNS service in the AWS Management Console.
- Click Create Topic → Select Standard.
- Name the topic (e.g., gd_topic) and note the ARN.
- Click Create Topic.
4. Add Subscriptions to the SNS Topic
- Select your SNS topic and go to the Subscriptions tab → Create Subscription.
- Choose your preferred protocol:
- Email: Provide a valid email address and confirm the subscription via the link sent to your inbox.
- SMS: Enter a phone number in international format (e.g., +1234567890).
5. Create SNS Publish Policy
- Go to IAM service → Policies → Create Policy.
- Under JSON, paste the content from policies/gd_sns_policy.json.
- Replace REGION and ACCOUNT_ID with your AWS region and account ID.
- Click Next → Review, name the policy (e.g., gd_sns_policy), and click Create Policy.
6. Create an IAM Role for Lambda
- Navigate to IAM service → Roles → Create Role.
- Select AWS Service → Choose Lambda.
- Attach the following policies:
- gd_sns_policy (created in step 4).
- AWSLambdaBasicExecutionRole (AWS-managed policy).
- Name the role (e.g., gd_role) and save its ARN.
7. Deploy the Lambda Function
- Go to the Lambda service → Create Function → Author from Scratch.
- Enter a name (e.g., gd_notifications) and select Python 3.x as the runtime.
- Assign the IAM role (gd_role) to the function.
- Upload the code from src/gd_notifications.py into the function editor.
-  Add environment variables:
- NBA_API_KEY: Your SportsData.io API key.
- SNS_TOPIC_ARN: The ARN of the SNS topic created earlier.
- Click Create Function.
8. Set Up Automation with EventBridge
- Navigate to EventBridge → Rules → Create Rule.
- Set the event source to Schedule → Use a cron expression for regular updates.
- Example (hourly updates): 0 * * * *
- Set the target to your Lambda function (gd_notifications) and save the rule.
9. Test the System
- Open the Lambda function in the AWS Console.
- Create a test event to simulate execution.
- Verify that notifications are sent to your email/SMS subscribers.

![image](https://github.com/user-attachments/assets/150b040d-c176-4103-9578-b6dcd13fe7e9)
![image](https://github.com/user-attachments/assets/1ae8bc73-4c49-4f62-8b75-e1060c493a86)
![image](https://github.com/user-attachments/assets/33406b16-ea14-4816-9f64-d07686e5712f)
![image](https://github.com/user-attachments/assets/ab3b3289-db03-4f6d-883a-e914506b00cb)
![image](https://github.com/user-attachments/assets/59e09652-b7f1-4ae7-ad8f-b8a1894793f0)
![image](https://github.com/user-attachments/assets/329f8055-3266-4ff9-a818-938a8fdcbcee)



Key Takeaways
- Integrated AWS SNS, Lambda, and EventBridge to design a real-time notification system.
- Secured the architecture with least privilege IAM policies.
- Demonstrated API integration and automation in a cloud environment.

Future Enhancements
- Add NFL Alerts: Extend functionality to include NFL game notifications.
- Personalized Preferences: Use DynamoDB to store user preferences (e.g., teams or game types).
- Web UI Integration: Create a frontend interface for users to manage subscriptions and preferences.
- Enhanced Analytics: Use AWS CloudWatch for deeper insights into notification performance.