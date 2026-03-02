import os
import time

import dotenv
from slack_cleaner2 import SlackCleaner, match

dotenv.load_dotenv()

SLACK_USER_TOKEN = os.getenv("SLACK_USER_TOKEN")
if not SLACK_USER_TOKEN:
    exit("SLACK_USER_TOKEN must be set.")


SLACK_CHANNEL = os.getenv("SLACK_CHANNEL")
if not SLACK_CHANNEL:
    exit("SLACK_CHANNEL must be set.")

s = SlackCleaner(SLACK_USER_TOKEN)

print(f"Cleaning {SLACK_CHANNEL} 🧹")
print("Waiting 10 seconds before mass deletion... Ctrl+C to abort")
time.sleep(10)

# delete all messages in specified channel
for msg in s.msgs(filter(match(SLACK_CHANNEL), s.conversations)):
    # delete messages, its files, and all its replies (thread)
    msg.delete(replies=True, files=True)
