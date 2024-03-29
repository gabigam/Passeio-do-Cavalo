﻿# Passeio-do-Cavalo
Algoritmo para Passeios do Cavalo em um Tabuleiro de Xadrez 8x8

Este repositório contém uma implementação em Python do algoritmo para encontrar os passeios do cavalo em um tabuleiro de xadrez 8x8. O programa utiliza backtracking para explorar recursivamente todas as possíveis posições do cavalo.

Funcionamento:

O programa começa na posição inicial do cavalo e explora recursivamente todos os 8 movimentos possíveis para verificar se levam à solução ou não. Se o caminho atual não chegar ao destino ou já tiver explorado todos os movimentos possíveis a partir da posição atual, é feito um backtracking (ou seja, um retrocesso).

Detalhes do Programa:

    linha e coluna: Representam os movimentos possíveis do cavalo no tabuleiro de xadrez.
    checa_validade(x, y): Função para verificar se as coordenadas (x, y) são válidas no tabuleiro de xadrez.
    passeio_cavalo(posicao_visitada, x, y, posicao): Função recursiva para realizar o passeio do cavalo usando backtracking.

Implementação:

O código é composto por uma função principal main() que define o tamanho do tabuleiro de xadrez (8x8) e inicia o passeio do cavalo a partir da posição (0, 0).

Exemplo de Uso:

O código imprime todos os passeios do cavalo no tabuleiro de xadrez 8x8.

Execução:

Para executar o código, basta rodar o arquivo Python. Os resultados dos passeios do cavalo serão impressos no terminal.
