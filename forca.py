import random  # Importando biblioteca para escolher uma palavra aleatoria dentro do arquivo txt

# tabuleiro é uma lista criada para armazenar o tabuleiro (o dezenho da forca)
tabuleiro = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Definindo uma class pra armazenar metodos para aplicar no jogo

class Forca():
    def __init__(self, word):
        self.word = word  # Atributo da palavra
        self.errada = []  # Atributo para armazenar as letras errada
        self.certa = []  # Atributo para armazenar as letras certas

    def achar_(self, letra):  # metodo que vai checar se a letra chutada pelo usuário é certa ou não

        if (letra in self.word and letra not in self.certa):  # Se a letra é encontrada no atributo word e não encotrada

            self.certa.append(letra)  # no atributo certa, adiciona a letra na lista certa

        elif letra not in self.word and letra not in self.errada:  # Se a letra não está no atributo word e não encontrada

            self.errada.append(letra)  # no atributo errada, adiciona a letra na lista errada

        else:  # caso contrário vai retornar Falso, pois se não causaria problemas de logica no jogo
            return False

        return True  # No geral, o metodo achar, vai retornar True

    def final_(self):  # Metodo final, definido para checar se o jogo acabou

        return self.vitoria_() or (
                    len(self.errada) == 6)  # Retorna o estado do metodo vitoria ou o tamanho da lista criada pelo atributo errada
        # Então o metodo final grava o estado e é usado para checar o fim do game

    def vitoria_(self):  # Metodo vitoria, definido para checar se os requisitos de vitoria foram atendidos

        if '_' not in self.esconder_():  # Se '_' não está no metodo esconder, quer dizer que as letras certas foram encontrar
            return True  # Retorna o valor booleano True se a condição for atendida
        return False  # Retorna False no geral, para que o jogo continue

    def esconder_(self):  # Metodo esconder, definido para esconder as letras da palavra escondida
        rtn = ''
        for letra in self.word:  # Para a letra no atributo word, vai rodar o if, e se a letra não esta no atributo certa

            if letra not in self.certa:  # vai retornar '_', escondendo as letras
                rtn += '_'

            else:  # Mas caso o contrario, a letra vai sendo revelada quando acertada
                rtn += letra
        return rtn  # Retorna o estado da variavel rtn, escolhida para armazenar '_'

    def status_(self):  # Metodo status, definido para mostrar o estado do jogo

        print(tabuleiro[
                  len(self.errada)])  # Vai mostrar o tabuleiro conforme o tamanho do atributo errada, responsavel por ir desenhando o bonequinho na forca

        print(
            '\nPalavra: ' + self.esconder_())  # Vai mostrar A palavra escolhida, só que enquanto não ouver letras certas vai mostrar somente '_'

        print('\nLetras erradas: ', )  # Vai mostrar todas as letras erradas até o momento

        for letra in self.errada:  # Para a letra no atributo errada, a letra será mostrada
            print(letra, )
        print()

        print('Letras corretas: ', )  # Vai mostrar as letras acertadas

        for letra in self.certa:  # Para a letra no atributo certa, vai mostrar as letras acertadas
            print(letra, )
        print()


def random_word():  # Função defida fora da classe, essa função vai escolher de forma aleatoria a palavra dentro do arquivo txt

    with open("palavras.txt", "rt") as f:  # Abrindo o arquivo txt para leitura

        bank = f.readlines()  # lendo o arquivo e armazenando os dados

    return bank[random.randint(0,
                               len(bank))].strip()  # Retorna uma palavra aleatoria, strip() serve para separar por espaços ou por algum caracter especifico


def main():  # Função para rodar o game

    game = Forca(random_word())  # Criando o objeto game dentro da class Forca para usar seus metodos no objeto

    while not game.final_():  # Enquanto o game não acabar o programa vai rodar os seguintes metodos para o objeto game

        game.status_()  # Pedindo o status do jogo, então tudo que foi definido dentro do metodo status sera atribuido para o objeto game

        user_input = input("\nDigite uma letra: ")  # Pede para o usuario digitar uma letra

        game.achar_(
            user_input)  # Com o input do usuario, chamamos o metodo achar para checar se esse input está certo ou não

    game.status_()  # Depois de rodar vai checar o status do game novamente

    if game.vitoria_():  # E se a condição de vitoria for satisfeita, o while acima ira parar por que o metodo vitoria ira retornar True

        print("\nPARABENS VOCÊ GANHOU!!")  # E será impresso a mensagem de vitoria

        print("\nA palavra certa: " + game.word)  # Mostra a palavra completa

    else:  # Caso contrario será game over
        print("\nGAME OVER!!!")

        print("\nA palavra certa: " + game.word)


if __name__ == "__main__":  # O conteudo dentro dessa estrutura só vai rodar quando você iniciar o programa
    main()
