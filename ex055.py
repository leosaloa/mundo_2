# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

cont = 0
peso = []

for contagem in range(1, 6):
    cont += 1
    peso.append(float(input(f'\nDigite o peso da {cont}ª pessoa: ')))
peso.sort()
print(f'\nMenor peso {peso[0]} kg.\nMaior peso {peso[-1]} kg')