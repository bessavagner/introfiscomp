# Exercícios Resolvidos

## 1. Cálculo de distância

Escreva um algoritmo para calcular a distância entre dois pontos no espaço bidimensional. Os pontos são representados por suas coordenadas _(x1, y1)_ e _(x2, y2)_.

### Solução


```
// Pseudocódigo para calcular a distância entre dois pontos
Programa distancia
Função distanciaEntrePontos(x1, y1, x2, y2):
    distância = sqrt((x2 - x1)^2 + (y2 - y1)^2)
    Retornar distância
Fim Função

// Uso da função
Início
    x1 = 1
    y1 = 2
    x2 = 4
    y2 = 6

    distânciaCalculada = distanciaEntrePontos(x1, y1, x2, y2)
    escreva("A distância entre os pontos é: " + distânciaCalculada)
Fim
```

## 2. Fatorial de um número

Escreva um algoritmo para calcular o fatorial de um número inteiro não negativo. O fatorial de um número n é o produto de todos os números inteiros positivos menores ou iguais a n. Por exemplo, o fatorial de 5 é 5 * 4 * 3 * 2 * 1 = 120.

### Solução


```
// Pseudocódigo para calcular o fatorial de um número
Programa fatorial
Função fatorial(n):
    fatorial = 1
    para i de 1 até n:
        fatorial = fatorial * i
    fim para
    Retornar fatorial
Fim Função
// Uso da função
Início
    n = 5
    fatorialCalculado = fatorial(n)
    escreva("O fatorial de " + n + " é: " + fatorialCalculado)
Fim
```

## 3. Números pares

Escreva um algoritmo para imprimir todos os números pares entre 1 e 100.

### Solução


```
// Pseudocódigo para imprimir números pares entre 1 e 100
Programa pares
Início
    para i de 1 até 100:
        se i%2 == 0:
            escreva(i)
        fim se
    fim para
Fim
```

## 4. Média de uma sequência de números

Escreva um algoritmo para calcular a média de uma sequência de números inseridos pelo usuário.

### Solução


```
// Pseudocódigo para calcular a média de uma sequência de números
Programa media
Início
    soma = 0
    quantidade = 0
    // repetição (laço) infinito
    enquanto Verdadeiro:
        // ler número fornecido pelo usuário do programa
        número = entrada()
        se numero == 0:
            sair  // interrompe a repetição
        fim se
        soma = soma + número
        quantidade = quantidade + 1
    fim enquanto
    média = soma / quantidade
    escreva("A média da sequência é: " + média)
Fim
```

## 5. Maior elemento de uma sequência de números

Escreva um algoritmo para encontrar o maior elemento de uma sequência de números inseridos pelo usuário.

### Solução


```
// Pseudocódigo para encontrar o maior elemento de uma sequência de números
Programa maior
Início
    maior = 0
    enquanto Verdadeiro:
        número = entrada()
        se numero == '':
            sair
        fim se
        se número > maior:
            maior = número
        fim se
    fim enquanto
    escreva("O maior elemento da sequência é: " + maior)
Fim
```

## 6. Folha de pagamento

Uma empresa possui uma lista de funcionários com seus respectivos salários. A empresa precisa calcular a folha de pagamento total e a média salarial dos funcionários. Os dados são fornecidos na lista a seguir:

```
funcionarios = [
    ["Fulano", 1000],
    ["Beltrana", 2000],
    ["João Ninguém", 3000]
]
```

### Solução

```
PROGRAMA folha_pagamento
funcionarios = [
    ["Fulano", 1000],
    ["Beltrana", 2000],
    ["João Ninguém", 3000]
]
INICIO
    
    folha_pagamento_total = 0
    media_salarial = 0
    
    PARA funcionario NO funcionarios:
        folha_pagamento_total = folha_pagamento_total + funcionario[1]
        media_salarial = media_salarial + funcionario[1]
    FIM PARA
    
    media_salarial = media_salarial/ len(funcionarios)
    
    escrever("Folha de pagamento total:", folha_pagamento_total)
    escrever("Média salarial:", media_salarial)
FIM
```

## 7.Lista de produtos

Um supermercado possui uma lista de produtos com seus respectivos preços. O supermercado precisa calcular o valor total das compras de um cliente com base em uma lista de produtos que ele comprou. Crie um programa que realiza essa tarefa, de acordo com os dados a seguir:

```
// Dicionário - produto: preço unitário
produtos = {
    "maçã": 1.50,
    "banana": 2.00,
    "laranja": 3.00,
    "arroz": 6.00,
    "feijão": 9.00,
    "macarrão": 4.00,
    "carne": 30.00,
}

// Dicionário - produto: quantidade comprada
compras = {
    "banana": 5,
    "arroz": 2,
    "feijão": 1,
    "carne": 2
}
```

### Solução

```
PROGRAMA compras

produtos = {
    "maçã": 1.50,
    "banana": 2.00,
    "laranja": 3.00,
    "arroz": 6.00,
    "feijão": 9.00,
    "macarrão": 4.00,
    "carne": 30.00,
}

compras = {
    "banana": 5,
    "arroz": 2,
    "feijão": 1,
    "carne": 2
}
INICIO
    valor_total = 0

    PARA produto NO compras:
        valor_total = valor_total + produtos[produto]*compras[produto]
    FIM PARA

    escrever("Valor total das compras:", valor_total)
FIM
```

## 8. Biblioteca

Uma biblioteca possui uma lista de livros com seus respectivos autores. A biblioteca precisa gerar um dicionário com nomes de autores como chaves, e quantidade de livos como valores. Realize essa tarefa no dado a seguir:

```
livros = {
    "Fulano": ["Livro 1", "Livro 2", "Livro 3", "Livro 4"],
    "Beltrana": ["Livro 5", "Livro 6"],
    "João Ninguém": ["Livro 7", "Livro 8", "Livro 9", "Livro 10", "Livro 11"]
}
```

#### Solução

```
PROGRAMA biblioteca

livros = {
    "Fulano": ["Livro 1", "Livro 2", "Livro 3", "Livro 4"],
    "Beltrana": ["Livro 5", "Livro 6"],
    "João Ninguém": ["Livro 7", "Livro 8", "Livro 9", "Livro 10", "Livro 11"]
}

INICIO
quantidades = {}
PARA autor NO livros:
    soma = tamanho(livros[autor])
    quantidade.adicionar('autor', soma)
FIM PARA
escrever(quantidades)
//Resultado:
/*
    {
        "Fulano": 4
        "Beltrana": 2
        "João Ninguém": 5
    }
*/
FIM
```

## 9. Filmes

Um sistema de recomendação de filmes precisa gerar uma lista de filmes recomendados para um usuário com base em seus filmes favoritos.

```
filmes_recomendados = {
    "O Poderoso Chefão": ["O Poderoso Chefão II", "O Poderoso Chefão III", "Scarface"],
    "Star Wars": ["Star Wars: O Império Contra-Ataca", "Star Wars: O Retorno de Jedi", "Star Wars: O Despertar da Força"],
    "Indiana Jones": ["Indiana Jones e Os Caçadores da Arca Perdida", "Indiana Jones e o Templo da Perdição", "Indiana Jones e a Última Cruzada"],
    "Jurassic Park": ["O Mundo Perdido: Jurassic Park", "Jurassic Park III", "Jurassic World"],
    "Matrix": ["Matrix Reloaded", "Matrix Revolutions", "Inception"],
    "O Exterminador do Futuro": ["O Exterminador do Futuro 2: O Julgamento Final", "O Exterminador do Futuro 3: A Rebelião das Máquinas", "O Exterminador do Futuro: Gênesis"],
    "O Senhor dos Anéis": ["O Hobbit", "As Crônicas de Nárnia", "Game of Thrones"],
    "Piratas do Caribe": ["Piratas do Caribe: A Maldição do Pérola Negra", "Piratas do Caribe: O Baú da Morte", "Piratas do Caribe: No Fim do Mundo"],
    "Toy Story": ["Toy Story 2", "Toy Story 3", "Toy Story 4"]
}

filmes_favoritos = ["O Poderoso Chefão", "O Senhor dos Anéis", "Matrix"]
```

Crie um código que realize essa tarefa

### Solução


```
PROGRAMA filmes
// variáveis 'filmes_recomendados' e 'filmes_recomendados' aqui

INICIO
    recomendacoes = []
    PARA filme_favorito NO filmes_favoritos:
        recomendacoes = recomendacoes + filmes_recomendados[filme_favorito]
    FIM PARA
    
escrever("Filmes recomendados:", recomendacoes)
fim
```


## 10. Lei da Gravitação Universal

Calcule o módulo da atração gravitacional entre duas partículas, definidas com os dicionários a seguir:

```
particula_1 = {
    'massa': 10,
    'posição': [1, 0]
}

particula_2 = {
    'massa': 300,
    'posição': [0, 10]
}
```

### Solução

```
PROGRAMA força

constante_gravitacional = 1

INICIO
    produto_massas = particula_1['massa'] * particula_2['massa']
    
    distancia_quadrado = particula_1['posição][0] * particula_2['posição][0] + particula_1['posição][1] * particula_2['posição][1]
    
    F = constante_gravitacional * produto_massas / distancia_quadrado
    escrever(F)
FIM
```