# Expressões Aritméticas

As expressões aritméticas são uma ferramenta fundamental na programação, permitindo realizar cálculos matemáticos e manipular dados numéricos.

Elas são compostas por operandos e operadores, onde os operandos são os números ou variáveis envolvidos na operação, e os operadores são os símbolos que indicam a operação a ser realizada.

## Exemplos de Expressões Aritméticas

```
// Adição
x = 10 + 20; // x = 30

// Subtração
y = 15 - 5; // y = 10

// Multiplicação
z = 3 * 4; // z = 12

// Divisão
w = 20 / 5; // w = 4

// Resto da divisão
r = 17 % 5; // r = 2

// Potenciação
p = 2 ** 3; // p = 8
```

## Ordem de Precedência

Quando uma expressão aritmética contém operações com precedência diferente, a ordem na qual elas são realizadas é definida pela regra de precedência. A ordem de precedência padrão é a seguinte:

1. <strong>Parênteses</strong> Os parênteses têm a maior precedência, o que significa que as operações dentro dos parênteses são sempre realizadas primeiro.
2. <strong>Potenciação</strong> A potenciação tem a segunda maior precedência, depois dos parênteses.
3. <strong>Multiplicação e Divisão</strong> A multiplicação e a divisão têm a mesma precedência e são realizadas da esquerda para a direita.
4. <strong>Adição e Subtração</strong> A adição e a subtração têm a menor precedência e são realizadas da esquerda para a direita.

Por exemplo, na expressão `10 + 20 * 3`, a multiplicação é realizada primeiro, resultando em 60, e depois a adição é realizada, resultando em 70.

## Operações Especiais

Existem algumas operações aritméticas especiais que são usadas com frequência na programação:

- <strong>Resto da Divisão (Módulo)</strong> O operador de resto da divisão, representado por `%` ou `mod`, retorna o resto da divisão de dois números. Por exemplo, `17 % 5` é igual a 2, porque 17 dividido por 5 é igual a 3 com resto 2.
- <strong>Divisão Inteira</strong> O operador de divisão inteira, representado por `//` ou `div`, retorna o resultado da divisão de dois números, arredondado para o inteiro mais próximo. Por exemplo, `17 // 5` é igual a 3, porque 17 dividido por 5 é igual a 3,4, que arredondado para o inteiro mais próximo é 3.
