print('********************************')
print('Bem vindo ao jogo da Adivinhação')
print('********************************')

numero_secreto = 42

numero_selecionado = input('Digite o seu número: ')
numero_selecionado = int(numero_selecionado)

acertou = numero_secreto == numero_selecionado
maior   = numero_selecionado > numero_secreto
menor   = numero_secreto > numero_selecionado

if(acertou):
    print('Você acertou !')
else:
    if(maior):
        print('Você errou ! O número selecionado era',
              numero_selecionado - numero_secreto, 'números menores.')
    if(menor):
        print('Você errou ! O número selecionado era',
              numero_secreto - numero_selecionado,'números maiores.')

print('Seu número escolhido foi:', numero_selecionado)

print('Fim do jogo')
