class SessionCore:
  def __init__(self, bot):
    self.sessions = bot.sessions
  
  def get_user_id(self, a):
    user = a.data.get('from')
    if user:
      return user.get('id')

  def set_session(self, a):
    user_id = self.get_user_id(a)
    if user_id:
      session = self.sessions.get(user_id)
      if not session:
        session = {}
        self.sessions[user_id] = session
      a.session = session
    