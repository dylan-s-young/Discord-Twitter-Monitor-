# ****Update Logs****

## ```Update Version 0.0.1```
### 12/22/20
- Pushed twitter_monitor logic to github. 
- Basic Structure for webhook

## ```Update Version 0.0.2```
### 12/22/20
- Made webhook_details.py & twitter_details.py where you input credentials 

## ```Update Version 0.0.3```
### 12/23/20
- Minor Tweeks to some python files. 
- Got rid of print statement in "initial_tweet" function. 
- Algorithm will send webhook depending on the 'created_at' in the JSON_File.
- Notes: 
    - Created Class Twitter_user() 
    - Will add webhook post before monitor starts letting the user know what is being monitored.
    - Have Error with profile pic being sent. (might being rate-limited?)
## ```Update Version 0.0.4```
### 12/23/20
- Fixed profile pic being sent in webhook.
- Sends Webhook of who is being monitored. 
- Minor tweaks to different methods. 
- Notes: 
    - Will add follow count and more. (See what I can add from JSON)
## ```Update Version 0.0.5```
### 12/23/20
- Tweak to fix image posting in 'Twitter_details.py'
- Bugs:
    - If a photo is available, full_text will post the https link along with the text in the tweet. (Can fix by filtering out https://)
## ```Update Version 0.0.6```
### 12/24/20
- Minor tweaks. 
- Added README.md
- Notes:
    - Added recursion limit and increased delay to 20 seconds. 
    - You will have to restart bot ater a certain amount of time.
