# Faça um programa que jogue PAR OU IMPAR com o computador. O jogo só será interrompido quando
# o jogador PERDER, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.

# VERIFICAR CONTADOR
import random

print('=-=' * 20)
print('\nVAMOS JOGAR PAR OU IMPAR\n')
print('=-=' * 20)

cont = 0

while True:
    soma = 0
    robo = random.randint(0, 10)
    jogador = int(input('Digite um valor: '))
    escolha = str(input('Você é PAR ou IMPAR? [P/I] ')).upper().strip()
    soma = jogador + robo
    par = soma % 2 == 0
    impar = soma % 2 != 0
    print('-' * 40)

    if par:
        print(f'Você jogou {jogador} e o computador {robo}. Total de {soma} DEU PAR')
    elif impar:
        print(f'Você jogou {jogador} e o computador {robo}. Total de {soma} DEU IMPAR')
    else:
        print('Algo deu errado! ERRO: 001')
    print('-' * 40)

    if (escolha == 'P' and par == True) or escolha == 'I' and impar == True:
        print(f'Você VENCEU!\nVamos jogar novamente...')
        cont += 1
    elif (escolha == 'P' and par == False) or (escolha == 'I' and impar == False):
        print(f'Você PERDEU!')
        print('=-=' * 20)
        print(f'GAME OVER! Você venceu {cont} vezes.')
        break
    else:
        print('Algo deu errado! ERRO: 002')

print('FIM DE JOGO')