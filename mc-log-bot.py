import requests
import json
import tailer
import time
import os
import subprocess

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

# # ATTEMPT 1
# while True:
#     try:
#         print("Starting Tail of log")
#     # Define a function to handle log file updates
#         for line in tailer.follow(open(log_file, 'r')):
#             print("Debug: ",line)
#             # Check if a player joined or left the server
#             if 'joined the game' in line or 'left the game' in line:
#                 # Extract the player name from the log line
#                 player_name = line.split(' ')[-4].strip()

#                 # Construct the message to send to the webhook
#                 message = f'{player_name} has {("joined" if "joined" in line else "left")} the server!'

#                 # Send the message to the webhook
#                 send_webhook_message(message)
#     except:
#         print('Error: Follow script crashed. Waiting 5 minutes')
# #        message = "Oops. Bot Crashed. Waiting 5 minutes and trying again..."
# #        send_webhook_message(message)
#         time.sleep(300)


# ATTEMPT 2
while True:
    print('Debug: Starting. Setting initial file size to 0.')
    file_size = 0
    f = open(log_file, "r")
    try:
        while True:
            line = f.readline()
            if line:
                if 'joined the game' in line or 'left the game' in line:
                    print('Debug: Player joined/left the game!')
                    #  Extract the player name from the log line
                    player_name = line.split(' ')[-4].strip()

                    # Construct the message to send to the webhook
                    message = f'{player_name} has {("joined" if "joined" in line else "left")} the server!'

                    # Send the message to the webhook
                    send_webhook_message(message)
                print("Debug: ", line)
            file_status_obj = os.stat(log_file)
            if file_size > file_status_obj.st_size:
                f.close()
                time.sleep(10)
                f = open(log_file, "r")
                print('Reopening file. File size is less than previous file size. File likely rotated.')
                print("File Size: ", file_size)
                print("file_status_obj.st_size: ", file_status_obj.st_size)
            file_size = file_status_obj.st_size
            #print("File Size: ", file_size)
            time.sleep(1)
    except:
        print('Error: Follow script crashed. Sleeping 10 seconds. Server likely restarting and log file is being rotated.')
        time.sleep(10)
        f.close()
    f.close()

# # ATTEMPT 3
# while True:
#     try:
#         while True:
#             print("running process...")
#             line = subprocess.check_output(['tail', '-1', log_file])
#             if line:
#                 print("LINE HAS BEEN FOUND. TESTING. ###############################")
#                 if 'joined the game' in line or 'left the game' in line:
#                     print('Debug: Player joined/left the game!')
#                     #  Extract the player name from the log line
#                     player_name = line.split(' ')[-4].strip()

#                     # Construct the message to send to the webhook
#                     message = f'{player_name} has {("joined" if "joined" in line else "left")} the server!'

#                     # Send the message to the webhook
#                     send_webhook_message(message)
#                 print("Debug: ", line)
#             time.sleep(1)
#     except:
#         print('Error: Follow script crashed. Sleeping 10 seconds. Server likely restarting and log file is being rotated.')
#         time.sleep(10)