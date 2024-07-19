# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pause de 1 segundo entre eles.

from time import sleep
from PIL import Image

image = Image.open('.\\mundo_2\\desafios\\feitos\\fogos.png')

print('\n')
for contagem in range(10, -1, -1):
    print(contagem)
    sleep(1)
print('\n')

image.show()
