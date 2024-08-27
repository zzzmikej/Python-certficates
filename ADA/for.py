for variavel in range(5):
    print(variavel)


for variavel in range(1, 10):
    print(variavel)

for variavel in range(5, 50, 5):
    print(variavel)

nota1 = 0
nota2 = 0
nota3 = 0
for variavel in range(3):
    notavariavel = float(input('Informe sua nota:'))
    if notavariavel != 0 and variavel == 0:
        nota1 = notavariavel
    elif notavariavel != 0 and variavel == 1:
        nota2 = notavariavel
    else:
        nota3 = notavariavel
    print(notavariavel)

print('Sua media final foi:\n', ((nota1 + nota2 + nota3) / 3))