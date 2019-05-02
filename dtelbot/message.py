from .methods import Methods

class Message(Methods):
    def __init__(self, type, data, args, bot):
        self.data = data
        self.args = args
        self.type = type
        self.bot = bot
        self.session = None
    
    @property
    def chat_id(self):
        return self.get_chat_id()

    @property
    def token(self):
        return self.bot.token

    @property
    def proxy(self):
        return self.bot.proxy

    @property
    def input(self):
        return self.args[0]