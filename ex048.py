# Faça um programa que calcule a soma entre todos os numeros impares que são multiplos de tres e que se encontram no intervalo de 1 até 500.
# Multiplos de tres resto = 0

soma = 0
count = 0

for contagem in range (1, 501, 2):
    if (contagem%3) == 0:
        soma += contagem
        count += 1
print(f'Soma: {soma}\nContagem: {count}')