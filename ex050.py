# Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for impar, desconsidere-o.

soma = 0
count = 0

for contagem in range(0,6):
        num = int(input('Digite o numero: '))
        if (num%2)==0:
            soma += num
            count += 1
print(f'Soma: {soma}\nContagem: {count}')