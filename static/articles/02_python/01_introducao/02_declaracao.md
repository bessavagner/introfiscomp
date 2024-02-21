# Declarações

Esta seção trata de conceitos estruturais da linguagem Python.

Assim como em qualquer outra linguagem, a escrita de um programa é a composição de diversas declarações, que não textos que seguem a regra sintática da linguagem em questão.

As declarações definem estruturas de execuções as quais ficam a cargo do interpretador coverter para código de máquina a fim de serem executadas.

Nesta seção vamos conferir declarações básicas de variáveis e operações.

Em Python, as declarações são usadas para dizer ao interpretador o que fazer. Existem diferentes tipos de declarações, incluindo:

## Atribuições:

As declarações de atribuição são usadas para atribuir um valor a uma variável.

### Exemplos

``` python
massa = 10
aceleracao = 2
```

Isso significa que a variável `x` agora contém o valor 10. Você pode usar a variável `x` em qualquer lugar do seu programa para se referir a esse valor.

## Declarações de função

As declarações de função são usadas para definir funções. Uma função é um bloco de código que pode ser reutilizado em diferentes partes do seu programa. Por exemplo, a seguinte declaração define uma função chamada `forca()` que aceita dois argumentos, `massa` e `aceleracao` e retorna a força:

```
def forca(massa, aceleracao):
  return massa * aceleracao
```

Isso significa que você pode usar a função `forca()` em qualquer lugar do seu programa para a força sobre uma partícula, das sua massa e sua aceleração. Por exemplo, o seguinte código usa a função `forca()` para uma partícula de 10 quilogramas e com aceleração de 2 metros por segundo ao quadrado, e então armazenar o resultado na variável `resultante`:

```
resultante = forca(1, 2)
```

Agora a variável `resultante` contém o valor 3.

## Declarações de classe

As declarações de classe são usadas para definir classes. Uma classe é um modelo para criar objetos. Por exemplo, a seguinte declaração define uma classe chamada `Pessoa` que tem dois atributos, `nome` e `idade`:

``` python
class Particula:
  def __init__(self, massa, posicao):
    self.massa = massa
    self.posicao = posicao
```

Isso significa que você pode usar a classe `Particula` para criar objetos que representam pessoas. Por exemplo, o seguinte código usa a classe `Particula` para criar dois objetos, `particula1` e `particula2`:

```
particula1 = Particula(9.11, 0)
particula2 = Particula(1.67, 1)
```

Agora os objetos `particula1` e `particula2` contêm informações sobre duas particulas diferentes. Você pode usar esses objetos no seu programa para acessar essas informações.

## Instruções condicionais

As instruções condicionais são usadas para controlar o fluxo de execução do seu programa. Elas permitem que você execute diferentes blocos de código dependendo de certas condições. Por exemplo, a seguinte instrução condicional verifica se o valor da variável `x` é maior que 10 e, se for, imprime a mensagem "x é maior que 10":

```
if x > 10:
  print("x é maior que 10")
```

Você também pode usar instruções condicionais para executar diferentes blocos de código dependendo de várias condições. Por exemplo, a seguinte instrução condicional verifica se o valor da variável `x` é maior que 10 e se o valor da variável `y` é menor que 20, e se ambas as condições forem atendidas, imprime a mensagem "x é maior que 10 e y é menor que 20":

```
if x > 10 and y < 20:
  print("x é maior que 10 e y é menor que 20")
```

#****# Instruções de repetição

As instruções de repetição são usadas para executar um bloco de código várias vezes. Por exemplo, a seguinte instrução de repetição usa um loop `for` para imprimir os números de 1 a 10:

```
for i in range(1, 11):
  print(i)
```

Isso imprime os números 1, 2, 3, ..., 10.

Você também pode usar instruções de repetição para executar um bloco de código enquanto uma determinada condição for atendida. Por exemplo, a seguinte instrução de repetição usa um loop `while` para imprimir os números de 1 a 10, mas para de imprimir quando o valor da variável `i` atinge 5:

```
i = 1
while i <= 10:
  print(i)
  i += 1
```

Isso imprime os números 1, 2, 3, 4, 5.