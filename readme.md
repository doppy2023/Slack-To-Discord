### Slack To Discord Bot

This is a simple bot that will relay messages from a Slack channel to a Discord channel. All you have to do is add this bot to a channel in your Slack workspace and a webhook in your Discord server, then the bot will do the rest.

# Requirements

- Python 3.10+ (https://www.python.org/downloads/)
- Rename `sample_settings.json` to `settings.json`

# Creating the bot on Slack

1. Create a new Slack app at https://api.slack.com/apps
2. Click on create from an app manifest
3. Click on Json and remove everything inside
4. Open manifest.json and copy all the contents inside, then paste it in the website
5. Click on Install App to Workspace
6. Click on OAuth & Permissions
7. Copy the bot token and input it in the settings.json file, inside of the quotation marks where it says SLACK_BOT_TOKEN
8. In the Basic Information section, copy the signing secret and input it in the settings.json file, inside of the quotation marks where it says SLACK_SIGNING_SECRET
9. In the Basic Information section, scroll down to App-Level tokens, click on generate Token and Scopes, and choose the following scope: connections:write, and name it whatever you want, then copy and paste it inside SLACK_APP_TOKEN in the settings.json

# Running the bot
- Open a terminal in the folder where the bot is located
- Run the following command: `python3 -m pip install -r requirements.txt` or `py -m pip install -r requirements.txt` or `python -m pip install requirements.txt`
- Run the following command: `python3 main.py` or `py main.py` or `python main.py`
- The bot will now be running

# Creating the webhook on Discord

- Go to your Discord server
- Go to a channel where you want the messages to be fowarded to
- Go to Integrations
- Click on Webhooks
- Click on New Webhook
- Copy the webhook and put it in settings.json

# Adding new users

- Copy the user's ID from Slack and paste it in the userToGetMessagesFrom list in settings.json

Example:

```
{
    "userToGetMessagesFrom": [

        "USERIDGOESHERE",
        "USERID2GOESHERE
    ]
}
```

- The last element of the array MUST NOT contain a comma. Only add a comma if you're adding new elements.

