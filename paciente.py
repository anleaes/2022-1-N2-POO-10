class Paciente:

  def __init__(self, tipo, raca, idade, peso, nome_pet, descricao_pet, cliente, animal):
    super().__init__(tipo, raca, idade, peso)
    self.nome_pet = nome_pet
    self.descricao_pet = descricao_pet
    self.cliente = cliente
    self.animal = animal

  def registra_paciente(self):
    return 'Registro realizado!'