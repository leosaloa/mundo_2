# Crie um programa que leia a IDADE e o SEXO de VARIAS PESSOAS. A cada pessoa cadastrada,
# o programa devera perguntar se o USUARIO quer ou não continuar. No final, mostre:
# A) Quantas pessoas tem mais de 18 ANOS.
# B) Quantos HOMENS foram cadastrados.
# C) Quantas MULHERES tem menos de 20 ANOS.

cont = 0
cont_maior = 0
cont_masc = 0
cont_fem_20 = 0

while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)

    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper()
    print('-' * 20)
    cont += 1
    continuar = str(input('Quer continuar? [S/N] ')).upper()
    if idade > 18:
        cont_maior += 1
    if sexo == 'M':
        cont_masc += 1
    if sexo == 'F' and idade < 20:
        cont_fem_20 += 1
    else:
        pass
    if continuar == 'N':
        print('Break')
        break
print(f'Tem {cont_maior} pessoas maiores de 18 anos')
print(f'Tem {cont_masc} homens cadastrados')
print(f'Tem {cont_fem_20} mulheres com menos de 20 anos')