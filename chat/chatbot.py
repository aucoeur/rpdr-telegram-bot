from chatterbot import ChatBot, comparisons

chatbot = ChatBot('RPDR bot',
    logic_adapters=[{
        'import_path': 'chatterbot.logic.BestMatch',
        "statement_comparison_function": comparisons.levenshtein_distance,
        'default_response': 'I am sorry, but I do not understand.',
        'maximum_similarity_threshold': 0.90 }]
    )


response = chatbot.get_response("Hello")
print(response)