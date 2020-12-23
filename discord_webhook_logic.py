import emoji
from discord_webhook import DiscordWebhook, DiscordEmbed
from webhook_details import webhook_list


def post(username, text, pfp_image, mediaurl):
    '''
    username: username of twitter user
    text: tweet information
    pfp_image: profile image of twitter user 
    mediaurl: will embed in webhook
    '''
    user_handler = 'twitter.com/' +username
    embed = DiscordEmbed(title = f'Tweet', description = text, color=242424)
    embed.set_timestamp()
    embed.add_embed_field(name='Twitter', value = user_handler)
    embed.set_footer(text = emoji.emojize('Version 0.0.2 | Coded by Dylan:thumbs_up:'))
    webhook = DiscordWebhook(url = webhook_list)
    embed.set_author(name = username, url = 'https://'+ user_handler, icon_url = pfp_image)
    webhook.add_embed(embed)
    if mediaurl != False:
        embed.set_image(url = mediaurl)
    
    response = webhook.execute()


