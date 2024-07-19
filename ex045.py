# Crie um programa que faça o computador jogar Jokenpô com você.

# Pedra > Tesoura
# Pedra = Pedra
# Pedra < Papel

# Papel > Pedra
# Papel = Papel
# Papel < Tesoura

# Tesoura > Papel
# Tesoura = Tesoura
# Tesoura < Pedra

from colorama import init, Fore, deinit
from random import randint
from time import sleep

pedra = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
papel = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
tesoura = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
versus = """

"""

print(Fore.YELLOW, '-=-'*15, Fore.RESET)
print('> '*9, Fore.GREEN,'JOKENPÔ', Fore.RESET,' <'*9)
print(Fore.YELLOW, '-=-'*15, Fore.RESET)
sleep(3)

maquina = randint(1,3)

print('\nESCOLHENDO...')
sleep(3)

print('\nPRONTO, FAÇA A SUA ESCOLHA!')
sleep(3)

jogador = int(input('\nEscolha qual vai jogar:\n\n1 - Pedra\n2 - Papel\n3 - Tesoura\n\nOpção: '))
sleep(1)

print(pedra)
sleep(1)
print(papel)
sleep(1)
print(tesoura)
sleep(1)

if (jogador == 1 and maquina == 3) or (jogador == 2 and maquina == 1) or (jogador == 3 and maquina == 2):
    print(f'\nVocê VENCEU!')
elif (jogador == 1 and maquina == 1) or (jogador == 2 and maquina == 2) or (jogador == 3 and maquina == 3):
    print(f'EMPATE!')
elif (jogador == 1 and maquina == 2) or (jogador == 2 and maquina == 3) or (jogador == 3 and maquina == 1):
    print(f'Você PERDEU!')

sleep(2)

print('\nFIM DE JOGO!')
sleep(3)
print('')
sleep(7)