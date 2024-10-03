# Passeio do Cavalo ♞

Este repositório contém uma implementação em Python do algoritmo para encontrar os passeios do cavalo em um tabuleiro de xadrez 8x8. O programa utiliza backtracking para explorar recursivamente todas as possíveis posições do cavalo.

## 📁 Estrutura do Projeto

O código é composto pelo arquivo principal:

- **passeio_cavalo.py**: Implementação do algoritmo de passeios do cavalo, incluindo a lógica de validação e backtracking.

## Funcionamento

O programa começa na posição inicial do cavalo e explora recursivamente todos os 8 movimentos possíveis para verificar se levam à solução. Se o caminho atual não chegar ao destino ou já tiver explorado todos os movimentos possíveis a partir da posição atual, é feito um backtracking.

### Detalhes do Programa

- **linha e coluna**: Representam os movimentos possíveis do cavalo no tabuleiro de xadrez.
- **checa_validade(x, y)**: Função para verificar se as coordenadas (x, y) são válidas no tabuleiro de xadrez.
- **passeio_cavalo(posicao_visitada, x, y, posicao)**: Função recursiva para realizar o passeio do cavalo usando backtracking.

## 🚀 Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/gabigam/Passeio-do-Cavalo.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd Passeio-do-Cavalo
   ```
3. Execute o arquivo Python:
   ```bash
   python passeio_cavalo.py
   ```

Os resultados dos passeios do cavalo serão impressos no terminal.
```

