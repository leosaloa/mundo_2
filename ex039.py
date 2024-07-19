# Faça um programa que leia o ano de nascimento de um jovem e informe,  de acordo com a sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import datetime

nasc = int(input('\nDigite seu ano de nascimento: '))
ano = datetime.now().year
idade = ano - nasc

if idade < 18:
    print(f'\nVocê ainda vai se alistar!\nFalta {(18 - idade) * 12} meses')
elif idade == 18:
    print('\nEsta na hora de se alistar!')
elif idade > 18:
    print(f'\nPassou do tempo de se alistar!\nVocê passou {(idade - 18) * 12} meses')