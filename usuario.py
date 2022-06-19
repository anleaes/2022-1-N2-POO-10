from asyncio.windows_events import NULL


class Usuario:

  def __init__(self, login, senha, email):
    self._login = login
    self._senha = senha
    self._email = email

  def valida_login(self):
    if self._login != NULL:
      return 'Login realizado com sucesso'
