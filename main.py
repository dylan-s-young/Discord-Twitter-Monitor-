#12/20/2020
from twitter_monitor import *
import time
from datetime import datetime
from discord_webhook_logic import post
import sys


#Multi-User monitoring will come in the future (Currently only support one user). Please input string only.
if __name__ == "__main__":
    sys.setrecursionlimit(10**9)
    username = input(f'Please input username to monitor. Example: @KanyeWest = \'KanyeWest\' (CTRL-C to end)\n')
    start_time = datetime.now()
    print(f'Monitor started at {start_time}')
    user = twitter_user(username)
    user.user_being_monitored()
    