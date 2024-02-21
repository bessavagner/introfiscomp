# Exercícios propostos

## 1. Área do triângulo

Escreva um algoritmo para calcular a área de um triângulo. A altura e a base são fornecidas pelo usuário.

## 2. Aceleração

Considere <code>m</code> e <code>a</code> (massa e aceleração de um corpo, respectivamente) os valores de entrada de um programa. Escreva um algorítimo em pseudocódigo para calcular a força resultante. <code>m</code> e <code>a</code> são fornecidos pelo usuário

## 3. Ângulo de um vetor

Escreva um programa o qual, dadas as componentes <code>x</code> e <code>y</code> de um vetor, calcula o ângulo do vetor com o eixo x.

## 4. Tensão máxima

A tensão máxima que um certo cabo de aço consegue suportar é <code>20000 N</code>. Escreva um algorítimo em pseudocódigo para determinar se este cabo consegue suportar o peso de um certo corpo de massa. Use a gravidade como 9,8 m/s². Seu programa deve escrever "suporta" caso o cabo suporte; e "não suporta" caso o cabo não suporte

## 5. Derivada

Escreva um algorítimo em pseudocódigo para calcular a derivada da função <math display="inline"><msup><mi>2</mi><mn>-x</mn></msup>cos(x)</math>, dado o valor de x, o ponto onde se calcula a derivada. Use a definição da derivada como um limite e escolha a variação (<math display="inline">&Delta; x</math>) como uma variável de escopo global.


## 6. Força resultante

Dados dois vetores em forma de lista, os quais representam forças que atuam sobre uma partícula, escreva um programa que determina a força resultante em forma de uma lista e calcula seu módulo.

```
forca_1 = [0, 2]
forca_1 = [1, -1]
```

## 7. Acadêmico

Uma sala de aula possui N alunos. A nota de cada aluno é armazenada em um dicionário. Escreva um código que calcula: 1. a média das notas de cada estudante; 2. a média das médias da turma e 3. o número de alunos com nota acima da média 7. Segue o dicionário:

```
turma_1 = {
    'Fulano': [5, 7.5, 8],
    'Beltrana': [10, 8.5, 10],
    'João Ninguém': [45, 3.5, 6],
    'Maria Vai Com As OUtras': [6, 7.5, 3]
}
```

## 8. Gestão de produtos

Um fabricante de automóveis possui um dicionário com os modelos de carros produzidos e suas respectivas quantidades. Escreva um programa que: 1. calcula a quantidade total de carros produzidos e 2. escreve o modelo mais produzido.

```
carros = {
    "Celta": 200,
    "Gol": 300,
    "Fiesta": 150,
    "Uno": 250,
    "Palio": 280
}
```
## 9. Gestão de vendas

Uma loja de roupas possui um dicionário com os itens vendidos e seus respectivos preços. Escreva um programa que calcula o valor total das compras de um cliente com base em uma lista de itens comprados.

```
produtos = {
    "banana": 1.50,
    "maçã": 2.00,
    "laranja": 3.00,
    "uva": 2.50,
    "pera": 3.50
}

compras = ["banana", "maçã", "uva"]
```

## 10. Biblioteca

Uma pessoa possui uma coleção de livros em forma de um dicionário, com o nome do autor como chave e seus respectivos livros como valores. Escreva um programa que exibe o número total de livros, dado um autor, e a lista de livros desse mesmo autor.

```
livros = {
    "Fulano": ["Livro 1", "Livro 2", "Livro 3"],
    "Beltrana": ["Livro 4", "Livro 5", "Livro 6"],
    "João Ninguém": ["Livro 7", "Livro 8"],
    "Maria Joaquina": ["Livro 9", "Livro 10"]
}
```
