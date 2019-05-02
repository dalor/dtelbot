from .session_core import SessionCore

class Session(SessionCore):
  def __init__(self, bot):
    super().__init__(bot)
    
  def reg(self, old):
    def new(thread, a, *args, **kwargs):
      self.set_session(a)
      old(thread, a, *args, **kwargs)
      return old
    return new
      