from limpar_console import limpar_console
from menu import show_menu

exit = False

limpar_console()

while exit != True:
    show_menu()
    op = int(input())
    if op == 1:
        print('Saindo do Programa')
    elif op == 2:
        print('Saindo do Programa')
    elif op == 3:
        print('Saindo do Programa')
    elif op == 4:
        print('Saindo do Programa')
    elif op == 5:
        print('Saindo do Programa')
    elif op == 6:
        print('Saindo do Programa')
    elif op == 7:
        print('Saindo do Programa')
        exit = True
    else:
        print('Opção Invalida')