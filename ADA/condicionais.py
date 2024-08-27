 # Condicionais Estruturadas

idade = int(input('Insira sua idade: '))

if idade >= 18:
    print('Você já pode fazer o cadastro na nossa plataforma!')
elif idade == 17:
    print('Volte daqui a 1 ano')
else:
    print('Volte daqui a', (18 - idade), 'anos')

