import os
from dotenv import load_dotenv

from chatterbot import ChatBot, comparisons, filters
from chatterbot.response_selection import get_random_response
from functools import wraps
from utils import send_typing_action

load_dotenv()
# MONGODB_URI = os.getenv(MONGODB_URI)

chatbot = ChatBot('RPDR bot',
        # storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
        # database_uri='mongodb://localhost:27017/rpdr-chatterbot',
        # logic_adapters=[{
        #     'import_path': 'chatterbot.logic.BestMatch',
        #     "statement_comparison_function": comparisons.levenshtein_distance,
        #     'default_response': 'I think I misunderstood the assignment.',
        #     'maximum_similarity_threshold': 0.5}],
        # tie_breaking_method="random_response",
        default_response = 'I think I misunderstood the assignment.',
        filters=[filters.get_recent_repeated_responses],
        response_selection = get_random_response
    )

@send_typing_action
def reply(update, context):
    """Checks message against db and replies to the best of its ability"""
    msg = update.message.text

    response = chatbot.get_response(msg)

    context.bot.send_message(chat_id=update.effective_chat.id, text=str(response))