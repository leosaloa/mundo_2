# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior      O segundo valor é maior     Não existe valor maior, os dois são iguais

from colorama import init, Fore, deinit

init()

print(Fore.YELLOW, '-=-' * 20)
print('          Comparações de numeros')
print(Fore.YELLOW, '-=-' * 20, Fore.RESET)

n1 = int(input('\nDigite o primeiro valor: '))
n2 = int(input('\nDigite o segundo valor: '))

if n1 > n2:
    print('\nO primeiro valor é o maior!')
elif n2 > n1:
    print('\nO segundo valor é o maior!')
elif n1 == n2:
    print('\nO valores são iguais!')
else:
    print('\nAlgo deu errado, digite os valores novamente!')

deinit()