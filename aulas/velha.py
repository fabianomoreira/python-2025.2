import random

class Velha():
    def __init__(self):
        # lista
        self.tabuleiro = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    # desenho do tabuleiro
    def desenharTabuleiro(self):
        print(' ' + self.tabuleiro[0][0] + ' | ' + self.tabuleiro[0][1] + ' | ' + self.tabuleiro[0][2])
        print('-----------')
        print(' ' + self.tabuleiro[1][0] + ' | ' + self.tabuleiro[1][1] + ' | ' + self.tabuleiro[1][2])
        print('-----------')
        print(' ' + self.tabuleiro[2][0] + ' | ' + self.tabuleiro[2][1] + ' | ' + self.tabuleiro[2][2])

    def jogarMaquina(self):
        return random.randint(0, 2)