class Tratamento:

  def __init__(self, tipo, duracao, paciente, remedio):
    self.tipo = tipo
    self.duracao = duracao
    self.paciente = paciente
    self.remedio = remedio

  def agenda_tratamento():
    return Tratamento(
      tipo = input('Tipo: '),
      duracao = input('Duracao: ')
    )

  def examina_paciente(self):
    return 'Resultado do exame: '