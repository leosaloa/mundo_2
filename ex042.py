# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

num1 = float(input('\nDigite o primeiro comprimento: '))
num2 = float(input('\nDigite o segundo comprimento: '))
num3 = float(input('\nDigite o terceiro comprimento: '))
regra = (num1 + num2) > num3 and (num2 + num3) > num1 and (num1 + num3) > num2
equ = num1 == num2 == num3
iso = num1 == num2 or num1 == num3 or num2 == num3
esc = num1 != num2 != num3

if  regra and equ:
    print('\nPode formar um triângulo Equilátero.')
elif regra and iso:
    print('\nPode formar um triângulo Isósceles.')
elif regra and esc:
    print('\nPode formar um triangulo Escaleno.')
else:
    print('\nNão pode formar um triângulo.')