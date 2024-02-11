# Funções built-ins do Python

Nesta seção vamos explorar a declaração e chamada de funções em Python, bem como a utilização de funções built-ins e a criação de funções personalizadas.

## Usando funções

As funções são uma parte essencial da programação em Python e são usadas para organizar e estruturar o código. Elas permitem que você divida seu código em blocos menores e reutilizáveis, o que torna seu código mais fácil de ler, entender e manter.


O Python possui um grande número de funções internas (_built-ins_) que podem ser usadas para realizar uma variedade de tarefas comuns. Essas funções são incorporadas à linguagem e estão sempre disponíveis para uso.

## Função print()

Uma das funções internas mais comuns é a função `print()`. Esta função é usada para exibir dados na tela. Por exemplo, o seguinte código exibe a mensagem "Olá, mundo!" na tela:

## Função input()

Outra função interna útil é a função input(). Esta função permite que você receba entrada do usuário durante a execução do programa. Ela espera que o usuário insira algum texto via teclado e retorna essa entrada como uma string.

```
nome = input("Por favor, digite seu nome: ")
print("Olá, " + nome + "! Bem-vindo!")

```
Neste exemplo, o programa solicita ao usuário que digite seu nome. A entrada do usuário é armazenada na variável nome, e em seguida, uma mensagem de boas-vindas é exibida junto com o nome inserido pelo usuário.

É importante notar que a função `input()` sempre retorna uma string, mesmo que o usuário insira um número ou outro tipo de dado. Se você precisar de um tipo diferente de dado, como um número inteiro ou ponto flutuante, precisará converter explicitamente a entrada usando as funções de conversão de tipo do Python, como `int()` ou `float()`. Por exemplo:

Isso garantirá que a entrada do usuário seja interpretada como um número inteiro.

```
idade = int(input("Por favor, digite sua idade: "))
```




```
print("Olá, mundo!")
```

## Conversões de tipos

- `int()`: Converte um valor para inteiro.
- `float()`: Converte um valor para ponto flutuante.
- `bool()`: Converte um valor para booleano.

```
numero = "10"
inteiro = int(numero)
print(inteiro)
```

## Funções de sequências

As sequências em Python, como listas, tuplas e strings, têm algumas funções úteis integradas que podem ser usadas para manipulá-las.

 - `len()`: Retorna o comprimento (número de itens) de uma sequência.
 - `max()`: Retorna o maior elemento de uma sequência.
 - `min()`: Retorna o menor elemento de uma sequência.
 - `sum()`: Retorna a soma de todos os elementos de uma sequência (para sequências numéricas).
 - `sorted()`: Retorna uma nova lista ordenada a partir dos elementos de uma sequência.

Exemplos:

```
lista = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(len(lista))       # Saída: 9
print(max(lista))       # Saída: 9
print(min(lista))       # Saída: 1
print(sum(lista))       # Saída: 36
print(sorted(lista))    # Saída: [1, 1, 2, 3, 4, 5, 5, 6, 9]

```

## Função _help_ e função _dir_

Além das funções internas específicas do Python, você também pode usar as funções `help()` e `dir()` para obter informações sobre objetos e módulos.

```
help(list)   # Mostra a documentação da lista
dir(list)    # Retorna os atributos disponíveis para listas
```

## Tabela de todas as funções built-ins

| Função | Descrição |
| --- | --- |
| `abs()` | Retorna o valor absoluto de um número. |
| `all()` | Retorna True se todos os elementos de uma sequência forem True. |
| `any()` | Retorna True se pelo menos um elemento de uma sequência for True. |
| `ascii()` | Retorna um string representando o código ASCII de um caractere. |
| `bin()` | Retorna um string representando a representação binária de um número. |
| `bool()` | Converte um objeto para um valor booleano. |
| `bytearray()` | Cria um novo objeto bytearray. |
| `bytes()` | Cria um novo objeto bytes. |
| `callable()` | Retorna True se um objeto for chamável. |
| `chr()` | Retorna o caractere correspondente a um código ASCII. |
| `classmethod()` | Cria um novo método de classe. |
| `compile()` | Compila um código Python. |
| `complex()` | Cria um novo número complexo. |
| `delattr()` | Exclui um atributo de um objeto. |
| `dict()` | Cria um novo dicionário. |
| `dir()` | Retorna uma lista dos atributos e métodos de um objeto. |
| `divmod()` | Retorna o quociente e o resto da divisão de dois números. |
| `enumerate()` | Retorna um iterador que gera tuplas contendo o índice e o valor de cada elemento de uma sequência. |
| `eval()` | Avalia uma expressão Python. |
| `exec()` | Executa um código Python. |
| `filter()` | Retorna um iterador que gera os elementos de uma sequência que satisfazem uma condição. |
| `float()` | Converte um objeto para um número de ponto flutuante. |
| `format()` | Formata um string. |
| `frozenset()` | Cria um novo conjunto imutável. |
| `getattr()` | Retorna o valor de um atributo de um objeto. |
| `globals()` | Retorna um dicionário com as variáveis globais do programa. |
| `hasattr()` | Retorna True se um objeto possui um determinado atributo. |
| `hash()` | Retorna o hash de um objeto. |
| `help()` | Exibe a documentação de uma função. |
| `hex()` | Retorna um string representando a representação hexadecimal de um número. |
| `id()` | Retorna o endereço de memória de um objeto. |
| `input()` | Lê uma linha de texto do console. |
| `int()` | Converte um objeto para um número inteiro. |
| `isinstance()` | Retorna True se um objeto for uma instância de uma determinada classe. |
| `issubclass()` | Retorna True se uma classe for uma subclasse de uma determinada classe. |
| `iter()` | Retorna um iterador que gera os elementos de uma sequência. |
| `len()` | Retorna o comprimento de uma sequência. |
| `list()` | Cria uma nova lista. |
| `locals()` | Retorna um dicionário com as variáveis locais do programa. |
| `map()` | Retorna um iterador que gera os elementos obtidos da aplicação de uma função a cada elemento de uma sequência. |
| `max()` | Retorna o maior elemento de uma sequência. |
| `memoryview()` | Cria uma nova visualização de memória. |
| `min()` | Retorna o menor elemento de uma sequência. |
| `next()` | Retorna o próximo elemento de um iterador. |
| `object()` | Cria um novo objeto. |
| `oct()` | Retorna um string representando a representação octal de um número. |
| `open()` | Abre um arquivo. |
| `ord()` | Retorna o código ASCII de um caractere. |
| `pow()` | Retorna a potência de um número. |
| `print()` | Imprime um string no console. |
| `property()` | Cria uma nova propriedade. |
| `range()` | Cria um novo iterador que gera uma sequência de números. |
| `repr()` | Retorna a representação de um objeto. |
| `reversed()` | Retorna um iterador que gera os elementos de uma sequência em ordem inversa. |
| `round()` | Arredonda um número. |
| `set()` | Cria um novo conjunto. |
| `setattr()` | Define o valor de um atributo de um objeto. |
| `slice()` | Cria um novo objeto de fatiamento. |
| `sorted()` | Retorna uma lista ordenada dos elementos de uma sequência. |
| `staticmethod()` | Cria um novo método estático. |
| `str()` | Converte um objeto para um string. |
| `sum()` | Retorna a soma dos elementos de uma sequência. |
| `super()` | Retorna o objeto superclasse de um objeto. |
| `tuple()` | Cria uma nova tupla. |
| `type()` | Retorna o tipo de um objeto. |
| `vars()` | Retorna um dicionário com as variáveis de um objeto. |
| `zip()` | Retorna um iterador que gera tuplas contendo os elementos de duas ou mais sequências. |