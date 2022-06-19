class Cliente: 

  def __init__(self, nome, cpf, endereco, telefone, usuario):
    self.nome = nome
    self._cpf = cpf
    self.endereco = endereco
    self.telefone = telefone
    self.usuario = usuario

  def personaliza_perfil(self):
    return 'Alteração realizada!'

  def altera_senha(self):
    return 'Senha alterada!'

  def novo_cliente(self):
    return 'Registro concluído!'