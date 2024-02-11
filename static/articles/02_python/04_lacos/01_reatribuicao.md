# Reatribuição de variáveis

A reatribuição de variáveis é um conceito importante em Python, onde você pode atribuir um novo valor a uma variável existente. Isso é útil quando você precisa atualizar o valor de uma variável com base em cálculos ou outras operações.

Por exemplo, vamos supor que você tenha uma variável chamada `idade` que armazena a idade de uma pessoa. Se você quiser atualizar essa idade para refletir o próximo ano, você pode fazer isso facilmente reatribuindo o valor da variável `idade`:

```
idade = 25
print("Idade atual:", idade)

# Atualizando a idade para o próximo ano
idade = idade + 1
print("Idade no próximo ano:", idade)
```

Neste exemplo, inicializamos a variável idade com o valor 25 e depois a atualizamos para refletir a idade no próximo ano, adicionando 1 ao valor atual da idade.

## Atualização com operadores de atribuição combinada

Além disso, Python oferece operadores de atribuição combinada, que permitem atualizar uma variável de forma mais concisa. Por exemplo, o código acima pode ser reescrito usando o operador +=:

```
idade = 25
print("Idade atual:", idade)

# Atualizando a idade para o próximo ano usando operador de atribuição combinada
idade += 1
print("Idade no próximo ano:", idade)
```

Este código produz o mesmo resultado que o exemplo anterior, mas de uma forma mais compacta.

