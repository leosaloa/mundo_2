# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um numero entre 0 e 10.
# So que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessarios para vencer.

from time import sleep
from colorama import init, Fore, deinit
from random import randint

init()

sorte = randint(0,10)
tentativas = 0
chute = ''

print(Fore.YELLOW, '-=-'*30)
print(Fore.BLUE,'Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print(Fore.YELLOW, '-=-'*30, Fore.RESET)

print(Fore.CYAN, 'Pensando em um numero...', Fore.RESET)
sleep(2)

while sorte != chute:
    chute = int(input('Adivinhe o numero de 0 a 10: '))
    tentativas += 1
    if sorte != chute:
        print('Você errou tente novamente!')
print(f'Você acertou e teve {tentativas} tentativas.')

deinit()