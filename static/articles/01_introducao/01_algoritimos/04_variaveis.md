# Variáveis

As variáveis são elementos fundamentais em programação, sendo utilizadas para armazenar dados em um programa. Uma variável é um nome que representa um valor, e esse valor pode ser modificado durante a execução do programa.

## Exemplos de declaração de variáveis

```
// Declaração e atribuição de uma variável **inteira**
var idade = 25

// Declaração e atribuição de uma variável **real**
var preco = 15.99
var desconto = 5.0
var preco_final = preco - desconto

// Declaração e manipulação de uma variável **texto**
var nome = "Maria"
var sobrenome = "Silva"
// Qual o valor que será atribuído à variável `nome_completo`?
var nome_completo = nome + " " + sobrenome
```

Nas linguagens de programação chamadas _tipadas_, como C++, é necessário declarar o tipo de variável. As declarações de variáveis também podem ser indicadas por palavras-chave declaradoras, como `var`, `let` e `const` em Javascript. Há também as linguagens não tipadas, como o Python, na qual as declarações não requerem nem uma palavra-chave declaradora nem a identificação do tipo. E será essa regra que vamos usar na sintaxe de nosso pseudocódigo. Neste caso, os exemplos acima devem ser para nosso pseudocódigo:

```
idade = 25
preco = 15.99
desconto = 5.0
preco_final = preco - desconto
nome = "Maria"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome
```

## Regras para nomes das variáveis

Detre outras regras listadas a seguir, vamos tornar nosso código sensível às maiúsculas, o que quer dizer que `NOME` é diferente de `nome`.

As regras são:

1. **Nome da regra:** Os nomes das variáveis devem ser **significativos** e refletir o seu conteúdo. _Exemplos:_ `idade`, `preco`, `nome`, `sobrenome`.
2. **Nome da regra:** Os nomes das variáveis não devem conter espaços ou caracteres especiais. _Exemplos:_ `idade_cliente`, `preco_produto` (_corretos_); `idade cliente`, `preco-produto` (_incorretos_).
3. **Nome da regra:** Os nomes das variáveis não devem começar com números. _Exemplos:_ `idade_cliente` (_correto_); `2idade_cliente` (_incorreto_).
4. **Nome da regra:** Os nomes das variáveis devem ser escritos em letras minúsculas. _Exemplos:_ `idade_cliente` (_correto_); `IdadeCliente` (_incorreto_).
5. **Nome da regra:** Os nomes das variáveis devem ser curtos e fáceis de lembrar. _Exemplos:_ `idade` (_correto_); `idade_do_cliente` (_incorreto_).

## Tipos de variáveis

Os tipos de variáveis são:

- **Inteiras:** Armazenam números inteiros, como 1, 2, 3, 4, 5, etc.
- **Reais:** Armazenam números reais, como 1.5, 2.5, 3.5, 4.5, 5.5, etc.
- **Texto:** Armazenam textos, como "Maria", "Silva", "São Paulo", etc.
- **Lógicas:** Armazenam valores booleanos, como `verdadeiro` ou `falso`.

## Escopo das variáveis

O escopo de uma variável é o trecho do código onde ela pode ser utilizada. Existem dois escopos principais:

- **Escopo local:** Uma variável declarada dentro de uma função ou bloco de código só pode ser utilizada dentro daquele escopo.
- **Escopo global:** Uma variável declarada fora de qualquer função ou bloco de código pode ser utilizada em qualquer lugar do programa.

## Operadores de atribuição

Os operadores de atribuição são utilizados para atribuir valores às variáveis. Os principais operadores de atribuição são:

- **=:** Atribui o valor da expressão à direita do operador à variável à esquerda do operador. _Exemplo:_ `idade = 25`.
- **+=:** Adiciona o valor da expressão à direita do operador ao valor da variável à esquerda do operador. _Exemplo:_ `idade += 1`.
- **-=:** Subtrai o valor da expressão à direita do operador ao valor da variável à esquerda do operador. _Exemplo:_ `idade -= 1`.
- ***=:** Multiplica o valor da expressão à direita do operador pelo valor da variável à esquerda do operador. _Exemplo:_ `idade *= 2`.
- **/=:** Divide o valor da expressão à direita do operador pelo valor da variável à esquerda do operador. _Exemplo:_ `idade /= 2`.

## Operadores de comparação

Os operadores de comparação são utilizados para comparar o valor de duas variáveis ou expressões. Os principais operadores de comparação são:

- **==:** Igual. _Exemplo:_ `idade == 25`.
- **!=:** Diferente. _Exemplo:_ `idade != 25`.
- **>:** Maior que. _Exemplo:_ `idade > 25`.
- **>=:** Maior ou igual a. _Exemplo:_ `idade >= 25`.
- **<:** Menor que. _Exemplo:_ `idade < 25`.
- **<=:** Menor ou igual a. _Exemplo:_ `idade <= 25`.
