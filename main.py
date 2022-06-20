from menu import Menu
from usuario import Usuario
from animal import Animal

print('Bem vindo a Clinica Master Pet!')
print('Digite a opcao desejada: ')

Menu.login_menu()

print('\nDigite a opcao desejada: ')

#if Usuario._login == 'admin':
#  Menu.admin_menu()
#else:
Menu.pet_menu()

resp = print('Deseja encerrar a sessão? S/N')
if (resp == 'S'):
  exit()
else:
  Menu.pet_menu()

