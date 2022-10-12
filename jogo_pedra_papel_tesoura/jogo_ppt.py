class Jogo:

  def __init__(self):
    self.jogador_1 = ''
    self.jogador_2 = ''

  def jogo_ppt(self, jogada1, jogada2):
    self.jogador_1 = jogada1
    self.jogador_2 = jogada2

    if jogada1 == 'papel' and jogada2 == 'pedra':
      print('Jogador 1 ganhou')
    elif jogada1 == 'pedra' and jogada2 == 'tesoura':
      print('Jogador 1 ganhou')
    elif jogada1 == 'tesoura' and jogada2 == 'papel':
      print('Jogador 1 ganhou')
    elif jogada1 == 'pedra' and jogada2 == 'papel':
      print('Jogador 2 ganhou')
    elif jogada1 == 'tesoura' and jogada2 == 'pedra':
      print('Jogador 2 ganhou')
    elif jogada1 == 'papel' and jogada2 == 'tesoura':
      print('Jogador 2 ganhou')
    else:
      print('Empate!')
    
    
