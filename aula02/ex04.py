#4 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
          #A mensagem "Aprovado", se a média alcançada for maior ou igual a 7;
          #A mensagem "Reprovado", se a média for menor do que 5;
          #A mensagem "Aprovado com Distinção", se a média for igual a 10.
          #A mensagem "Exame" se a média for menor ou igual a 6;
nota = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota+nota2)/2


if media >= 7:
    print('Aprovado')
if media < 5:
    print('Reprovado')
if media == 10:
    print('Aprovado com Distinção')
if media <= 6:
    print('Exame')