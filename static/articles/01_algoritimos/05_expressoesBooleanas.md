# Expressões Booleanas

As expressões booleanas são fundamentais em programação para avaliar se uma condição é verdadeira ou falsa.

Elas são compostas por operandos e operadores booleanos. Os operandos podem ser variáveis ou constantes, e os operadores booleanos são símbolos que indicam a operação a ser realizada.

Por exemplo, a seguinte expressão booleana avalia se a variável <code>x</code> é maior que 10:


```
x > 10
```

 O resultado da expressão acima é um valor do tipo <strong>booleano</strong>, ou seja, lógico. Neste exemplo acima, se <strong>x</strong> for um número positivo, então a expressão é avaliada como <strong>Verdadeiro</strong>; se <strong>x</strong> for negativo, o resultado é <strong>Falso</strong>. Dados booleanos são fundamentais para avaliação de expressões condicionais. Esses valores são utilizados para controlar o fluxo do programa em estruturas condicionais.

Seguem aqui mais alguns exemplos

```
// Expressão booleana simples
// Qual será o valor armazenado em `é_maior_de_idade`?
idade = 18
é_maior_de_idade = idade >= 18
```

```
// Uso de operadores lógicos
nota = 75
frequencia = 0.8
passou = nota >= 60 E frequencia >= 0.75
```

## Tabela Verdade do Operador E

| Operando 1 | Operando 2 | Resultado  |
| ---------- | ---------- | ---------- |
| Verdadeiro | Verdadeiro | Verdadeiro |
| Verdadeiro | Falso      | Falso      |
| Falso      | Verdadeiro | Falso      |
| Falso      | Falso      | Falso      |

## Tabela Verdade do Operador OU

| Operando 1 | Operando 2 | Resultado  |
| ---------- | ---------- | ---------- |
| Verdadeiro | Verdadeiro | Verdadeiro |
| Verdadeiro | Falso      | Verdadeiro |
| Falso      | Verdadeiro | Verdadeiro |
| Falso      | Falso      | Falso      |
