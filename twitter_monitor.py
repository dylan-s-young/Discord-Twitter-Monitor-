import tweepy
import time
import json
import sys
from datetime import datetime
from twitter_details import auth_keys,api_keys

auth = tweepy.OAuthHandler(api_keys[0],api_keys[1]) #API Keys
auth.set_access_token(auth_keys[0],auth_keys[1]) #Auth Tokens
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def initial_tweet(username):
    """
    Summary: 
    Prints Initial Tweet that is being monitored. 
    Returns:
    username
    text from tweet 
    """
    tweets = api.user_timeline(screen_name = username, count = 200, include_rts = False, tweet_mode = 'extended')
    
    status = tweets[0]
    json_str = json.dumps(status._json)
    parsed_json = json.loads(json_str)
    print(json.dumps(parsed_json,indent=4, sort_keys=True))
    text = ''
    text += parsed_json['full_text'] #Grabs Tweet Info 
    profile_img = ''
    profile_img += parsed_json['user']['profile_image_url'] #Gets profile image
    media_image = ''
    try:
        media_image += parsed_json['entities']['media'][0]['media_url']
    except:
        media_image = False
    return username , text , profile_img, media_image, 

def Monitor_user(username, created_at):
    pass