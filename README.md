# mc-log-bot
Minecraft Server Log Bot. Send Minecraft server login notifications to a Discord channel webhook.


## Build Command
docker build -t mc-log-bot-image .

## Docker Start Command
docker run -d --name mc-log-bot -v [Path to Your Log Directory]:/app/logs/ mc-log-bot-image
