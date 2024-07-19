# Desenvolva um programa que leia o primeiro termo e a razao de uma Progressão aritimetica.
# No final, mostre os 10 primeiros termos dessa progressão.

termo_inicial = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

for contagem in range(10):
    termo = termo_inicial + (contagem * razao)
    print(termo, end = ' > ')
print('Acabou')