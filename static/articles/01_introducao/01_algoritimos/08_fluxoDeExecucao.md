# Fluxo de Execução

O fluxo de execução de um algoritmo é a sequência de etapas que ele segue para resolver um problema.

Normalmente, o fluxo de execução de um algoritmo, código ou programa é sequencial e em série, isto é, cada comando é executado após o outro, e somente após o anterior ser finalizado.

Em pseudo código, podemos, conceitualmente, separar um código em dois escopos: escopo global e escopo principal.

- Global: define "sub programas", também chamado de subrotinas, ou define dados ou estruturas globais de dados, como classes.
- Principal: define a execução principal do programa. É onde a "leitura" do programa se inicia.

## Exemplo 1: Fluxo de Execução em um Algoritmo de Conta Bancária

```
// Pseudocódigo para um algoritmo simples de conta bancária

// escopo global
USUARIO = '01892299'

SENHA = '123456'

Classe Conta(u, se, sa):
 
    usuario = u
    senha = se
    saldo = sa

    Função depositar(valor):
        classe.saldo = classe.saldo + valor
    Fim Função

    Função sacar(valor, u, se):
        se u == classe.usuario E se == classe.senha:
            classe.saldo = classe.saldo - valor
            retorna valor
        se não:
            retorna ErroDeValidação
    Fim Função

    Função verificarSaldo(u, se):
        se u == classe.usuario E se == classe.senha:
            retorna classe.saldo
        se não:
            retorna ErroDeValidação
    Fim Função
Fim Classe

Função encerrarConta(conta):
    valor = conta.saldo
    saque = conta.sacar(valor)
    delete conta  // apaga a variável conta
    retorna saque
    Fim Função

// escopo principal
Início
    nova_conta = Conta(USUARIO, SENHA, 0)
    escreva(nova_conta.saldo) // resultado: 0
    nova_conta.depositar(100)
    escreva(nova_conta.verificarSaldo()) // resultado: 100
    sacar(50, USUARIO, SENHA)
    escreva(nova_conta.verificarSaldo()) // resultado: 50
    saque = encerrarConta(nova_conta, USUARIO, SENHA)
    escreva(nova_conta.verificarSaldo()) // dá erro pois a variável `conta` foi deletada
Fim
```

Nesse algoritmo, o fluxo de execução é o seguinte:

1. No escopo global, são definidas as variáveis `USUARIO` e `SENHA`, que serão usadas para autenticação nas operações bancárias. Também é definida a classe `Conta`, que representa uma conta bancária com os atributos `usuario`, `senha`, `saldo` e os métodos `depositar()`, `sacar()` e `verificarSaldo()`.
2. No escopo principal, é criada uma nova conta bancária usando a classe `Conta`.
3. O saldo da nova conta é exibido na tela (resultado: 0).
4. É feito um depósito de 100 reais na conta.
5. O saldo da conta é exibido novamente na tela (resultado: 100).
6. É feita uma retirada de 50 reais da conta, usando a função `sacar()`.
7. O saldo da conta é exibido novamente na tela (resultado: 50).
8. É encerrada a conta bancária usando a função `encerrarConta()`, que retorna o saldo da conta após o encerramento.
9. É exibido na tela o saldo da conta encerrada (dá erro, pois a variável `conta` foi deletada).

O fluxo de execução desse algoritmo é fácil de acompanhar, pois as etapas são executadas em ordem sequencial. No entanto, existem algoritmos mais complexos, nos quais o fluxo de execução pode ser mais difícil de entender. Nesses casos, é importante usar diagramas de fluxo ou outras técnicas de visualização para ajudar a entender o fluxo de execução do algoritmo.
