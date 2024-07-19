# Faça um programa que mostre a TABUADA de VARIOS NUMEROS, um de cada vez, para cada valor 
# digitado pelo usuario. O programa será INTERROMPIDO quando o numero solicitado for NEGATIVO.

while True:
    cont = soma = 0
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*20)
    if num < 0:
        break
    else:
        pass
    for cont in range(10):
        cont += 1
        soma += num
        print(f'{num} x {cont:>2} = {soma}', end = '\n')
    print('-'*20)
print('Fim do programa')