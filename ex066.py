# Crie um programa que leia VARIOS NUMEROS inteiros pelo teclado. O programa só vai parar quando o
# usuario digitar o valor 999, que é a CONDIÇÃO DE PARADA. No final, mostre QUANTOS NUMEROS foram
# digitados e qual foi a SOMA entre eles (desconsiderando o flag (999))

cont = 0
soma = 0

while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    else:
        pass
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}!')