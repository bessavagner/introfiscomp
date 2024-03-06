# Exemplos e aplicações

## Introdução


## Exemplo 1: Calculadora de Raízes Quadráticas

Um cenário comum em matemática é o cálculo de raízes quadráticas. A fórmula para encontrar as raízes de uma equação quadrática é `x = (-b ± sqrt(b^2 - 4ac)) / (2a)`. No entanto, essa fórmula não é válida se `b^2 - 4ac` for menor que zero, pois o resultado de `sqrt(b^2 - 4ac)` seria um número imaginário, o que não é suportado por muitas aplicações práticas.

``` python
import math

def calcular_raizes_quadraticas(a, b, c):
    try:
        discriminante = b**2 - 4*a*c
        if discriminante < 0:
            raise ValueError("O discriminante é negativo, raízes imaginárias não suportadas.")
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return x1, x2
    except ValueError as e:
        print(e)
        return None

# Exemplo de uso
raizes = calcular_raizes_quadraticas(1, -3, 2)
if raizes:
    print(f"As raízes são {raizes[0]} e {raizes[1]}")
```

## Exemplo 2: Cálculo de Velocidade em Física

Em física, é comum calcular a velocidade de um objeto em movimento. A velocidade é a distância percorrida dividida pelo tempo. No entanto, se o tempo for zero, a velocidade seria indefinida, o que não é uma situação válida em muitos contextos físicos.

``` python
def calcular_velocidade(distancia, tempo):
    try:
        if tempo == 0:
            raise ZeroDivisionError("O tempo não pode ser zero.")
        velocidade = distancia / tempo
        return velocidade
    except ZeroDivisionError as e:
        print(e)
        return None

# Exemplo de uso
velocidade = calcular_velocidade(10, 2)
if velocidade:
    print(f"A velocidade é {velocidade} metros por segundo.")
```

## Exemplo 3: Cálculo de Energia em Física

A energia cinética de um objeto em movimento pode ser calculada pela fórmula `E = 1/2 * m * v^2`, onde `E` é a energia, `m` é a massa e `v` é a velocidade. No entanto, se a massa ou a velocidade forem negativas, a energia cinética seria negativa, o que não é uma situação física válida.

``` python
def calcular_energia_cinetica(massa, velocidade):
    try:
        if massa < 0 or velocidade < 0:
            raise ValueError("Massa e velocidade devem ser positivas.")
        energia = 0.5 * massa * velocidade**2
        return energia
    except ValueError as e:
        print(e)
        return None

# Exemplo de uso
energia = calcular_energia_cinetica(2, 3)
if energia:
    print(f"A energia cinética é {energia} joules.")
```


Exceções em Python são uma ferramenta essencial para lidar com erros e condições inesperadas em aplicações matemáticas e físicas. Ao usar exceções, podemos escrever código que não apenas funciona corretamente, mas também é robusto e confiável, capaz de lidar com uma ampla gama de situações, incluindo entradas inválidas ou condições físicas impossíveis.
