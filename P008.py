import random
pedra = 'pedra' 
papel = 'papel' 
tesoura = 'tesoura'

lista = pedra, papel, tesoura

voce = str(input('\033[1;33Digite a sua jogada: ')).upper()
oponente = random.choice(lista).upper()

print(f'Seu oponente escolheu: {oponente}')         

if voce == pedra and oponente == tesoura:
    print('Você ganhou!!')

elif voce == tesoura and oponente == pedra:
    print('Você ganhou!!')

elif voce == papel and oponente == pedra:
    print('Você venceu!!')

elif voce == oponente:
    print('Você empatou!!')

else:
    print('Você perdeu!!')