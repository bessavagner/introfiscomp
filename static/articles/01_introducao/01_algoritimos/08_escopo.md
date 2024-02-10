# Escopo de Variáveis

As variáveis em um programa têm diferentes escopos, determinando onde elas podem ser acessadas e modificadas. No exemplo anterior, a variável USUARIO e SENHA são globais, pois são definidas fora de qualquer função ou classe, e podem ser acessadas por qualquer "sub escopo", como o escopo principal, enquanto as variáveis usuario, senha, e saldo dentro da classe Conta têm escopo local à classe.
Escopo global

## O escopo global

Este é o escopo mais externo de um programa. Variáveis declaradas no escopo global são visíveis em todo o programa, desde que não haja outra variável com o mesmo nome declarada em um escopo interno.

```
programa banco
// Variáveis declaradas no escopo global
USUARIO = '01892299'
SENHA = '123456'
início
    // escopo principal
fim
```


## Escopo principal

O escopo principal é o escopo do bloco de código que inicia o programa. Variáveis declaradas no escopo principal só podem ser acessadas a partir desse bloco de código.


```
programa banco

// Variáveis declaradas no escopo principal
Início
    nova_conta = Conta(USUARIO, SENHA, 0)
    valor = nova_conta.saldo
    saque = encerrarConta(nova_conta)
Fim

```
## Visibilidade de variáveis

A visibilidade de uma variável é determinada pelo seu escopo. Variáveis declaradas no mesmo escopo são visíveis umas para as outras. Variáveis declaradas em escopos diferentes não são visíveis umas para as outras, a menos que sejam declaradas como `public`.

// Variáveis declaradas no mesmo escopo são visíveis umas para as outras
USUARIO, SENHA, nova_conta

## Regras de escopo

As regras de escopo são as seguintes:

- Uma variável só pode ser declarada uma vez em um determinado escopo.
- Uma variável declarada em um escopo interno não pode ser acessada a partir de um escopo externo.
- Uma variável declarada em um escopo externo pode ser acessada a partir de um escopo interno.

## Exemplo 1: Variáveis de escopo em uma função

Aqui está um exemplo de como variáveis de escopo podem ser usadas em uma função:

```
Programa fatorial
// Função que calcula o fatorial de um número
Função fatorial(n):
    // Variável declarada no escopo interno da função
    resultado = 1
    // Laço for que itera de 1 até n
    para i = 1 até n:
        // Atualiza o valor da variável `resultado`
        resultado = resultado * i
    // Retorna o valor da variável `resultado`
    retorna resultado
Fim Função

Início
    resultado = fatorial(3)
    escreva(resultado) // será exibido o valor 6
Fim
```

Neste exemplo, a função `fatorial()` tem um escopo interno. A variável `resultado` é declarada no escopo interno da função. Isso significa que ela só pode ser acessada a partir da função `fatorial()`. Por isso no escopo principal podemos definir uma variávelde mesmo nome, pois ambas pertencem a escopos diferentes 