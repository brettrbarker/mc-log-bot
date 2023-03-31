FROM python:3.9-slim-buster

# Install dependencies
RUN apt-get update && \
    apt-get install -y git && \
    pip install requests tailer 

# Copy bot script into container
WORKDIR /app
COPY mc-log-bot.py .

# Set environment variables
#ENV BOT_TOKEN=your-bot-token
#ENV LOG_FILE=/path/to/log/file
#ENV CHANNEL_ID=your-channel-id

# Start bot script
CMD ["python", "-u", "mc-log-bot.py"]
