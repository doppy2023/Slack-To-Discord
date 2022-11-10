import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from discord_webhook import DiscordEmbed, DiscordWebhook
import requests
import shutil
import json

with open('settings.json', "r") as f:
    settings = json.load(f)

headers = {
    "Authorization": "Bearer " + settings["SLACK_BOT_TOKEN"]
}

# Initializes your app with your bot token and socket mode handler
app = App(token=settings["SLACK_BOT_TOKEN"], signing_secret= settings["SLACK_SIGNING_SECRET"])

def getText(event):
    #Check if message contain images:
        if event.get('files'):
            for (idx, image) in enumerate(event['files']):
                userId = image['user']
                imageFr = image['url_private']
                userRealName = app.client.users_info(user= userId)

                text = event['text']

                #Download image
                response = requests.get(imageFr, stream=True, headers= headers)
                with open('img.png', 'wb') as out_file:
                    shutil.copyfileobj(response.raw, out_file)
                del response
                
                
                webhook = DiscordWebhook(url= settings["DISCORD_WEBHOOK"], username= f"{userRealName['user']['real_name']} - via Slack", avatar_url= userRealName['user']['profile']['image_512'])
                
                if len(text) > 0 and idx == 0:
                    webhook.set_content(text)

                with open("img.png", "rb") as f:
                    webhook.add_file(file=f.read(), filename='img.png')   

                webhook.execute(remove_embeds=True, remove_files=True)
                os.remove('img.png')
        
        #If message doesn't contain images:
        else:
            userId = event['user']
            
            userRealName = app.client.users_info(user= userId)

            text = event['text']

            webhook = DiscordWebhook(url= settings["DISCORD_WEBHOOK"], username= f"{userRealName['user']['real_name']} - via Slack", avatar_url= userRealName['user']['profile']['image_512'])
            webhook.set_content(text)
            webhook.execute(remove_embeds=True, remove_files=True)

@app.event("message")
def event_handler(client, event, logger):


    #Get messages from everyone if array is empty.
    if len(settings['userToGetMessagesFrom']) == 0:
        getText(event)
    
    #Get messages from specific users.
    elif len(settings['userToGetMessagesFrom']) > 0:
        if event['user'] in settings['userToGetMessagesFrom']:
            getText(event)
    else:
        print("Error getting message for a specific user, please input a valid user ID in settings.json or leave it with empty.")
        return


# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, settings["SLACK_APP_TOKEN"]).start()