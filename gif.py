from dotenv import load_dotenv
import os, requests, json, pprint
from telegram import ChatAction
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from functools import wraps
from utils import send_typing_action

load_dotenv()
pp = pprint.PrettyPrinter(indent=1)

GIPHY_KEY = os.getenv("GIPHY_KEY")

@send_typing_action
def gif_random(update, context):
    '''Gets a random RPDR gif from GIPHY endpoint https://developers.giphy.com/docs/api/endpoint/#random
    
    Example: https://api.giphy.com/v1/gifs/random?api_key=[GIPHY_KEY]&tag=rpdr&rating=R '''

    url = "https://api.giphy.com/v1/gifs/random"
    params = {
        'api_key': GIPHY_KEY,
        'tag': "RPDR",
        'rating': "R"
    }

    response = requests.get(url, params)
    json = response.json()
    gif_link = json['data']['fixed_height_downsampled_url']
    # pp.pprint(gif_link)
    context.bot.send_animation(update.effective_chat.id, gif_link)