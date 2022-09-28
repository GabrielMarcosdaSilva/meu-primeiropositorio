nota = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))

média = (nota + nota2)/2

if média > 7:
    print('Aprovado')
elif média ==6:
    print('Em exame')
else:
    print('Recuperação')