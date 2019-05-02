import json

class InlineQuery:
    def __init__(self, data, bot, args=[]):
        self.data = data
        self.args = args
        self.type = 'inline_query'
        self.bot = bot
        self.session = None
        
    def answer(self, results, **kwargs):
        kwargs['inline_query_id'] = self.data['id']
        kwargs['results'] = json.dumps(results)
        return self.bot.method('answerInlineQuery', **kwargs)
