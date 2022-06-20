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

  def altera_senha(nova_senha):
    senha = nova_senha

  def recupera_senha(self):
    return self._senha