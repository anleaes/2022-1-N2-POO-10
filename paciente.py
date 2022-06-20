class Paciente:

  def __init__(self, tipo, raca, idade, peso, nome_pet, descricao_pet, animal):
    #super().__init__(tipo, raca, idade, peso)
    self.nome_pet = nome_pet
    self.descricao_pet = descricao_pet
    self.animal = animal

  def registra_pet():
    return Paciente(
      tipo = input('Tipo: '),
      raca = input('Raça: '),
      idade = int(input('Idade: ')),
      peso = input('Peso: '),
      nome_pet = input('Nome: '),
      descricao_pet = input('Descricao: '),
      animal = 'Animal'
    ) 

  def consulta_pet(self):
    return self.nome_pet