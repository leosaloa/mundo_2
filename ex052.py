# Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo.
# Numero primo:
# 1- O numero é divisivel por 1
# 2- O numero é divisivel por ele mesmo
# 3- O numero não pode ser divisivel por algum numero menor que ele
# Exemplo 7 é um numero primo

from colorama import init, Fore, deinit

init() # iniciar biblioteca colorama

print('\nVerificação se o numero é primo.\n')
num = int(input('\nDigite um numero: '))
tipo = 0

if num <= 1:
    print('\nDigite o valor maior que 1.')
else:
    for contagem in range(1,num+1):
        if num % contagem == 0:
            tipo = tipo + 1
if tipo == 2:
    print('\nO numero é', Fore.GREEN, 'PRIMO', Fore.RESET)
else:
    print('\nO numero não é', Fore.RED, 'PRIMO', Fore.RESET)

deinit() # Finalizar biblioteca colorama