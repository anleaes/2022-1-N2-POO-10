class Usuario:

  def __init__(self, login, senha, email):
    self._login = login
    self._senha = senha
    self._email = email

  def novo_usuario():
    return Usuario(
      login = input('Login: '),
      senha = input('Senha: '),
      email = input('E-mail: '),
    ) 

  def altera_senha(self):
    nova_senha = input('Nova senha: ')
    self._senha = nova_senha
    return 'Senha alterada!'

  def recupera_senha():
    return self._senha

  def valida_login(self):
    if self._login != NULL:
      return 'Login realizado com sucesso'