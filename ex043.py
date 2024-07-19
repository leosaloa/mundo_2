# Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

peso = float(input('\nDigite o seu peso: '))
altura = float(input('\nDigite a sua altura: '))

imc = (peso / altura) / altura

if imc < 18.5:
    print(f'\nVocê esta abaixo do peso.\nIMC: {imc:.2f}')
elif imc <= 25:
    print(f'\nVocê esta com peso ideal.\nIMC: {imc:.2f}')
elif imc <= 30:
    print(f'\nVocê esta sobrepeso.\nIMC: {imc:.2f}')
elif imc <= 40:
    print(f'\nVocê esta com obesidade.\nIMC: {imc:.2f}')
elif imc > 40:
    print(f'\nVocê esta com obesidade morbida.\nIMC: {imc:.2f}')
else:
    print(f'\nVerifique novamente o peso ou a altura.\nIMC: {imc:.2f}')