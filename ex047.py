# Crie um programa que mostre na tela todos os numeros pares que estão no intervalo entre 1 e 50.
# Usar o resto(%) para verificar se é par ou impar, numero par = 0, impar = 1

for contagem in range(1,51):
    if (contagem % 2) == 0:
        print(contagem, end = ' ')