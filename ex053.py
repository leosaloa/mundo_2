# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
# Exemplo: Apos a sopa      A sacada da casa        A torre da derrota      O lobo ama o bolo       Anotaram a data da maratona

from colorama import init, Fore, deinit

init() # Iniciar biblioteca colorama
print('\n\bVerificar se a palavra é um palindromo.')
frase = str(input('\nDigite a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
invertido = ''

for letra in range(len(junto) - 1, - 1, - 1):
    invertido += junto[letra]
if junto == invertido:
    print(f'\nVocê escreveu: {frase}')
    print('\nA frase é um',  'palindromo:', Fore.CYAN, invertido, Fore.RESET)
else:
    print(f'\nVocê escreveu: \n{frase}')
    print('\nEssa frase não é um', Fore.RED, 'palindromo.', Fore.RESET)

deinit() # Finalizar biblioteca colorama