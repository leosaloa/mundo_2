# Refaça o desafio 009, mostrando a tabuada de um nuero que o usuario escolher, so que agora utilizando um laço for.

num = int(input('\nDigite um numero para saber sua tabuada: '))

for contagem in range(1, 11):
    print(f'{num} x {contagem:>2} = {num*contagem}')