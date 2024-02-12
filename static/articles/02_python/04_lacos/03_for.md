# Instrução for

A instrução `for` é utilizada em Python para iterar sobre uma sequência de elementos, como listas, dicionários, strings, entre outros. Ela permite percorrer cada item da sequência e executar um bloco de código para cada um deles.

## A função range()

A função `range()` é comumente utilizada em conjunto com a instrução `for` para gerar uma sequência de números. Ela pode receber um, dois ou três argumentos, que representam o início, o fim e o passo da sequência, respectivamente.

### Exemplo:

```
for i in range(1, 10, 2):
    print(i)
```

Neste exemplo, a função `range(1, 10, 2)` irá gerar a sequência de números ímpares de 1 a 9, pulando de 2 em 2.

## Iterando sobre sequências

### Listas

Para iterar sobre os elementos de uma lista, basta utilizar a instrução `for` juntamente com a lista desejada.

#### Exemplo:

```
alunos = ['Ana', 'João', 'Maria', 'Pedro']
for aluno in alunos:
    print(f'Olá, {aluno}!')
```

### Dicionários

Para iterar sobre os elementos de um dicionário, é possível utilizar o método `items()` para obter tanto a chave quanto o valor de cada item.

#### Exemplo:

```
notas = {'Ana': 8.5, 'João': 7.0, 'Maria': 9.0, 'Pedro': 6.5}
for aluno, nota in notas.items():
    if nota >= 7.0:
        print(f'{aluno} foi aprovado com a nota {nota}')
    else:
        print(f'{aluno} foi reprovado com a nota {nota}')
```

## Laços 'for' aninhados

É possível utilizar laços `for` dentro de outros laços `for`, o que é conhecido como laços aninhados. Isso é útil para percorrer estruturas de dados mais complexas, como listas de listas.

### Exemplo:

```
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for linha in matriz:
    for elemento in linha:
        print(elemento)
```

Neste exemplo, o código irá percorrer cada linha da matriz e, para cada linha, irá imprimir cada elemento contido nela.

## Usando o 'break'

A instrução `break` pode ser utilizada dentro de um laço `for` para interromper a execução do mesmo antes de percorrer todos os elementos da sequência.

### Exemplo:

```
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    if numero == 3:
        break
    print(numero)
```

Neste exemplo, o código irá percorrer a lista de números e imprimir cada um deles, mas irá parar a execução quando encontrar o número 3.


## Exercícios resolvidos

### Soma vetorial

Crie om programa que realiza a soma vertial de dois vetores em duas dimenções. Os vetores podem ser representados por listas ou tuplas.

#### Solução

```
def somar_vetores(v, w):
    resultante = []
    for vv, ww in zip(v, w):
        resultante.append(ww + ww)
    return resultante


v = [1, 0, 1]
w = [-1, 1, -1]
print(somar_vetores(v, w))
```

Saída:
```
[-2, 2, -2]
```

Acima usamos a função buil-in `zip`, que serve para combinar e manipular dados em diferentes estruturas iteráveis, como listas, tuplas e dicionários. Ela funciona agrupando elementos de cada iterável em tuplas, criando uma nova estrutura de dados que facilita a manipulação conjunta dos dados originais

#### Mais exemplos de aplicação de zip

```
# Combinar duas listas em uma lista de tuplas
lista_nomes = ["Ana", "João", "Maria"]
lista_idades = [20, 25, 30]

dados_pessoais = zip(lista_nomes, lista_idades)

# Iterar sobre duas listas simultaneamente
for nome, idade in dados_pessoais:
    print(f"{nome} tem {idade} anos")

# Desempacotar tuplas
nome, idade = zip(*dados_pessoais)

# Criar dicionários
dicionario_pessoas = dict(zip(lista_nomes, lista_idades))
```