# Faça um programa que leia um numero qualquer e mostre o seu fatorial.
# Ex: 5! = 5x4x3x2x1 = 120


num = int(input('Digite um numero para mostrar o seu fatorial: '))
fatorial = num

print(f'{num}! = ', end = '')
while num > 1:
    print(f'{num}', end = 'x')
    num -= 1
    fatorial = fatorial * num
print(f'1 = {fatorial}')
print('\nFim do programa')