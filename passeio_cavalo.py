# Algoritmo que encontra os passeios do cavalo em um tabuleiro de xadrez 8x8
# O programa usa backtracking
# Começando na posição inicial
# Explora recursivamente todos os 8 movimentos possíveis para verificar se levam a solução ou não
# Se o caminho atual não chegar ao destino ou já explorou todos os movimentos possíveis a partir da posição atual,
# é feito um backtracking(ou seja um retrocesso)


# todos os oito movimentos possíveis para o cavalo
linha = [2, 1, -1, -2, -2, -1, 1, 2] # numero positivo significa movimento para direita e negativo movimento para esquerda
coluna = [1, 2, 2, 1, -1, -2, -2, -1] # numero positivo significa movimento para cima e negativo movimento para baixo


# Verifica se `(x, y)` são coordenadas válidas do tabuleiro de xadrez
def checa_validade(x, y):
    return not (x < 0 or y < 0 or x >= N or y >= N)


# Função recursiva para realizar o passeio do cavalo usando backtraking(retrocesso)
def passeio_cavalo(posicao_visitada, x, y, posicao):
    # marca a posicao atual como visitada
    posicao_visitada[x][y] = posicao

    # se todos as posicoes já tiverem sido visitadas, imprime a solução
    if posicao >= N * N:
        for s in posicao_visitada:
            print(s)
        print()

        # recua antes de retornar
        posicao_visitada[x][y] = 0
        return

    # verifica todos os oito movimentos possíveis para o cavalo
    # e recua para cada movimento válido
    for c in range(8):

        # obtem a nova posição do cavalo a partir da posição atual dele no tabuleiro de xadrez
        nova_linha = x + linha[c]
        nova_coluna = y + coluna[c]

        # verifica se a posição nova é válida e se ainda não foi visitada
        if checa_validade(nova_linha, nova_coluna) and posicao_visitada[nova_linha][nova_coluna] == 0:
            passeio_cavalo(posicao_visitada, nova_linha, nova_coluna, posicao + 1)

    # recua da posicao atual e remove ela do caminho atual
    posicao_visitada[x][y] = 0


if __name__ == '__main__':
    # tabuleiro de xadrez "NxN"
    N = 8
    print("Tabuleiro criado com sucesso!")
    print("Os passeios do cavalo são:")
    # "posicao_visitada":
    # serve para manter o controle das casas envolvidas no passeio do cavalo
    # e armazenar a ordem em que as posições são visitadas
    posicao_visitada = [[0 for x in range(N)] for y in range(N)]
    posicao = 1
    # começa o passeio do cavalo a partir da posicao `(0, 0)`
    passeio_cavalo(posicao_visitada, 0, 0, posicao)
