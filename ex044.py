# Elabora um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# 1- À vista dinheiro/cheque: 10% de desconto
# 2- À vista no cartão: 5% de desconto
# 3- Em até 2x no cartão: preço normal
# 4- 3x ou mais no cartão: 20% de juros

vl_produto = float(input('\nDigite o valor do produto: '))
print('\nEscolha a forma de pagamento:')
ds_pagamento = int(input('\n1 - À Vista (Dinheiro)\n2 - À Vista no cartão\n3 - 2x no cartão\n4 - 3x ou mais no cartão\n\nOpção: '))
parcelas = int(input('\nQuantas parcelas? '))
desc_dinheiro = vl_produto * 0.1 # Desconto DINHEIRO
desc_cartao = vl_produto * 0.05 # Desconto CARTÃO
juros = vl_produto * 0.2 # JUROS

if ds_pagamento == 1:
    print(f'\nValor total R$ {vl_produto-desc_dinheiro:.2f}.\nValor produto R$ {vl_produto:.2f}.\nDesconto R$ {desc_dinheiro:.2f}')
elif ds_pagamento == 2:
    print(f'\nValor total R$ {vl_produto-desc_cartao:.2f}.\nValor produto R$ {vl_produto:.2f}.\nDesconto R$ {desc_cartao:.2f}')
elif ds_pagamento == 3:
    print(f'\nValor total R$ {vl_produto:.2f}.')
elif ds_pagamento == 4:
    print(f'\nSua compra será parcelada em {parcelas}x COM JUROS de R$ {(vl_produto+juros)/parcelas:.2f}\nValor total R$ {vl_produto+juros:.2f}.')
else:
    print('Algo deu errado!')