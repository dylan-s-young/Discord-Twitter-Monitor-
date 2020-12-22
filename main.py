#12/20/2020
from twitter_monitor import Monitor_user, initial_tweet
import time
from datetime import datetime
from discord_webhook_logic import post



#Multi-User monitoring will come in the future (Currently only support one user). Please input string only.
if __name__ == "__main__":
    username = input(f'Please input username to monitor.Example: @KanyeWest = \'KanyeWest\'\n')
    start_time = datetime.now()
    print(f'Monitor started at {start_time}')
    username, text , profile_image, media_image = initial_tweet(username)
    post(username, text, profile_image, media_image)