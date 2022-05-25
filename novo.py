print('********************************')
print('Bem vindo ao jogo da Adivinhação')
print('********************************')

numero_secreto = 42

numero_selecionado = input('Digite o seu número: ')

numero_selecionado = int(numero_selecionado)

if(numero_selecionado == numero_secreto):
    print('Você acertou !')
else:
    print('Você errou !')

print('Seu número escolhido foi:', numero_selecionado)

print('Fim do jogo')