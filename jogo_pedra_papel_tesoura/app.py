from jogo_ppt import Jogo

game = Jogo()

game.jogador_1 = input('Jogador 1: Pedra, Papel ou Tesoura ?')
game.jogador_2 = input('Jogador 2: Pedra, Papel ou Tesoura ?')

game.jogo_ppt(game.jogador_1, game.jogador_2)