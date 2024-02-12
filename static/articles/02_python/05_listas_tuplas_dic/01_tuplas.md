# Tuplas

As tuplas são estruturas de dados em Python muito semelhantes às listas, porém são imutáveis, ou seja, não podem ser alteradas após a sua criação. Elas são úteis para armazenar coleções de itens que não precisam ser modificados.

## Criando e acessando tuplas

Para criar uma tupla em Python, utilizamos parênteses `()` e separamos os elementos por vírgulas. Veja um exemplo:

```
# Criando uma tupla de coordenadas
coordenadas = (10, 20)

# Acessando os elementos da tupla
print(coordenadas[0])  # Saída: 10
print(coordenadas[1])  # Saída: 20
```

## Desempacotamento de tuplas

Assim como nas listas, é possível desempacotar os elementos de uma tupla em variáveis separadas. Veja um exemplo:

```
# Desempacotando uma tupla
coord_x, coord_y = coordenadas

print(coord_x)  # Saída: 10
print(coord_y)  # Saída: 20
```

## Métodos de tuplas

Como as tuplas são imutáveis, elas possuem menos métodos embutidos do que as listas. No entanto, ainda existem algumas operações que podem ser realizadas. Veja um exemplo:

```
# Contar a ocorrência de um elemento em uma tupla
numeros = (1, 2, 3, 4, 1, 2, 1)
count_1 = numeros.count(1)

print(count_1)  # Saída: 3
```

## Usos das tuplas

As tuplas são frequentemente utilizadas em situações em que os dados não devem ser alterados, como por exemplo ao retornar múltiplos valores de uma função. Veja um exemplo:

```
# Função que retorna coordenadas x e y
def obter_coordenadas():
    return 10, 20

x, y = obter_coordenadas()
print(f'Coordenadas: ({x}, {y})')  # Saída: Coordenadas: (10, 20)
```

As tuplas são uma estrutura de dados versátil e eficiente em Python, sendo úteis em diversas situações, principalmente quando os dados não devem ser modificados após a sua criação.
