# Operações

Operações são usadas para executar cálculos em valores. Python oferece uma ampla variedade de operações, incluindo:

## Operadores aritméticos

Os operadores aritméticos são usados para realizar cálculos matemáticos básicos, como adição (+), subtração (-), multiplicação (*) e divisão (/). Por exemplo, o seguinte código imprime o resultado da adição de 10 e 20:

```
print(10 + 20)
```

### Tabela de Operadores Aritméticos

| Operador | Descrição | Exemplo | Resultado |
| --- | --- | --- | --- |
| + | Adição | 10 + 20 | 30 |
| - | Subtração | 20 - 10 | 10 |
| * | Multiplicação | 10 * 20 | 200 |
| / | Divisão | 20 / 10 | 2.0 |
| % | Módulo (resto da divisão) | 27 % 10 | 7 |
| ** | Exponenciação | 10 ** 2 | 100 |
| // | Divisão inteira | 27 // 10 | 2 |

## Operadores relacionais:

Os operadores relacionais são usados para comparar dois valores. Os operadores relacionais incluem maior que (>), menor que (<), maior ou igual a (>=), menor ou igual a (<=), igual a (==) e diferente de (!=). Por exemplo, o seguinte código imprime o resultado da comparação de 10 e 20:

```
print(10 > 20)
```

### Tabela de Operadores Relacionais

| Operador | Descrição | Exemplo | Resultado |
| --- | --- | --- | --- |
| > | Maior que | 10 > 20 | False |
| < | Menor que | 10 < 20 | True |
| >= | Maior ou igual a | 10 >= 10 | True |
| <= | Menor ou igual a | 10 <= 10 | True |
| == | Igual a | 10 == 10 | True |
| != | Diferente de | 10 != 20 | True |

## Operadores lógicos

Os operadores lógicos são fundamentais em programação para avaliar condições e tomar decisões com base em expressões booleanas. Vamos explorar mais sobre eles e como podem ser aplicados em Python.

### Operador "E"

O operador "E" (também conhecido como "and") é representado pelo símbolo && em algumas linguagens, mas em Python, é simplesmente `and`. Ele retorna verdadeiro (True) se ambas as expressões comparadas forem verdadeiras. Vejamos um exemplo:

```
x = 10
y = 20
z = 30

resultado = (x < y) and (y < z)
print(resultado)  # Saída: True
```

Neste exemplo, a expressão (`x < y`) é verdadeira, pois 10 é menor que 20, e (`y < z`) também é verdadeira, já que 20 é menor que 30. Portanto, a expressão completa (`x < y`) and (`y < z`) verdadeira, e o resultado impresso será `True`.

### Operador "OU"
O operador "OU" (também conhecido como "or") é representado pelo símbolo || em algumas linguagens, mas em Python, é simplesmente `or`. Ele retorna verdadeiro (True) se pelo menos uma das expressões comparadas for verdadeira. Vamos ver um exemplo:

```
idade = 25

resultado = (idade < 18) or (idade >= 65)
print(resultado)  # Saída: False
```

Neste exemplo, a expressão (idade < 18) é falsa, pois 25 não é menor que 18, mas (idade >= 65) é falsa também, pois 25 não é maior ou igual a 65. Como nenhuma das expressões é verdadeira, o resultado da expressão completa (idade < 18) or (idade >= 65) é falso, e o resultado impresso será False.

### Operador "NÃO"

O operador "NÃO" (também conhecido como "not") é representado pelo símbolo ! em algumas linguagens, e em Python é `not`. Ele inverte o valor de uma expressão booleana. Vamos ver um exemplo:

```
x = 10
y = 20

resultado = not (x == y)
print(resultado)  # Saída: True
```
Neste exemplo, a expressão (x == y) é falsa, pois 10 não é igual a 20. Usando o operador "NÃO", invertemos esse resultado para verdadeiro, pois queremos saber se x é diferente de y.
Tabela de Operadores Lógicos em Python

Aqui está uma tabela resumindo os operadores lógicos em Python:

### Tabela de Operadores Lógicos

| Operador | Descrição | Exemplo de Uso | Resultado |
| ---------- | ----------- | ---------------- | ----------- |
| `and`    | E         | `True and False` | False |
| `or`     | OU        | `True or False`  | True  |
| `not`    | NÃO       | `not True`       | False |

Esses operadores são extremamente úteis para criar lógica condicional em seus programas Python. Eles permitem que você controle o fluxo do seu código com base em condições específicas, tornando seus programas mais dinâmicos e eficientes.

## Operadores de atribuição

Os operadores de atribuição são fundamentais em Python para modificar o valor de variáveis de forma rápida e eficiente. Vamos aprofundar nossos conhecimentos sobre eles e ver como podem ser aplicados em situações diversas.

No início desta seção vimos o operador de atribuição simples (=). Mas existem outras formas de realizar atribuições de valores a variáveis


### Atribuição com adição (+=)

O operador += é usado para adicionar um valor à variável existente e, em seguida, atualizar o valor da variável com o resultado da adição. Vejamos um exemplo:

```
t = 1
dt = 0.01
t += dt  # Adiciona 5 ao valor de x
print(dt)  # Saída: 1.01
```
Neste exemplo, o valor original de t é 1. Usando t += 0.01, adicionamos dt, ou seja, 0.01 ao valor de t, resultando em 1.01.

### Atribuição com Subtração (-=)

O operador -= é usado para subtrair um valor da variável existente e, em seguida, atualizar o valor da variável com o resultado da subtração. Vejamos um exemplo:

```
y = 20
y -= 8  # Subtrai 8 do valor de y
print(y)  # Saída: 12
```

Neste exemplo, o valor original de y é 20. Usando y -= 8, subtraímos 8 do valor de y, resultando em 12.

### Atribuição com Multiplicação (*=)

O operador *= é usado para multiplicar o valor da variável existente por um determinado valor e, em seguida, atualizar o valor da variável com o resultado da multiplicação. Vejamos um exemplo:

```
z = 5
z *= 3  # Multiplica o valor de z por 3
print(z)  # Saída: 15
```

Neste exemplo, o valor original de z é 5. Usando z *= 3, multiplicamos o valor de z por 3, resultando em 15.

### Atribuição com Divisão (/=)

O operador /= é usado para dividir o valor da variável existente por um determinado valor e, em seguida, atualizar o valor da variável com o resultado da divisão. Vejamos um exemplo:

```
w = 50
w /= 10  # Divide o valor de w por 10
print(w)  # Saída: 5.0
```
Neste exemplo, o valor original de w é 50. Usando w /= 10, dividimos o valor de w por 10, resultando em 5.0.

## Operações em tipos de texto

### Concatenação de Strings

A concatenação de strings em Python é feita utilizando o operador `+`. Vamos ver um exemplo simples de como podemos concatenar duas strings:

```
string1 = "Olá"
string2 = "mundo!"
resultado = string1 + " " + string2
print(resultado)
```

Resultado:
```
Olá mundo!
```

No exemplo acima, as strings "Olá" e "mundo!" foram concatenadas para formar a frase "Olá mundo!". Note que utilizamos o espaço entre as strings para garantir que haja um espaço entre as palavras na frase final.

### Fatiamento de Strings

O fatiamento de strings em Python é feito utilizando colchetes `[]`. Podemos selecionar partes específicas de uma string com base nos índices. Vamos ver um exemplo de como fatiar uma string:

```
frase = "Python é uma linguagem de programação poderosa"
palavra = frase[0:6]
print(palavra)
```

Resultado:
```
Python
```

No exemplo acima, fatiamos a string para obter a palavra "Python" a partir dos índices 0 a 5. Lembre-se de que o índice inicial é inclusivo e o índice final é exclusivo.

### Busca em Strings

A busca em strings em Python é feita utilizando o operador `in`. Podemos verificar se uma determinada substring está presente em uma string maior. Vamos ver um exemplo de como buscar uma substring em uma string:

```
frase = "Python é uma linguagem de programação poderosa"
busca = "linguagem" in frase
print(busca)
```

Resultado:
```
True
```

No exemplo acima, verificamos se a palavra "linguagem" está presente na frase. O resultado da busca foi `True`, indicando que a palavra foi encontrada na string.

## Substituição em Strings

A substituição em strings em Python é feita utilizando o método `replace()`. Podemos substituir uma substring por outra em uma string. Vamos ver um exemplo de como substituir uma palavra em uma frase:

```
frase = "Python é uma linguagem de programação poderosa"
nova_frase = frase.replace("Python", "JavaScript")
print(nova_frase)
```

Resultado:
```
JavaScript é uma linguagem de programação poderosa
```

No exemplo acima, substituímos a palavra "Python" por "JavaScript" na frase. A nova frase resultante foi impressa no console.