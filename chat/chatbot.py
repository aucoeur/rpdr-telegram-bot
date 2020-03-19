import os, requests, json, pprint
from telegram import ChatAction
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from functools import wraps
from utils import send_typing_action


@send_typing_action
def reply(update, context):
    """Checks the user message to see if there is a matching response, else echos the user."""
    update.message.reply_text(update.message.text)