# Herança

A herança é um dos pilares fundamentais da programação orientada a objetos (POO) em Python. Ela permite que uma classe herde atributos e métodos de outra classe, facilitando a reutilização de código e a organização do mesmo. Em Python, a herança é implementada através do uso da palavra-chave `class` seguida pelo nome da *classe derivada* e da *classe base*, separadas por uma vírgula.

## Por que Usar Herança?

A herança é útil por várias razões:

- Reutilização de Código: Ao herdar de uma classe base, a classe derivada pode reutilizar os atributos e métodos definidos na classe base, economizando tempo e esforço na reescrita de código.
- Organização do Código: A herança ajuda a organizar o código, agrupando classes relacionadas em uma hierarquia. Isso torna o código mais fácil de entender e manter.
- Encapsulamento: A herança permite que a classe derivada esconda os detalhes de implementação da classe base, expondo apenas os métodos e propriedades necessários. Isso é conhecido como encapsulamento e ajuda a proteger os dados da classe base de serem acessados ou modificados de maneira inadequada.

## Definição de uma Classe Base e uma Classe Derivada

Vamos definir uma classe base para partículas pontuais:


``` python
class Particula:
    def __init__(self, massa, carga, r):
        self.massa = massa
        self.carga = carga
        self.posicao = r
```

Agora vamos criar duas classes derivadas de `Particula`:

``` python

class Eletron(Particula):
    def __init__(self, r):
        super().__init__(9.11e-31, -1.6e-19, r)
```

``` python

class Proton(Particula):
    def __init__(self, r):
        super().__init__(1.67e-27, 1.6e-19, r)
```

Vamos usar isto de exemplo para a utilidade da herança de classes. Suponha que você quisesse criar um objeto que representa um elétron, usando a classa `Partícula`:

``` python
massa = 9.11e-31
carga = -1.6e-19
posicao_inicial = 8
eletron = Particula(massa, carga, posicao_inicial)
```

Note que sempre que quiser criar um objeto que represente um elétron, você deve passar o valor da carga. Mas com a classe derivada `Eletron` acima, não precisamos, pois ela já é implementada de forma a criar um objeto de `Particula` com o valor de massa `9.11e-31` de carga `-1.6e-19`:

``` python
posicao_inicial = 8
eletron = Eletron(posicao_inicial)
```

Isso deixa o código mais limpo, enxuto e compreensível. Isso é possível pois dentro do contrutor da classe derivada (`Eletron`) chamamos o construtor da classe base (`Particula`) usando a função especial `super`. A linha

``` python
super().__init__(9.11e-31, -1.6e-19, r)
```

Fala ao interpretador para criar uma instância da classe base, que serve de... BASE para criar uma instância da classe derivada.