import requests
import json
import tailer
import time

# Replace this with your own webhook URL
webhook_url = ''
log_file = 'logs/latest.log'

# Define the message content and other parameters
username = 'Minecraft Server'
#avatar_url = 'https://i.imgur.com/4M34hi2.png'

# Define a function to send a message to the webhook
def send_webhook_message(message):
    # Define the JSON payload
    payload = {
        'content': message,
        'username': username,
#        'avatar_url': avatar_url
    }

    # Send the HTTP POST request to the webhook URL
    response = requests.post(webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})

    # Check if the request was successful
    if response.status_code == 204:
        print('Message sent successfully!')
    else:
        print(f'Error {response.status_code}: {response.text}')

while True:
    try:
        print("Starting Tail of log")
    # Define a function to handle log file updates
        for line in tailer.follow(open(log_file, 'r')):
            print("Debug: ",line)
            # Check if a player joined or left the server
            if 'joined the game' in line or 'left the game' in line:
                # Extract the player name from the log line
                player_name = line.split(' ')[-4].strip()

                # Construct the message to send to the webhook
                message = f'{player_name} has {("joined" if "joined" in line else "left")} the server!'

                # Send the message to the webhook
                send_webhook_message(message)
    except:
        print('Error: Follow script crashed. Waiting 5 minutes')
#        message = "Oops. Bot Crashed. Waiting 5 minutes and trying again..."
#        send_webhook_message(message)
        time.sleep(300)


