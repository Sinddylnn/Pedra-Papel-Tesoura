import time
while True:
       from random import randint
       from time import sleep
       itens = ('Pedra', 'Papel', 'Tesoura')
       computador = randint (0, 2)
       print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
       print('')
       jogador = int(input('Qual é a sua jogada? '))
       print('PEDRA')
       sleep(0.5)
       print('PAPEL')
       sleep(0.5)
       print('TESOURA!!!')
       print('-' * 24)
       print('jogador jogou {}'.format(itens[jogador]))
       print('Computador jogou {}'.format(itens[computador]))
       print('-' * 24)
       if computador == 0: # Computador jogou PEDRA
              if jogador == 0:
                     print('EMPATE')
              elif jogador == 1:
                     print('JOGADOR VENCE')
              elif jogador == 2:
                     print('COMPUTADOR VENCE')
              else:
                     print('JOGADA INVÁLIDA')
       elif computador == 1: # Computador jogou PAPEL
              if jogador == 0:
                     print('COMPUTADOR VENCE')
              elif jogador == 1:
                     print('EMPATE')
              elif jogador == 2:
                     print('JOGADOR VENCE')
              else:
                     print('JOGADA INVÁLIDA')
       elif computador == 2: # Computador jogou TESOURA
              if jogador == 0:
                     print('JOGADOR VENCE')
              elif jogador == 1:
                     print('COMPUTADOR VENCE')
              elif jogador == 2:
                     print('EMPATE')
              else:
                     print('JOGADA INVÁLIDA')

time.sleep(5)
