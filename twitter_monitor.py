import tweepy
import time
import json
from datetime import datetime
from twitter_details import auth_keys,api_keys
from discord_webhook_logic import *


auth = tweepy.OAuthHandler(api_keys[0],api_keys[1]) #API Keys
auth.set_access_token(auth_keys[0],auth_keys[1]) #Auth Tokens
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


class twitter_user():
    def __init__(self,username):
        self.username = username
        self.media_image = ""
        self.text = ""
        self.profile_img = ""
        self.created_at = ""
    def monitoring_tweets(self):
        """
        Summary: 
        Prints Initial Tweet that is being monitored. 
        Returns:
        username
        text from tweet 
        """
        tweets = api.user_timeline(screen_name = self.username, count = 200, include_rts = False, tweet_mode = 'extended')
        status = tweets[0]
        json_str = json.dumps(status._json)
        parsed_json = json.loads(json_str)

        monitoring_next = parsed_json['created_at']
        if monitoring_next == self.created_at:
            print(f'No new tweets @ {datetime.now()}...Sleeping for 10 Seconds.')
            time.sleep(10)
        else:
            print(f'New Tweet Detected! Posting to webhook.')
            self.created_at = monitoring_next
            self.text += parsed_json['full_text'] #Grabs Tweet Info 
            try:
                self.media_image += parsed_json['entities']['media'][0]['media_url']
            except:
                self.media_image = False
            print(self.media_image)
            post(self.username,self.text,self.profile_img,self.media_image) #posts tweet
        self.monitoring_tweets()
            

    def user_being_monitored(self): 
        tweets = api.user_timeline(screen_name = self.username, count = 200, include_rts = False, tweet_mode = 'extended')
        status = tweets[0]
        json_str = json.dumps(status._json)
        parsed_json = json.loads(json_str)
        tweet_created = parsed_json['created_at']
        self.created_at = tweet_created
        self.profile_img += parsed_json['user']['profile_image_url'] #sets profile image
        print(f'{self.username} is being monitoed. Posting to webhook.')
        monitoring_post(self.username,self.profile_img)
        print(f'Last tweet was @ {self.created_at}. Monitoring for next tweet....')
        self.monitoring_tweets()

        
        