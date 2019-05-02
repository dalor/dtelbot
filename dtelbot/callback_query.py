class CallbackQuery:
    def __init__(self, data, bot, args=[]):
        self.data = data
        self.args = args
        self.type = 'callback_query'
        self.bot = bot
        self.session = None
        
    def answer(self, **kwargs):
        kwargs['callback_query_id'] = self.data['id']
        return self.bot.method('answerCallbackQuery', **kwargs)
    