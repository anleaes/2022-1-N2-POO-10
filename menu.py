from usuario import Usuario
from paciente import Paciente
from tratamento import Tratamento
from funcionario import Funcionario
from animal import Animal

class Menu:

  def login_menu():
    user = None
    while True:
      resposta = int(input('\n1: Criar conta \n2: Recuperar senha \n3: Acessar a conta\n'))
      
      if resposta == 1:
        if user is None:
          user = Usuario.novo_usuario()
          print('\nUsuario criado com sucesso!')
        else:
          print('\nAcesse sua conta')
      elif resposta == 2:
        if user is None:
          print('\nUsuário não encontrado.')
        else:
          print(user.recupera_senha())
      elif resposta == 3:
        if user is None:
          print('\nUsuário não encontrado.')
        else:
          break
      else:
        exit()

  def pet_menu():
    pet = None
    while True:   
      resposta = int(input('\n1: Registrar um pet \n2: Consultar pet\n3: Agendar tratamento\n4: Alterar senha \n5: Encerrar sessão \n'))
      
      if resposta == 1:
        if pet is None:
          pet = Paciente.registra_pet()
          print('\nPet registrado com sucesso!')
        else:
          print(f'\nJá possui um pet registrado {pet.nome_pet}')
      elif resposta == 2:
        if pet is None:
          print('\nVocê não possui nenhum pet registrado.')
        else:
          print(pet.consulta_pet())
      elif resposta == 3:
        if pet is None:
          print('\nVocê não possui nenhum pet registrado.')
        else:
          tratamento = Tratamento.agenda_tratamento()
          print('\nTratamento agendado!')
      elif resposta == 4:
          nova_senha = input('Nova senha: ')
          Usuario.altera_senha(nova_senha)
          print('\nSenha alterada!')
      elif resposta == 5:
        exit()
      else:
        break

  def admin_menu():
    admin = None
    while True:   
      resposta = int(input('\n1: Registrar Funcionario \n2: Buscar funcionario \n3: Alterar senha \n4: Encerrar sessão \n'))
      
      if resposta == 1:
        admin = Funcionario.registra_funcionario()
        print('\nFuncionário registrado com sucesso!')
      elif resposta == 2:
          consulta = admin.consulta_funcionario()
          print(consulta)
      elif resposta == 3:
          nova_senha = input('Nova senha: ')
          Usuario.altera_senha(nova_senha)
          print('\nSenha alterada!')
      elif resposta == 4:
        exit()
      else:
        break


