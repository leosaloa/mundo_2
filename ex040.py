# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entra 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

from colorama import init, Fore, deinit

n1 = float(input('\nDigite a primeira nota: '))
n2 = float(input('\nDigite a segunda nota: '))
media = (n1 + n2) / 2

if media < 5:
    print('\nVocê foi', Fore.RED, 'REPROVADO', Fore.RESET, 'estude mais!')
elif media >= 5 and media <= 6.9:
    print('\nVocê esta em', Fore.LIGHTBLUE_EX, 'RECUPERAÇÃO', Fore.RESET, 'estude para não reprovar.')
elif media >= 7:
    print('\nParabéns você foi', Fore.GREEN, 'APROVADO!', Fore.RESET)
else:
    print('Verificar notas digitadas.')