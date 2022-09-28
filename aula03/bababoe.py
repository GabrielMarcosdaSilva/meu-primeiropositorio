num1 = int(input('digite número'))
num2 = int(input('Digite seu segundo número'))
num3= int(input('Digite seu terceiro número'))

soma = num1+ num2+ num3

if soma >=30 and soma <= 50:
    print(f'Você ficou dentro do orçamente, você gastou: {soma}')

if soma > 50:
    print(f'você ficou acima do orçamento, você gastou: {soma}')

if soma < 30:
    print(f'Parabens você gastou abaixo da média, você gastou {soma}')