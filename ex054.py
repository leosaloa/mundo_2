# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atiginram a maioridade e quantas já são maiores.       MAIORIDADE = 21 ANOS

from datetime import date
data = date.today().year

cont = 0
menor = 0
maior = 0

for nome in range(0,7):
    cont = cont+1
    ano = int(input(f'\nDigite o ano de nascimento da {cont} pessoa: '))
    idade = data - ano
    if idade < 21:
        menor += 1
    elif idade >= 21:
        maior += 1
print(f'\nPessoas menor de idade: {menor}.\nPessoas maior de idade: {maior}.')