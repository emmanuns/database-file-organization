# Banca de Testes de Organizações Primárias de Arquivos de Registros em SBD

## Descrição do Projeto
O projeto consiste em desenvolver uma banca de teste para a comparação do desempenho entre um conjunto de métodos de acesso para os três tipos de organizações primárias de "arquivos de registros" (file of records), comumente usadas por SGBD relacionais.

O objetivo é avaliar e comparar o desempenho dessas organizações primárias de arquivos em termos de:
- O total de blocos de memória utilizados.
- A quantidade de blocos acessados para cada método de acesso.

## Funcionalidades Implementadas
Os seguintes métodos de acesso foram desenvolvidos para testar a eficiência das organizações de arquivos de registros:

### Métodos de Inserção (INSERT)
- Inserção de um único registro.
- Inserção de um conjunto de registros.

### Métodos de Seleção (SELECT)
- Seleção de um único registro pela chave primária.
- Seleção de registros cujas chaves primárias pertencem a um conjunto de valores.
- Seleção de registros por uma faixa de valores de um campo chave.
- Seleção de registros por campo não chave igual a um valor dado.

### Métodos de Remoção (DELETE)
- Remoção de um único registro selecionado através da chave primária.
- Remoção de um conjunto de registros selecionados por algum critério.


## Organizações de Arquivos de Registros
Os métodos foram implementados para as seguintes organizações primárias de arquivos:

1. **Heap (Tamanho Fixo)**: Arquivo sequencial sem qualquer ordenação, com registros de tamanho fixo e lista encadeada para registros deletados. A inserção é feita no final ou aproveitando o primeiro espaço livre.

2. **Heap (Tamanho Variável)**: Similar ao heap de tamanho fixo, porém com registros de tamanhos variáveis. Os registros deletados são marcados e um processo de compressão do arquivo é implementado.

3. **Arquivo Ordenado**: Arquivo ordenado por um campo específico, com registros de tamanho fixo. Inserção é feita em um arquivo de extensão com posterior reordenação entre o arquivo principal e sua extensão.

4. **Hash Externo Estático**: Utiliza uma função de hashing para distribuir registros, com tratamento de colisão através de listas em buckets de overflow.

## Estrutura do Projeto

- `src/`: Contém os códigos-fonte dos métodos de acesso e organizações de arquivos.
- `data/`: Inclui os arquivos de dados usados para teste e exemplos.
