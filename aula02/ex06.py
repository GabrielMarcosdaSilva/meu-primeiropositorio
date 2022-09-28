#6 - Faça um Programa que leia três números e mostre-os em ordem decrescente.
num1 = float(input("Digite Seu Primeiro Número: "))
num2 = float(input("Digite Seu Segundo Número: "))
num3 = float(input("Digite Seu Terceiro Número: "))

if num1 > num2 and num3:
    print('Seu primeiro número foi o maior')

if num2 > num1 and num3:
    print('Seu primeiro número foi o maior')

if num3 > num1 and num2:
    print('Seu primeiro número foi o maior')


