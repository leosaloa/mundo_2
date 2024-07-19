# Crie um programa que simule o funcionamento de um CAIXA ELETROINCO. No inicio, pergunte
# ao usuario qual sera o VALOR A SER SACADO (numero inteiro) e o progrmaa vai informar
# quantas CEDULAS de cada valor serão entregues.
# OBS: Considere que o caixa possui cedulas de R$ 50, R$ 20, R$ 10 e R$ 1

n50 = 0
n20 = 0
n10 = 0
n1 = 0


while True:
    valor = int(input('Digite o valor para saque: R$ '))
    if valor // 50:
        n50 = valor // 50
        print(f'{n50} notas de 50')
    if valor % 50 >= 20:
        n20 = (valor - (50 * n50)) // 20
        print(f'{n20} notas de 20')
    if valor % 20 >= 10:
        n10 = (valor - (50 * n50) - (20 * n20)) // 10
        print(f'{n10} notas de 10')
    if valor % 10 >= 1:
        n1 = valor - (50 * n50) - (20 * n20) - (10 * n10)
        print(f'{n1} notas de 1')
    cance = str(input('Deseja fazer mais saques? [S/N] ')).upper()
    if cance == 'N':
        break
print(f'Fim do programa')
