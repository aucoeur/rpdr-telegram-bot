from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from functools import wraps
import os

GIPHY_KEY = os.getenv("GIPHY_KEY")

def gif_random(update, context):
    '''Gets a random RPDR gif from GIPHY endpoint https://developers.giphy.com/docs/api/endpoint/#random'''
    pass