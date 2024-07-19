# Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuario digitar o valor 999,
# que é a condição de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles(Desconsiderando o 999)

cont = 0
soma = 0
numero = 0
numero = int(input('Digite um numero [999 para parar]: '))

while numero != 999:
    cont += 1
    soma += numero
    numero = int(input('Digite um numero [999 para parar]: '))
print(f'\nVocê digitou {cont} numeros.\nA soma entre eles é {soma}')