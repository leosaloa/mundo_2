# Refaça o DESAFIO 051, lendo o primeiro termo e a razao de uma PA, 
# mostrando os 10 primeiros termos da progressão usando a estrurura while.

termo_inicial = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 0

while cont < 10:
    termo = termo_inicial + (cont * razao)
    cont += 1
    print(termo, end = ' > ')
print('Acabou')