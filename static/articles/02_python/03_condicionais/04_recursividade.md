# Recursividade

A recursividade é um conceito fundamental na programação, que consiste na capacidade de uma função chamar a si mesma para resolver um problema de forma mais simples. Neste arquivo, vamos explorar as leis da recursão, como calcular a soma de números de forma recursiva, a busca binária, boas práticas na implementação de funções recursivas e as vantagens e desvantagens desse método.

## As leis da recursão

Existem três leis fundamentais que devem ser seguidas ao implementar funções recursivas:
1. **Base Case**: toda função recursiva deve ter um caso base, que é a condição que determina quando a recursão deve parar.
2. **Progressão**: a função recursiva deve sempre progredir em direção ao caso base, ou seja, a cada chamada recursiva, o problema deve se tornar mais simples.
3. **Chamada recursiva**: a função deve chamar a si mesma para resolver subproblemas.

## Calculando a soma de números

Um exemplo clássico de recursão é o cálculo da soma de números de 1 a n. Vamos implementar essa função de forma recursiva em Python:

```
def soma_recursiva(n):
    if n == 1:
        return 1
    else:
        return n + soma_recursiva(n-1)

# Testando a função
print(soma_recursiva(5))  # Saída: 15
```

Neste exemplo, a função `soma_recursiva` chama a si mesma para calcular a soma de todos os números de 1 até n.

## Busca binária

A busca binária é um algoritmo eficiente para encontrar um elemento em um array ordenado. Vamos implementar a busca binária de forma recursiva em Python:

```
def busca_binaria(arr, elemento, inicio=0, fim=None):
    if fim is None:
        fim = len(arr) - 1
    
    if inicio > fim:
        return None
    
    meio = (inicio + fim) // 2
    
    if arr[meio] == elemento:
        return meio
    elif arr[meio] < elemento:
        return busca_binaria(arr, elemento, meio+1, fim)
    else:
        return busca_binaria(arr, elemento, inicio, meio-1)

# Testando a função
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
elemento = 5
print(busca_binaria(arr, elemento))  # Saída: 4
```

Neste exemplo, a função `busca_binaria` realiza a busca de um elemento em um array ordenado de forma recursiva. Em detalhes, temos:

1. **Definição da função `busca_binaria`:** Esta linha define uma função chamada `busca_binaria`, que será responsável por encontrar a posição de um elemento em uma lista ordenada usando o algoritmo de busca binária.

2. **Parâmetros da função:** A função recebe quatro parâmetros: arr (a lista onde será feita a busca), elemento (o elemento que estamos procurando na lista), inicio (o índice inicial da parte da lista que estamos considerando) e fim (o índice final da parte da lista que estamos considerando).

3. **Inicialização de `fim`:** Se o parâmetro fim não for fornecido quando chamamos a função, ele é definido como o índice do último elemento da lista.

4. **Condição de parada:** Se o índice inicial for maior que o índice final, significa que não há mais elementos a serem verificados na lista. Nesse caso, a função retorna `None`, indicando que o elemento não foi encontrado.

5. **Cálculo do meio:** O índice médio (meio) da parte da lista que estamos considerando é calculado dividindo a soma do índice inicial e final por 2. Este é o ponto de divisão onde vamos comparar o elemento desejado.

6. **Verificação do elemento no meio da lista:** Comparamos o elemento no índice meio com o elemento que estamos buscando. Se forem iguais, retornamos o índice meio, indicando que encontramos o elemento naquela posição.

7. **Decisão de continuar a busca:** Se o elemento no índice meio for menor que o elemento que estamos buscando, isso significa que o elemento que queremos está na metade direita da lista. Chamamos a função `busca_binaria` novamente, mas com o índice de início atualizado para meio + 1 para buscar na metade direita da lista.

8. **Decisão de continuar a busca (parte 2):** Se o elemento no índice meio for maior que o elemento que estamos buscando, isso significa que o elemento que queremos está na metade esquerda da lista. Chamamos a função `busca_binaria` novamente, mas com o índice de fim atualizado para meio - 1 para buscar na metade esquerda da lista.

## Boas práticas na implementação de funções recursivas

Ao implementar funções recursivas, é importante seguir algumas boas práticas:

- Garantir que a função tenha um caso base bem definido.
- Verificar se a função está progredindo em direção ao caso base.
- Evitar recursões infinitas, garantindo que a recursão tenha um fim.

## Vantagens e desvantagens

### Vantagens:

- Facilita a implementação de algoritmos para problemas complexos que podem ser divididos em subproblemas.
- Pode tornar o código mais legível e conciso em comparação com soluções iterativas.

### Desvantagens:

- Pode ser menos eficiente em termos de tempo e espaço em comparação com abordagens iterativas.
- O excesso de chamadas recursivas pode levar a estouro de pilha (stack overflow) em casos de problemas muito grandes.

Experimente implementar funções recursivas e explore os benefícios desse método na resolução de problemas.
