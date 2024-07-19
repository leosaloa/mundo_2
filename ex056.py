# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final o programa, mostre: 
# A media de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres tem menos de 20 anos.

cont = 0
media = 0
maioridade = 0
nomevelho = ''
mulher20 = 0

for contagem in range(1, 5):
    cont += 1
    print(f'\n-------{cont}ª PESSOA -------')
    nome = str(input(f'\nNome: '))
    idade = int(input(f'\nIdade: '))
    sexo = str(input(f'\nSexo [M/F]: '))
    media += idade
    if contagem == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
print(f'\nA média do grupo é {media//4:.2f}.')
print(f'\nO homem mais velho é o {nomevelho}, com {maioridade} de idade')
print(f'Tem um total de {mulher20} mulheres com menos de 20 anos.')