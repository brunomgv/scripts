#!/bin/bash
# Author: Bruno Vilalba
# Description: This bash script provides a structured and organized way to send notifications to a Slack channel.
#
# Prerequisites: Bash and connection with the internet
#
# Configuration: Feel free to customize the message sent
#
# Usage: sh slacknotify.sh "Message"
#
# e.g. sh slacknotify.sh "Hello, World!"

# Check if the argument is provided
if [ $# -eq 0 ]; then
  echo "Please provide a message as an argument."
  exit 1
fi

# Get the message from the command line argument
message="$1"

# Define the Slack webhook URL
webhook_url=""

# Send the curl request
curl -X POST -H 'Content-type: application/json' --data "{\"text\":\"Message: $message\"}" "$webhook_url"
