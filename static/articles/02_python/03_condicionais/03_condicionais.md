# Estrutura de execução condicional

As estruturas condicionais são cruciais para direcionar o fluxo de execução do programa com base em condições.

## Estrutura if

Utilizada para executar um bloco de código apenas se uma condição for verdadeira.

```
idade = 20
if idade >= 18:
    print("Você tem permissão para dirigir.")
```

## Estrutura if-else

Permite executar um bloco de código se a condição for verdadeira e outro bloco se for falsa.

```
saldo = 500
saque = 600
if saldo >= saque:
    print("Saque realizado com sucesso!")
else:
    print("Saldo insuficiente.")
```

## Estrutura if-elif-else

Usada para avaliar múltiplas condições de forma sequencial.

```
cut_off = 0.1
distance = 0.4
if distance >= cut_off:
    print("Calcular força")
elif distance < cut_off and distance > 0:
    print("A força é zero")
else:
    print("Erro de calculo! Distância não pode ser menor ou igual a zero.")
```

### Aninhamento de condicionais

Consiste em colocar uma estrutura condicional dentro de outra, permitindo criar lógicas mais complexas.

```
hora = 11
if hora < 12:
    print("Bom dia!")
    if hora < 6:
        print("Ainda está muito cedo.")
    else:
        print("Hora de se preparar para o dia.")
elif hora < 18:
    print("Boa tarde!")
else:
    print("Boa noite!")
```

Estes exemplos ilustram como os operadores relacionais e lógicos, juntamente com as estruturas condicionais, são fundamentais para a lógica de programação, permitindo a criação de programas que podem tomar decisões e executar ações com base em condições específicas.
