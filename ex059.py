# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] Somar
# [2] Multiplicar
# [3] Maior valor
# [4] Digitar novos numeros
# [5] Sair do programa
#  Seu programa devera realizar a operaçao solicitada em cada caso.

from time import sleep

escolha = 0

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

while escolha != 5:
    sleep(1)
    print('\n[1] Somar\n[2] Multiplicar\n[3] Maior valor\n[4] Digitar novos numeros\n[5] Sair do programa')
    escolha = int(input('Escolha a opção desejada: '))
    if escolha == 1:
        print(f'\nSoma: {num1} + {num2} = {num1 + num2}')
    elif escolha == 2:
        print(f'\nMultiplicar: {num1} * {num2} = {num1 * num2}')
    elif escolha == 3:
        maior = [num1, num2]
        maior.sort()
        print(f'Maior valor digitado foi o {maior[-1]}')
    elif escolha == 4:
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
    else:
        pass
sleep(1)
print('Fim do programa')