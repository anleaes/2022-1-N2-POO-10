from usuario import Usuario
from paciente import Paciente
from tratamento import Tratamento
from funcionario import Funcionario

class Menu:

  def login_menu():
    user = None
    while True:
      resposta = int(input('\n1: Criar conta \n2: Recuperar senha \n3: Acessar a conta\n'))
      
      if resposta == 1:
        if user is None:
          user = Usuario.novo_usuario()
          print('Usuario criado com sucesso!')
        else:
          user.Usuario.valida_login()
      elif resposta == 2:
        if user is None:
          print('Usuário não encontrado.')
        else:
          user.Usuario.recupera_senha()
      elif resposta == 3:
        if user is None:
          print('Usuário não encontrado.')
        else:
          break
      else:
        exit()

  def animal_menu():
    pet = None
    while True:   
      resposta = int(input('\n1: Registrar um pet \n2: Agendar tratamento \n3: Consultar profissionais\n4: Encerrar sessão \n'))
      
      if resposta == 1:
        pet = Paciente.registra_pet()
        print('Pet registrado com sucesso!')
      elif resposta == 2:
        if pet is None:
          print('Você não possui nenhum pet registrado.')
        else:
          pet.Tratamento.agenda_tratamento()
      elif resposta == 3:
        if pet is None:
          print('Você não possui nenhum pet registrado.')
        else:
          pet.Funcionario.registra_funcionario()
      elif resposta == 4:
          Usuario.altera_senha()
      elif resposta == 5:
        exit()
      else:
        break


