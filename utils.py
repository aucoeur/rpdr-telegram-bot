from telegram import ChatAction
from telegram.ext import Updater
from functools import wraps

def send_typing_action(func):
    """Sends typing action while processing func command with @send_typing_action wrapper"""

    @wraps(func)
    def command_func(update, context, *args, **kwargs):
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        return func(update, context,  *args, **kwargs)

    return command_func