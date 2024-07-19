# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
# peça a digitação novamente até ter um valor correto.

sexo = ''

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o seu sexo [M/F]: ')).upper()
    print('Digite novamente o valor, só aceitamos M ou F.')

if sexo == 'M':
    print('\nVocê é do sexo Masculino.')
elif sexo == 'F':
    print('\nVocê é do sexo Feminino.')
else:
    print('Algo deu errado.')