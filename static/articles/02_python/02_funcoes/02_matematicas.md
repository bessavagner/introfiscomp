# Funções matemáticas (pacote _math_)

Além das funções built-ins padrão, o Python oferece o pacote math, que contém uma ampla gama de funções matemáticas mais avançadas.

Para utilizar as funções do pacote math, você precisa importá-lo primeiro usando a declaração  `impor math`.

```
import math
```

## Função sqrt()

A função sqrt() é usada para calcular a raiz quadrada de um número. Por exemplo:

```
import math

raiz_quadrada = math.sqrt(25)
print(raiz_quadrada)  # Saída: 5.0
```

Outras funções matemáticas

O pacote math oferece uma variedade de outras funções matemáticas úteis, incluindo:

- `math.sin(x)`: Retorna o seno de x (em radianos).
- `math.cos(x)`: Retorna o cosseno de x (em radianos).
- `math.tan(x)`: Retorna a tangente de x (em radianos).
- `math.exp(x)`: Retorna o valor de e elevado à potência de x.
- `math.log(x)`: Retorna o logaritmo natural de x.
- `math.pow(x, y)`: Retorna x elevado à potência de y.
- `math.factorial(x)`: Retorna o fatorial de x.

Exemplos

```
print(math.sin(math.pi / 2))    # Saída: 1.0 (seno de 90 graus)
print(math.exp(2))               # Saída: 7.38905609893065 (e elevado à potência de 2)
print(math.log(10))              # Saída: 2.302585092994046 (logaritmo natural de 10)
print(math.pow(2, 3))            # Saída: 8.0 (2 elevado à potência de 3)
print(math.factorial(5))         # Saída: 120 (fatorial de 5)
```
Essas são apenas algumas das funções disponíveis no <a href="https://docs.python.org/pt-br/3/library/math.html">pacote math</a>. Você pode consultar a documentação oficial do Python para obter uma lista completa e detalhada de todas as funções oferecidas por este pacote.
