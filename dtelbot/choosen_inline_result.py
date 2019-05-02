class ChosenInlineResult:
    def __init__(self, data, bot, args=[]):
        self.data = data
        self.args = args
        self.type = 'chosen_inline_result'
        self.bot = bot
        self.session = None