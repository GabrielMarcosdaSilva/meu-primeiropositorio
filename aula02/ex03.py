#3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

gênero = str(input('Diga seu gênero F= Feminino ou M= Masculino: '))

if gênero == 'm':
    print('Gênero Masculino')
if gênero == 'f':
    print('Gênero Feminino')
else:
    print('Não temos essa opição')
