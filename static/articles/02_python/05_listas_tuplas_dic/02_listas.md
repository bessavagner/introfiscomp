# Listas

As listas são estruturas de dados muito versáteis e úteis em Python. Elas permitem armazenar diversos tipos de elementos em uma única variável, facilitando o acesso e manipulação desses dados.

## Iterando sobre listas

Para percorrer uma lista em Python, podemos utilizar um loop `for`. Veja um exemplo:

```
frutas = ['maçã', 'banana', 'laranja']

for fruta in frutas:
    print(fruta)
```

Neste exemplo, o loop `for` itera sobre cada elemento da lista `frutas` e imprime o nome de cada fruta na tela.

## Unpacking

O unpacking em Python permite atribuir os elementos de uma lista a variáveis separadas. Veja alguns exemplos:

```
# Unpacking de uma lista
numeros = [1, 2, 3]
a, b, c = numeros

# Unpacking de uma lista de tuplas
pontos = [(1, 2), (3, 4), (5, 6)]
for x, y in pontos:
    print(f'Coordenadas: ({x}, {y})')

# Unpacking com *
numeros = [1, 2, 3, 4, 5]
primeiro, *restante = numeros
print(primeiro)  # Saída: 1
print(restante)  # Saída: [2, 3, 4, 5]
```

## Métodos de listas

Python possui diversos métodos embutidos que facilitam a manipulação de listas. Aqui estão alguns exemplos:

```
numeros = [1, 2, 3, 4, 5]

# Adicionar um elemento ao final da lista
numeros.append(6)

# Remover um elemento específico da lista
numeros.remove(3)

# Ordenar a lista
numeros.sort()

# Inverter a ordem dos elementos
numeros.reverse()

# Contar a ocorrência de um elemento
count_2 = numeros.count(2)

# Limpar a lista
numeros.clear()
```

## Fatias

As fatias (slices) em Python permitem acessar partes específicas de uma lista. Veja um exemplo:

```
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Acessar os elementos do índice 2 ao índice 5
print(numeros[2:6])  # Saída: [3, 4, 5, 6]

# Acessar os elementos do índice 0 ao índice 7, de 2 em 2
print(numeros[0:8:2])  # Saída: [1, 3, 5, 7]
```

## List comprehension

List comprehension é uma forma concisa de criar listas em Python. Veja um exemplo usando f-string para formatar os elementos da lista:

```
numeros = [1, 2, 3, 4, 5]

# Criar uma nova lista com o quadrado dos números
quadrados = [f'O quadrado de {num} é {num**2}' for num in numeros]

print(quadrados)
```

Neste exemplo, a lista `quadrados` será uma lista de strings formatadas com os quadrados dos números da lista `numeros`.
