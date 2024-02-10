# Conjuntos

Um conjunto é uma estrutura de dados que armazena uma coleção de elementos únicos e não ordenados. Isso significa que cada elemento só pode aparecer uma vez no conjunto, e não há ordem específica entre os elementos.

Conjuntos são úteis para diversas aplicações, como:

- Armazenar e verificar se um elemento está presente em um conjunto.
- Encontrar a interseção, união e diferença entre conjuntos.
- Remover elementos duplicados de uma lista.

Em pseudocódigo, podemos criar um conjunto da seguinte forma:

```
conjunto = {1, 2, 3, "banana", True}
```

Conjuntos podem armazenar elementos de diversos tipos, incluindo inteiros, números reais, textos, e até mesmo outros conjuntos.

Aqui estão alguns exemplos:

```
conjunto_numeros = {1, 2, 3, 4, 5}
conjunto_nomes = {"Fulano", "Beltrana", "João Ninguém"}
conjunto_mista = {1, "dois", 3.14, True, {1, 2}}
```

## Aplicações

- **Eficiência:** A busca por um elemento em um conjunto é muito rápida, mesmo em conjuntos com muitos elementos.
- **Simplicidade:** A implementação de conjuntos é relativamente simples.
- **Versatilidade:** Conjuntos podem ser usados para diversas aplicações.

## Operações

Vamos use notação de métodos para apresentar operações em conjuntos aqui.

### 1. Acessar elementos

Em conjuntos, não podemos acessar elementos diretamente por índice, pois eles não são ordenados.

### 2. Adicionar elementos

Para adicionar um elemento a um conjunto, podemos usar a operação adicionar. Essa operação verifica se o elemento já existe no conjunto e, se não existir, o adiciona.

```
conjunto = {1, 2, 3}
conjunto.adicionar(4)
escrever(conjunto)  # {1, 2, 3, 4}
```

### 3. Remover elementos

Para remover um elemento de um conjunto, podemos usar a operação remover. Essa operação verifica se o elemento existe no conjunto e, se existir, o remove.

```
conjunto = {1, 2, 3}
conjunto.remover(2)
escrever(conjunto)  # {1, 3}
```

### 4. Verificar se um elemento está presente

Para verificar se um elemento está presente em um conjunto, podemos usar a operação contem. Essa operação retorna True se o elemento estiver presente no conjunto e False caso contrário.

```
conjunto = {1, 2, 3}
contem_elemento = conjunto.contem(2)
escrever(contem_elemento)  # True
```

### 5. Operações entre conjuntos

Podemos realizar diversas operações entre conjuntos, como:

- **União:** A união de dois conjuntos é um conjunto que contém todos os elementos dos dois conjuntos originais.
- **Interseção:** A interseção de dois conjuntos é um conjunto que contém apenas os elementos que estão presentes em ambos os conjuntos originais.
- **Diferença:** A diferença de dois conjuntos é um conjunto que contém os elementos que estão presentes no primeiro conjunto, mas não estão presentes no segundo conjunto.

```
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

uniao = conjunto1.uniao(conjunto2)
escrever(uniao)  # {1, 2, 3, 4, 5}

intersecao = conjunto1.intersecao(conjunto2)
escrever(intersecao)  # {3}

diferenca = conjunto1.diferenca(conjunto2)
escrever(diferenca)  # {1, 2}
```

**Observação**: As operações entre conjuntos podem ser implementadas de diferentes maneiras, e a sintaxe específica pode variar de acordo com a linguagem de programação que você está usando.
