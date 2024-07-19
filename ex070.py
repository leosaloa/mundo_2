# Crie um programa que leia o NOME e o PREÇO de VARIOS PRODUTOS. O programa devera perguntar
# se o USUARIO vai continuar. No final, mostre:
# A) Qual é o TOTAL GASTO na compra.
# B) Quantos produtos custam MAIS de R$ 10000.
# C) Qual o NOME do produto mais BARATO.

lista_prod = []
vl_prod = []
cont = 0
soma = 0


while True:
    produto = str(input('Digite o nome do produto: '))
    lista_prod.append(produto)
    print(f'Produto: {produto}')
    preco = int(input('Digite o valor do produto: R$ '))
    vl_prod.append(preco)
    print(f'\nPreço: {preco}')
    continuar = str(input('Deseja continuar? [S/N]')).upper()
    soma += preco
    print(f'\nSoma: {soma}')
    if preco > 10000:
        cont += 1
        print(cont)
    if continuar != 'N' or continuar != 'S':
        print('Digite algo!')
    if continuar == 'N':
        break
    else:
        pass
menor_valor = min(vl_prod)
i_menor_valor = vl_prod.index(menor_valor)
ds_produto = lista_prod[i_menor_valor]
# print(f'Menor valor: R$ {menor_valor}\nO produto é o {ds_produto} \nO index é {i_menor_valor}')
print(f'Valor total de gasto R$ {soma:.2f}\nComprou {cont} produtos com valor acima de R$ 10.000,00')
print(f'O produto mais barato é o {menor_valor}')

# A) Qual é o TOTAL GASTO na compra.
# B) Quantos produtos custam MAIS de R$ 10000.
# C) Qual o NOME do produto mais BARATO.