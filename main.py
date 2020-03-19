#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
from dotenv import load_dotenv
import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from gif import gif_random
from chatbot import reply

load_dotenv()

TOKEN = os.getenv("TOKEN")
HEROKU_URL = os.getenv("HEROKU_URL")
PORT = int(os.getenv('PORT', '8443'))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

# Basic command functions
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! Hello! How are you?')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Who\'s after Peppermint? Not Shea Coulee!')

def unknown(update, context):
    """Sends message in event of unknown command.  Must be placed last"""
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ex-squeeeeeeeze me???")

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

# Define handlers

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Command handlers 
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("random", gif_random))

    dp.add_handler(MessageHandler(Filters.command, unknown))

    # Message (non-command) Handler - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, reply))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot

    if os.getenv('ENV') == 'dev':
        # For local dev, use polling
        updater.start_polling()
        print('Running local dev envrionment')
    else:
        # For heroku, use webhook
        updater.start_webhook(listen="0.0.0.0",
                            port=PORT,
                            url_path=TOKEN)
        updater.bot.set_webhook(HEROKU_URL + TOKEN)

    updater.idle()


if __name__ == '__main__':
    main()