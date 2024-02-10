# Listas e vetores (arrays)

## O que são listas e vetores?

Listas e vetores são estruturas de dados fundamentais que armazenam uma coleção de elementos, onde cada elemento possui uma posição única. Eles são amplamente utilizados em programação para armazenar e manipular dados de forma eficiente.

## Como criar listas e vetores em pseudocódigo?

Em pseudocódigo, podemos criar uma lista ou vetor da seguinte forma:

```
numeros = [1, 2, 3, 4, 5]
nomes = ["Fulano", "Beltrana", "João Ninguém"]
```
## Tipos de elementos em listas e vetores

As listas e os vetores podem armazenar elementos de diversos tipos, incluindo inteiros, números reais, strings e até outras listas ou vetores.

Aqui estão alguns exemplos:

```
lista_numeros = [1, 2, 3, 4, 5] // lista de números inteiros
lista_nomes = ["Fulano", "Beltrana", "João Ninguém"] // lista de strings
lista_mista = [1, "dois", 3.14, True] // lista com elementos de tipos diferentes
```

## Quais são as principais vantagens de listas e vetores?

Listas e vetores são estruturas de dados muito versáteis e oferecem várias vantagens:

1. **Armazenamento de dados sequenciais**: As listas são usadas para armazenar coleções de elementos em uma ordem específica. Isso é útil em situações onde a ordem dos elementos é relevante, como em listas de tarefas, histórico de atividades, etc.

2. **Implementação de pilhas (stacks) e filas (queues)**: As listas podem ser usadas para implementar pilhas e filas, onde os elementos são adicionados e removidos de acordo com o princípio "último a entrar, primeiro a sair" (LIFO) para pilhas e "primeiro a entrar, primeiro a sair" (FIFO) para filas.

3. **Iteração e processamento de dados**: Listas são frequentemente usadas em loops e iterações para processar uma sequência de elementos. Isso pode envolver a execução de operações em cada elemento da lista, filtragem com base em critérios específicos, ou agregação de valores.

4. **Armazenamento de resultados de consultas ou cálculos**: As listas são usadas para armazenar os resultados de consultas a bancos de dados, cálculos matemáticos ou processamento de dados de entrada, permitindo fácil acesso e manipulação desses resultados.

5. **Implementação de estruturas de dados complexas**: Listas são componentes básicos de muitas outras estruturas de dados, como árvores, grafos e matrizes. Elas podem ser usadas para representar conexões entre elementos ou para organizar dados em uma estrutura hierárquica.

6. **Ordenação e busca de elementos**: Listas podem ser ordenadas de acordo com critérios específicos, facilitando a busca e recuperação de elementos. Algoritmos de ordenação como o _merge sort_, _quicksort_ e _bubble sort_ são comumente aplicados a listas.

7. **Implementação de menus e interfaces de usuário**: Em interfaces de usuário de aplicativos, as listas são frequentemente usadas para exibir opções de menu, escolhas de seleção, ou listagens de itens em uma grade.

8. **Gerenciamento de memória**: Em linguagens de baixo nível, as listas podem ser usadas para alocar e gerenciar blocos de memória dinâmica, permitindo a criação de estruturas de dados flexíveis.

9. **Manipulação de dados estruturados**: Listas podem ser usadas para representar dados estruturados, como registros em um banco de dados ou propriedades de objetos em linguagens de programação orientadas a objetos.

10. **Implementação de estruturas de controle**: Listas podem ser usadas para armazenar condições ou casos em estruturas de controle condicional, como em uma série de instruções if-else ou em um switch-case.

## Operações

As operações mais comuns em listas e vetores incluem:

- **Adicionar elementos:** Adiciona um novo elemento à lista ou vetor.
- **Acessar elementos:** Obter o valor de um elemento específico na lista ou vetor.
- **Remover elementos:** Remove um elemento específico da lista ou vetor.
- **Concatenação:** Combina duas ou mais listas ou vetores em uma única lista ou vetor.
- **Tamanho:** Retorna o número de elementos da lista ou vetor.

## Operações

As operações em lstas de pseudocódigos seguem uma sintaxe relaxada: desde que você descreva como funciona o método ou função de operação sobre uma ou mais listas, e quais os seus argumetos e seus tipos, você é livre para expressar operações em listas usando pseudocódigos. A notação que vamos adotar aqui é de métodos de objetos: um ponto separa o nome do objeto (da lista, no caso) e do método.

Antes, vamos definir o acesso aos elementos de uma lista.

### 1. Acessar elementos (índices)

Usamos a notação de índices (número inteiro entre par de colchetes) para representas o acesso de um elemento em uma lista. Listas são sequÊncias de elementos indexados, geralmente começado pelo índice zero:

```
// Acessar primeiro elemento da lista
numeros = [1, 2, 3, 4, 5]
elemento = numeros[0]
```

```
// Acessar o qurato elemento da lista
numeros = [1, 2, 3, 4, 5]
elemento = numeros[3]
```


### 2. Adicionar elementos

Podemos definir uma função de nome _AdicionarAoFinal_:

```
// Adicionar elemento ao final da lista
PROGRAMA adiciona_elementos

FUNÇÃO AdicionarAoFinal(lista, elemento):
    // Adiciona 'elemento' ao final
    // de 'lista'. Retorna o resultado
FIM FUNÇÃO

INICIO
    numeros = [1, 2, 3, 4, 5]
    novos_numeros = AdicionarAoFinal(numeros, 6)
    escreva(novos_numeros)
FIM
```

O resultado do programa acima é _[1, 2, 3, 4, 5]_

Podemos também definir uma operação de _AdicionarNaPosicao_:
```
// Adicionar elemento em uma posição específica
PROGRAMA adiciona_elementos

FUNÇÃO AdicionarNaposicao(lista, elemento, posicao):
    // Adiciona 'elemento' em 'posicao'
    // de 'lista'. Retorna o resultado
FIM FUNÇÃO

INICIO
    numeros = [1, 2, 3, 4, 5]
    novos_numeros = AdicionarNaposicao(numeros, 6, 2)
    escreva(novos_numeros)
FIM
```

Alternativamente, e preferencialmente, podemos definir métodos de litas como notação alternativa. Neste caso, as operações alteram a lista:

```
// Adicionar elemento em uma posição específica
PROGRAMA adiciona_elementos
// O método 'insert(elemento, posicao)' adiciona
// o valor 'elemento' na 'posicao' modificando a lista
INICIO
    numeros = [1, 2, 3, 4, 5]
    lista.insert(2.5, 2)
    escreva(numeros)
    //resultado: [1, 2, 2.5, 3, 4, 5]
FIM
```
```
// Adicionar elementoao final
PROGRAMA adiciona_elementos_ao_final
// O método 'append(elemento, posicao)' adiciona
// o valor 'elemento' ao final da lista
INICIO
    numeros = [1, 2, 3, 4, 5]
    lista.append('EOF')
    escreva(numeros)
    //resultado: [1, 2, 3, 4, 5, 'EOF']
FIM
```

Daqui pra frente vamos preferir a notação de métodos de objetos.

### 3. Remover elementos

Para remover elementos de uma lista ou vetor, podemos utilizar a operação de remoção. Existem duas formas comuns de remoção:

* **Remoção por índice:** Remove o elemento na posição especificada pelo índice.
* **Remoção por valor:** Remove o primeiro elemento que corresponde ao valor especificado.

Aqui estão alguns exemplos de remoção de elementos em pseudocódigo:

```
# Remoção por índice
numeros = [1, 2, 3, 4, 5]
numeros.remover(2)  # remove o elemento na posição 2
escrever(numeros)  # [1, 2, 4, 5]

# Remoção por valor
lista_nomes = ["Fulano", "Beltrana", "João Ninguém"]
lista_nomes.remover("Beltrana")  # remove o primeiro elemento com o valor "Beltrana"
escrever(lista_nomes)  # ["Fulano", "João Ninguém"]
```

### 4. Concatenação

A concatenação é a operação de unir duas ou mais listas ou vetores em uma única lista ou vetor. Em pseudocódigo, podemos utilizar o operador "+" para realizar a concatenação.

Aqui está um exemplo de concatenação em pseudocódigo:

```
numeros1 = [1, 2, 3]
numeros2 = [4, 5, 6]
numeros_concatenados = numeros1 + numeros2
escrever(numeros_concatenados)  # [1, 2, 3, 4, 5, 6]
```

### 5. Tamanho

É muito comum que lingagens de programação modernas definam o método (ou função) de se obter diretamente o tamanho (número de elementos) em uma lista:

```
numeros = [1, 2, 3]

// parecido com Javascript:
tamanho = numeros.tamanho();
escrever(tamanho)  # 3

// parecido com Python:
tamanho = tamanho(numeros);
escrever(tamanho)  # 3
```