# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 - Para binário      2 - Para octal      3 - para hexadecimal

from colorama import init, Fore, deinit

init() # Iniciar cores
num = int(input('Digite o numero inteiro a ser convertido: '))
conversor = int(input('\n1 - Binário\n2 - Octal\n3 - Hexadecimal\n\nEscolha alguma das opções: '))

if conversor == 1:
    print(f'\nA conversão do numero', Fore.GREEN, f'{num}', Fore.RESET,'para Binário é', Fore.CYAN, f'{bin(num)}')
elif conversor == 2:
    print(f'\nA conversão do numero', Fore.GREEN, f'{num}', Fore.RESET,' para Octal é', Fore.CYAN, f'{oct(num)}')
elif conversor == 3:
    print(f'\nA conversão do numero', Fore.GREEN, f'{num}', Fore.RESET,' para Hexadecimal é', Fore.CYAN, f'{hex(num)}')
else:
    print('Numero incorreto digite novamente!')

deinit() # Parar cores