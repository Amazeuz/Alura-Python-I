print('********************************')
print('Bem vindo ao jogo da Adivinhação')
print('********************************')

numero_secreto = 42

total_de_tentativas = 3
rodada = 1

while(total_de_tentativas > 0):

    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    numero_selecionado = input('Digite o seu número: ')
    numero_selecionado = int(numero_selecionado)
    print('Seu número escolhido foi:', numero_selecionado)

    acertou = numero_secreto == numero_selecionado
    maior = numero_selecionado > numero_secreto
    menor = numero_secreto > numero_selecionado

    if(acertou):
        print('Você acertou !')
    else:
        if(maior):
            print('Você errou ! O número selecionado é menor')
        if(menor):
            print('Você errou ! O número selecionado é maior')
        
    total_de_tentativas = total_de_tentativas - 1
    rodada = rodada + 1


print('Fim do jogo !')
print('O número sorteado era',numero_secreto)
