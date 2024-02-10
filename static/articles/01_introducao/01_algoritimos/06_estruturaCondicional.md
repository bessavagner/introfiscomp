# Estrutura Condicional

A estrutura condicional é um componente fundamental na programação, permitindo que o fluxo de execução de um programa seja alterado com base na avaliação de condições.

Ela é composta por blocos condicionais como Se, Senão Se e Senão, que permitem a execução de diferentes conjuntos de instruções dependendo do resultado de expressões booleanas.

## Blocos condicionais mais comuns

- **Se**: Este bloco é utilizado para verificar uma condição booleana e, se for verdadeira, executar um conjunto de instruções.
- **Senão Se**: Este bloco é utilizado para verificar outra condição booleana e, se for verdadeira, executar um conjunto de instruções. Ele é utilizado em conjunto com o bloco Se.
- **Senão**: Este bloco é utilizado para executar um conjunto de instruções se nenhuma das condições anteriores for verdadeira. Ele é utilizado em conjunto com os blocos Se e Senão Se.

## Exemplos

```
// Verificação de maioridade
idade = 17
Se idade >= 18 então
    escreva("É maior de idade.")
Fim Se
```

Neste exemplo, a variável `idade` é verificada para determinar se o valor é maior ou igual a 18 anos. Se esta condição for verdadeira, a instrução `escreva("É maior de idade.")` será executada, exibindo uma mensagem no console.

```
// Classificação de notas
nota = 75
Se nota >= 90 então
    escreva("Excelente!")
Senão Se nota >= 70 E nota < 90 então
    escreva("Bom trabalho.")
Senão
    escreva("Precisa melhorar.")
Fim Se
```

Neste exemplo, a variável `nota` é verificada para determinar a classificação da nota. Se a nota for maior ou igual a 90, a mensagem "Excelente!" será exibida. Se a nota for maior ou igual a 70 e menor que 90, a mensagem "Bom trabalho." será exibida. Caso nenhuma das condições anteriores seja verdadeira, a mensagem "Precisa melhorar." será exibida.

```
// Verificação de números e suas características
numero = -5
Se numero > 0 E numero mod 2 = 0 então
    escreva("Número positivo e par.")
Senão Se numero > 0 E numero mod 2 ≠ 0 então
    escreva("Número positivo e ímpar.")
Senão Se numero < 0 OU numero = 0 então
    escreva("Número negativo ou zero.")
Fim Se
```

Neste exemplo, a variável `numero` é verificada para determinar suas características. Se o número for maior que 0 e par, a mensagem "Número positivo e par." será exibida. Se o número for maior que 0 e ímpar, a mensagem "Número positivo e ímpar." será exibida. Se o número for menor que 0 ou igual a 0, a mensagem "Número negativo ou zero." será exibida.

Na linguagem de pseudocódigo utilizada nos exemplos, a expressão `escreva()` é utilizada para exibir mensagens ou resultados na saída do programa. Pode ser interpretada como uma instrução para imprimir ou mostrar informações no console, dependendo do contexto de execução.
