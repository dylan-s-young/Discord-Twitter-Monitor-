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