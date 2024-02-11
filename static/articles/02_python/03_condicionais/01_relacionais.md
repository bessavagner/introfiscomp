# Operadores Relacionais

Os operadores relacionais são essenciais na programação, pois permitem comparar valores, facilitando a tomada de decisões e o controle do fluxo do programa. Eles sempre retornam um valor booleano (`True` ou `False`), dependendo do resultado da comparação entre os valores.

## Igual a (==)

Este operador verifica se dois valores são exatamente iguais. É importante diferenciar o operador de igualdade (`==`) do operador de atribuição (`=`).

```
# Comparando números
numero_1 = 10
numero_2 = 10
print(numero_1 == numero_2)  # Saída: True

# Comparando strings
texto_1 = "Python"
texto_2 = "python"
print(texto_1 == texto_2)  # Saída: False
```

## Diferente de (!=)

Verifica se dois valores não são iguais. Se forem diferentes, o resultado é `True`.

```
# Exemplo com números
valor_1 = 100
valor_2 = 200
print(valor_1 != valor_2)  # Saída: True

# Exemplo com strings
nome_1 = "Alice"
nome_2 = "Bob"
print(nome_1 != nome_2)  # Saída: True
```

## Maior que (>)

Avalia se o valor à esquerda do operador é maior que o valor à direita.

```
idade_pedro = 18
idade_maria = 21
print(idade_pedro > idade_maria)  # Saída: False

# Comparando valores em uma lista
notas = [7, 8, 9, 10]
print(max(notas) > 9)  # Saída: True
```

## Menor que (<)

Verifica se o valor à esquerda é menor que o valor à direita.

```
peso_1 = 55.5
peso_2 = 60.0
print(peso_1 < peso_2)  # Saída: True

# Utilizando em condições climáticas
temperatura = 30
print(temperatura < 25)  # Saída: False
```

## Maior ou igual a (>=)

Confirma se o valor à esquerda é maior ou igual ao valor à direita.

```
saldo_conta = 500
compra = 500
print(saldo_conta >= compra)  # Saída: True

# Avaliando notas
nota_aluno = 7.5
nota_minima = 7.0
print(nota_aluno >= nota_minima)  # Saída: True
```

## Menor ou igual a (<=)

Verifica se o valor à esquerda é menor ou igual ao valor à direita.

```
altura_muro = 2.5  # metros
altura_escada = 3.0  # metros
print(altura_muro <= altura_escada)  # Saída: True

# Comparando idades
idade_minima = 18
candidato_idade = 16
print(candidato_idade <= idade_minima)  # Saída: True
```
