class Funcionario:

  def __init__(self, matricula, nome_profissional, especialidade, tratamento):
    self.matricula = matricula
    self.nome_profissional = nome_profissional
    self.especialidade = especialidade
    self.tratamento = tratamento

  def registra_funcionario():
    return Funcionario(
      matricula = input('Matricula: '),
      nome_profissional = input('Nome: '),
      especialidade = input('Especialidade: ')
  )

  def consulta_funcionario(self):
    return Funcionario(
      self.matricula,
      self.nome_profissional,
      self.especialidade
  )