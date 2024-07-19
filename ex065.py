# Crie um programa que leia varios numeros inteiros pelo teclado. No final da execução, mostre a media entre todos os valores
# e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuario se ele quer ou não continuar a digitar valores.

parar = ''
cont = 0
soma = 0
valor = []

while parar != 'S':
    num = int(input('Digite o valor: '))
    cont += 1
    soma += num
    parar = str(input('Deseja sair do programa? [S]/[N]')).upper().strip()
    valor.append(num)
    valor.sort()
print(f'Media {soma/cont}\nMaior {valor[-1]}\nMenor {valor[0]}')