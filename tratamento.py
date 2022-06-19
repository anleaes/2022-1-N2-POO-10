class Tratamento:

  def __init__(self, tipo, duracao, paciente, vacina, remedio):
    self.tipo = tipo
    self.duracao = duracao
    self.paciente = paciente
    self.remedio = remedio

  def realiza_receita(self):
    return 'Receita pronta!'

  def examina_paciente(self):
    return 'Resultado do exame: '