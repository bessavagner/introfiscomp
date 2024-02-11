# Variáveis e tipos de dados em Python

Variáveis são elementos fundamentais em Python, pois são utilizadas para armazenar e manipular dados na memória do computador. Ao atribuir um valor a uma variável, você está reservando um espaço na memória para armazenar esse valor. Vamos explorar mais sobre variáveis e os tipos de dados suportados em Python.

## Criando e acessando variáveis

Para criar uma variável em Python, basta atribuir um valor a ela usando o operador de atribuição `=`. Por exemplo:

```python
x = 10
```

Neste exemplo, declaramos uma variável chamada `x` e atribuímos o valor `10` a ela. Para acessar o valor armazenado em uma variável, basta utilizar o nome da variável. Por exemplo, para imprimir o valor da variável `x` no console, você usaria:

```python
print(x)
```

## Regras para nomes de variáveis

Ao escolher nomes para suas variáveis em Python, é importante seguir algumas regras:

- Os nomes de variáveis devem começar com uma letra (a-z, A-Z) ou sublinhado `_`.
- Não podem conter espaços ou caracteres especiais como `$`, `#`, `@`.
- Os nomes das variáveis devem ser únicos dentro do escopo em que são definidos.
- Evite utilizar palavras-chave reservadas do Python como nomes de variáveis.
- Escolha nomes significativos e descritivos para suas variáveis para facilitar a compreensão do seu código.

## Tipos de dados em Python

Python suporta diversos tipos de dados que podem ser armazenados em variáveis. Vamos explorar alguns dos tipos de dados mais comuns:

### Números

Em Python, os números podem ser inteiros, flutuantes ou complexos. Veja exemplos:

```python
inteiro = 10
flutuante = 10.5
complexo = 10 + 2j
```

### Strings

Strings são sequências de caracteres e podem ser definidas usando aspas simples ou duplas:

```python
mensagem = "Olá mundo!"
```

#### Método format

O método format permite formatar strings com valores dinâmicos. A string é definida com marcadores {} que são substituídos pelos valores das variáveis. Veja um exemplo:

```
nome = "João"
idade = 25

frase_formatada = "Olá, {}! Você tem {} anos.".format(nome, idade)
print(frase_formatada)
```

O código acima imprime a seguinte saída:

```
Olá, João! Você tem 25 anos.
```

O método format oferece diversas opções de formatação para controlar a aparência dos valores na string.

#### Interpolação de strings (f-strings)

As f-strings (strings literais formatadas) são uma maneira mais concisa de formatar strings. A string é definida com o prefixo f e pode conter expressões Python entre chaves {}. Veja um exemplo:

```
nome = "João"
idade = 25

frase_interpolada = f"Olá, {nome}! Você tem {idade} anos."
print(frase_interpolada)
```

O código acima imprime a mesma saída do exemplo anterior.

As f-strings são mais concisas e fáceis de ler do que o método format. Elas também oferecem suporte a expressões mais complexas dentro da string.

**Observação**: As f-strings só estão disponíveis no Python 3.6 e versões posteriores.

### Listas

Listas são coleções ordenadas de elementos e podem conter diferentes tipos de dados. Para acessar os elementos de uma lista, você pode utilizar índices:

```python
lista = [1, 2, 3, "Python", True]

# Acessando o terceiro elemento da lista
print(lista[2])
```

### Tuplas

Tuplas são similares às listas, mas são imutáveis, ou seja, não podem ser alteradas após a criação. Para acessar os elementos de uma tupla, também é possível utilizar índices:

```python
tupla = (1, 2, 3, "Python", True)

# Acessando o último elemento da tupla
print(tupla[-1])
```

### Dicionários

Dicionários são coleções de pares chave-valor e são muito úteis para armazenar informações relacionadas. Para acessar os valores de um dicionário, você pode utilizar as chaves:

```python
dicionario = {"nome": "Maria", "idade": 25, "cidade": "São Paulo"}

# Acessando a idade no dicionário
print(dicionario["idade"])
```

Esses são apenas alguns dos tipos de dados suportados em Python. Ao utilizar variáveis e tipos de dados de forma eficiente, você poderá criar programas mais robustos e expressivos. Experimente criar suas próprias variáveis e explorar diferentes tipos de dados em Python!
