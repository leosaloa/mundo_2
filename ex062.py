# Melhore o DESAFIO 061, perguntando para o usuario se ele quer mostrar mais alguns termos. 
# O programa encerra quando ele disser que quer mostrar 0 termos

escolha = ''

while escolha != 'N':
    cont = 0
    termo_inicial = int(input('Digite o primeiro termo: '))
    razao = int(input('Digite a razão: '))
    while cont < 10:
        termo = termo_inicial + (cont * razao)
        cont += 1
        print(termo, end = ' > ')
    print('Acabou')
    escolha = str(input('Deseja continuar?[S/N] ')).upper()
print('Fim do programa')

# escolha = 1

# while escolha != 0:
#     cont = 0
#     termo_inicial = int(input('Digite o primeiro termo: '))
#     razao = int(input('Digite a razão: '))
#     while cont < 10:
#         termo = termo_inicial + (cont * razao)
#         cont += 1
#         print(termo, end = ' > ')
#     print('Acabou')
#     escolha = int(input('Digite 0 para parar o programa e 1 para continuar '))
# print('Fim do programa')