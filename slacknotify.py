# Author: Bruno Vilalba
#
# Description: This updated script provides a structured and organized way to send notifications to a Slack channel. 
#
# Prerequisites: Make sure you have the slack package installed in your Python environment before running this script. You can install it using pip install slackclient.
#
# Configuration: Replace the placeholder values ('your_slack_api_token_here' and 'your_slack_channel_here') with your actual Slack API token and desired Slack channel ID or name.
#
import slack

def send_notification(slack_token, channel, message):
    client = slack.WebClient(token=slack_token)
    response = client.chat_postMessage(channel=channel, text=message)
    
    if response["ok"]:
        print("Notification sent successfully to Slack channel!")
    else:
        print("Failed to send notification to Slack channel. Error: {}".format(response["error"]))

# Replace 'slack_token' with your actual Slack API token
slack_token = "your_slack_api_token_here"

# Replace 'channel' with the desired Slack channel ID or name
channel = "your_slack_channel_here"

# Customize the notification message as needed
message = "This is a test notification from the script."

send_notification(slack_token, channel, message)
