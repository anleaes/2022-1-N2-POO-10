class Cliente: 

  def __init__(self, login, senha, email, nome, cpf, endereco, telefone, usuario):
    super().__init__(login, senha, email)
    self.nome = nome
    self._cpf = cpf
    self.endereco = endereco
    self.telefone = telefone
    self.usuario = usuario
    
  def novo_cliente():
    return Cliente(
      nome = input('Nome: '),
      cpf = input('CPF: '),
      endereco = input('Endereço: '),
      telefone = input('Telefone: ')
    )