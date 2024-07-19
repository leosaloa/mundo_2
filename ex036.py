# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O prograva vai perguntar o VALOR DA CASA,
# o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

vl_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do seu salário: '))
anos = int(input('Digite em quantos anos pretende pagar a casa: '))

parcela = vl_casa / (anos * 12)

if parcela < salario * 0.3:
    print(f'Empréstimo APROVADO!\nValor das parcelas R$ {parcela:.2f}\nQuantidade de parcelas {anos * 12}')
else:
    print('Empréstimo NEGADO!')