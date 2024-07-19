# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com a idade
# Até 9 anos: MIRIM     Até 14 anos: INFANTIL       Até 19 anos: JUNIOR     Até 20 anos: SÊNIOR     Acima: MASTER

from datetime import datetime

nasc = int(input('\nDigite o ano de nascimento do atleta: '))
ano = datetime.now().year
idade = ano - nasc

if idade <= 9:
    print('\nCategoria MIRIM.')
elif idade <= 14:
    print('\nCategoria INFANTIL')
elif idade <= 19:
    print('\nCategoria JUNIOR')
elif idade <= 20:
    print('\nCategoria SENIOR')
elif idade > 20:
    print('\nCategoria MASTER')
else:
    print('\nVerificar idade digitada')