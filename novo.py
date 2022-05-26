print('********************************')
print('Bem vindo ao jogo da Adivinhação')
print('********************************')

from random import randint
from timeit import repeat

numero_secreto = randint(1, 100)
#print(numero_secreto)
total_de_tentativas = 3
pontos = 1000

print('Qual o nível de dificuldade ?')
print('(1) Fácil (2) Médio (3) Difícil')

nivel = int(input('Selecione o nível: '))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
elif(nivel == 3):
    total_de_tentativas = 5
else:
    print('Digite um número válido')
    exit()

for rodada in range(1, total_de_tentativas + 1):

    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    numero_selecionado = input('Digite o seu número: ')
    numero_selecionado = int(numero_selecionado)

    if(numero_selecionado < 1 or numero_selecionado > 100):
        print('Digite um número entre 0 e 100')
        continue

    acertou = numero_secreto == numero_selecionado
    maior = numero_selecionado > numero_secreto
    menor = numero_secreto > numero_selecionado

    if(acertou):
        print('Você acertou e fez {} pontos!' .format(pontos))
        break
    else:
        if(maior):
            print('Você errou ! O número sorteado é menor')
        if(menor):
            print('Você errou ! O número sorteado é maior')
        pontos_perdidos = abs(numero_secreto - numero_selecionado)
        pontos = pontos - pontos_perdidos

print('Fim do jogo !')
print('O número sorteado era', numero_secreto)
print('Você possúi {} pontos!' .format(pontos))
