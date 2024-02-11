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
nota = 85
if nota >= 90:
    print("Aprovado com louvor!")
elif nota >= 70:
    print("Aprovado")
else:
    print("Reprovado")
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
