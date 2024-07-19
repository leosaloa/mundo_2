# Escreva um programa que leia um nuemro N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequencia de Fibonacci.
# 0 → 1 → 1 → 2 → 3 → 5 → 8

numero = int(input('Digite quantos temos voce quer mostar: '))

t1 = 0
t2 = 1
cont = 3

print(f'{t1} > {t2}', end = '')
while cont <= numero:
    t3 = t1 + t2
    print(f' > {t3}', end = '')
    t1 = t2
    t2 = t3
    cont += 1
print(' > FIM')
