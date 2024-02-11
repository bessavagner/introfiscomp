# Operadores relacionais

Os operadores relacionais são essenciais na programação, pois permitem comparar valores, facilitando a tomada de decisões e o controle do fluxo do programa. Eles sempre retornam um valor booleano (`True` ou `False`), dependendo do resultado da comparação entre os valores.

## Igual a (==)

Este operador verifica se dois valores são exatamente iguais. É importante diferenciar o operador de igualdade (`==`) do operador de atribuição (`=`).

```python
# Comparando números
numero1 = 10
numero2 = 10
print(numero1 == numero2)  # Saída: True

# Comparando strings
texto1 = "Python"
texto2 = "python"
print(texto1 == texto2)  # Saída: False
```

## Diferente de (!=)

Verifica se dois valores não são iguais. Se forem diferentes, o resultado é `True`.

```python
# Exemplo com números
valor1 = 100
valor2 = 200
print(valor1 != valor2)  # Saída: True

# Exemplo com strings
nome1 = "Alice"
nome2 = "Bob"
print(nome1 != nome2)  # Saída: True
```

## Maior que (>)

Avalia se o valor à esquerda do operador é maior que o valor à direita.

```python
idadePedro = 18
idadeMaria = 21
print(idadePedro > idadeMaria)  # Saída: False

# Comparando valores em uma lista
notas = [7, 8, 9, 10]
print(max(notas) > 9)  # Saída: True
```

## Menor que (<)

Verifica se o valor à esquerda é menor que o valor à direita.

```python
peso1 = 55.5
peso2 = 60.0
print(peso1 < peso2)  # Saída: True

# Utilizando em condições climáticas
temperatura = 30
print(temperatura < 25)  # Saída: False
```

## Maior ou igual a (>=)

Confirma se o valor à esquerda é maior ou igual ao valor à direita.

```python
saldoConta = 500
compra = 500
print(saldoConta >= compra)  # Saída: True

# Avaliando notas
notaAluno = 7.5
notaMinima = 7.0
print(notaAluno >= notaMinima)  # Saída: True
```

## Menor ou igual a (<=)

Verifica se o valor à esquerda é menor ou igual ao valor à direita.

```python
alturaMuro = 2.5  # metros
alturaEscada = 3.0  # metros
print(alturaMuro <= alturaEscada)  # Saída: True

# Comparando idades
idadeMinima = 18
candidatoIdade = 16
print(candidatoIdade <= idadeMinima)  # Saída: True
```