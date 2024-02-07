# Exercícios Resolvidos
## Exercício 1: Cálculo de distância

Escreva um algoritmo para calcular a distância entre dois pontos no espaço bidimensional. Os pontos são representados por suas coordenadas _(x1, y1)_ e _(x2, y2)_.

- Solução:

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

## Exercício 2: Fatorial de um número

Escreva um algoritmo para calcular o fatorial de um número inteiro não negativo. O fatorial de um número n é o produto de todos os números inteiros positivos menores ou iguais a n. Por exemplo, o fatorial de 5 é 5 * 4 * 3 * 2 * 1 = 120.

- Solução:

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

# Exercício 3: Números pares

Escreva um algoritmo para imprimir todos os números pares entre 1 e 100.

- Solução:

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

# Exercício 4: Média de uma sequência de números

Escreva um algoritmo para calcular a média de uma sequência de números inseridos pelo usuário.
Solução:

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

# Exercício 5: Maior elemento de uma sequência de números

Escreva um algoritmo para encontrar o maior elemento de uma sequência de números inseridos pelo usuário.
Solução:

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
