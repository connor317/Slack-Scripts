# Slack-Scripts
Scripts for making slack easier to use as admins

Attendance.py

This script was originally created to collect attendance for meetings.  We used reactions to a message to see who all was at the meeting.
The script will output all of the names of who was at the meeting and a total of how many people were at the meeting.  
It does check for unique users, so if a user did react with multiple different reactions then they will still only show once.  

Some edits are needed to make this script work:
1. Add your channel's ID to the querystring on line 4
2. Add your API token on line 7
3. Add your postman token on line 11

NOTES:
  The message must be pinned and be the most recent pinned comment
  It must have at least one reaction

