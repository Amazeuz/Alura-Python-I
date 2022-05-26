print('********************************')
print('Bem vindo ao jogo da Adivinhação')
print('********************************')

from random import randint

numero_secreto = randint(1, 100)
print(numero_secreto)
total_de_tentativas = 3



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
        print('Você acertou !')
        break
    else:
        if(maior):
            print('Você errou ! O número sorteado é menor')
        if(menor):
            print('Você errou ! O número sorteado é maior')

    total_de_tentativas = total_de_tentativas - 1


print('Fim do jogo !')
print('O número sorteado era', numero_secreto)
