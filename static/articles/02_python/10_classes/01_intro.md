# Introdução às Classes

As classes são um dos pilares fundamentais da programação orientada a objetos (POO) em Python. A POO é um paradigma de programação que enfatiza a criação de objetos que contêm tanto dados quanto métodos para manipular esses dados. Em Python, as classes são definidas usando a palavra-chave class, seguida pelo nome da classe e dois pontos

## Por que Usar Classes?

As classes são úteis por várias razões:

- **Reutilização de Código**: As classes permitem que você defina um modelo para criar objetos com propriedades e comportamentos específicos. Isso significa que você pode reutilizar o mesmo modelo para criar vários objetos, economizando tempo e esforço.
- **Organização do Código**: As classes ajudam a organizar o código, agrupando dados e métodos relacionados em uma única estrutura. Isso torna o código mais fácil de entender e manter.
- **Encapsulamento**: As classes permitem que você esconda os detalhes de implementação de um objeto, expondo apenas os métodos e propriedades necessários. Isso é conhecido como encapsulamento e ajuda a proteger os dados do objeto de serem acessados ou modificados de maneira inadequada.

## Definição de uma Classe

Aqui está um exemplo simples de como definir uma classe em Python:

``` python
class Particula:
    def __init__(self, massa, carga):
        self.massa = massa
        self.carga = carga

    def calcular_forca(self, aceleracao):
        return self.massa*aceleracao

    def calcular_campo_eletrico(self, r):
        return 9e9*self.carga/r**2
```

Neste exemplo, `Particula` é o nome da classe. A função `__init__` é um método especial chamado construtor, que é chamado automaticamente quando um objeto é criado a partir da classe. Os parâmetros massa e carga são passados para o construtor. O parâmetro self é uma referência ao objeto que está sendo criado e é usado para acessar as propriedades e métodos do objeto, mas não precisa ser fornecido ao se criar um objeto.

## Criando Objetos

Para criar um objeto a partir de uma classe, você usa o nome da classe seguido por parênteses e passa os argumentos necessários para o construtor:

``` python
eletron = Particula(9.11e-31, -1.6e-19)
proton = Particula(1.67e-27, 1.6e-19)
```

## Acessando Propriedades e Métodos

Você pode acessar as propriedades e métodos de um objeto usando a notação de ponto:

``` python
print(eletron.massa)
print(proton.carga)

print(eletron.calcular_campo_eletrico(8e-9))
```

## Exemplos

### Classe para Representar uma Partícula em Movimento

Em física, partículas em movimento podem ser descritas por suas posições e velocidades. Vamos criar uma classe ParticulaEmMovimento que inclui métodos para calcular a posição final de uma partícula após um determinado tempo, considerando uma aceleração constante.

``` python
class ParticulaEmMovimento:
    def __init__(self, posicao_inicial, velocidade_inicial, aceleracao):
        self.posicao_inicial = posicao_inicial
        self.velocidade_inicial = velocidade_inicial
        self.aceleracao = aceleracao

    def calcular_posicao_final(self, tempo):
        posicao_final = self.posicao_inicial + self.velocidade_inicial * tempo + 0.5 * self.aceleracao * tempo**2
        return posicao_final
```

### Classe para Representar um Vetor

Até o momento temos usado listas ou tuplas para representar um vetor na computação. Com o uso da POO podemos criar uma classe que se comporta exatamente como um vetor na matemática.

Para isso vamos falar de algumas funções especiais: `__add__`, `__sub__` e `__str__`. Estas funções são métodos especiais em Python que permitem que os objetos de uma classe se comportem de maneira personalizada quando são usados com operadores específicos ou quando são convertidos para strings. Vamos explorar cada uma dessas funções:

- `__add__`

O método `__add__` é chamado quando o operador + é usado com objetos da classe. Ele permite que você defina o comportamento de adição personalizado para os objetos da sua classe. Por exemplo, se você tem uma classe Vetor que representa vetores em um espaço tridimensional, você pode definir o método `__add__` para adicionar dois vetores componentemente.

``` python
class Vetor:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vetor(self.x + other.x, self.y + other.y, self.z + other.z)
```

Neste exemplo, quando você adiciona dois objetos Vetor usando o operador +, o método `__add__` é chamado, e ele retorna um novo objeto Vetor cujos componentes são a soma dos componentes dos dois vetores.

- `__sub__`

O método `__sub__` é chamado quando o operador - é usado com objetos da classe. Ele permite que você defina o comportamento de subtração personalizado para os objetos da sua classe. Similar ao método `__add__`, você pode definir o método `__sub__` para subtrair dois vetores componentemente.

``` python
class Vetor:
    # ...
    def __sub__(self, other):
        return Vetor(self.x - other.x, self.y - other.y, self.z - other.z)
```

Neste exemplo, quando você subtrai dois objetos Vetor usando o operador -, o método `__sub__` é chamado, e ele retorna um novo objeto Vetor cujos componentes são a diferença dos componentes dos dois vetores.

- `__str__`

O método `__str__` é chamado quando você tenta converter um objeto da sua classe em uma string usando a função `str()` ou quando o objeto é impresso usando a função `print()`. Ele permite que você defina uma representação em string personalizada para os objetos da sua classe.

``` python
class Vetor:
    # ...
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
```

Neste exemplo, quando você tenta converter um objeto Vetor em uma string ou imprimi-lo, o método __str__ é chamado, e ele retorna uma string que representa o vetor no formato (x, y, z).

Esses métodos especiais são uma parte importante da programação orientada a objetos em Python, pois permitem que você personalize o comportamento dos objetos da sua classe para se encaixar melhor no contexto do seu programa. Segue a classe `Vetor` na íntegra:

``` python
class Vetor:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def magnitude(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def __add__(self, other):
        return Vetor(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vetor(self.x - other.x, self.y - other.y, self.z - other.z)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
```