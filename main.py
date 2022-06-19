from menu import Menu
from usuario import Usuario

print('Bem vindo a Clinica Master Pet!')
print('Digite a opcao desejada: ')

Menu.login_menu()

print('Digite a opcao desejada: ')

Menu.animal_menu()

resp = print('Deseja encerrar a sessão? S/N')
if (resp == 'S'):
  Menu.login_menu()
else:
  Menu.animal_menu()

