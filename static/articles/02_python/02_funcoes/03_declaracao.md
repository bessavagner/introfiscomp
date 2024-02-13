# Declaração e chamada de funções

## Criando funções

Além de utilizar funções built-ins, podemos criar nossas próprias funções personalizadas para encapsular lógicas específicas e reutilizáveis.

## Argumentos (ou parâmtros) posicionais

Os argumentos posicionais são aqueles passados para uma função na ordem em que foram definidos. Eles são vinculados aos parâmetros da função na mesma ordem. Por exemplo:

```
def saudacao(nome, mensagem):
    print(f"Olá, {nome}! {mensagem}")

saudacao("Ana", "Como vai?")  # "Olá, Ana! Como vai?"
```

No exemplo acima, "Ana" é passado como o primeiro argumento e é associado ao parâmetro nome, enquanto "Como vai?" é o segundo argumento associado ao parâmetro mensagem.

## Argumentos nomeados ou opcionais

Os argumentos nomeados, também conhecidos como argumentos opcionais, permitem passar argumentos para uma função usando o nome do parâmetro correspondente. Isso oferece mais flexibilidade e clareza na chamada da função, especialmente quando há muitos parâmetros ou quando queremos fornecer apenas alguns argumentos específicos.

```
def posicao(t, v, s0=0):
    return s0 + v*t

posicao(2, 1)  # saída: 2
posicao(0.5, 8, s0=2)  # 6
```

No exemplo acima, o parâmetro `s0` é opcional e tem um valor padrão zero. Se não for fornecido na chamada da função, ele assumirá esse valor. No entanto, também podemos passar um valor diferente para `s0` usando a atribuição nomeada. Isso proporciona uma maior legibilidade ao código.

## Variáveis locais

As variáveis declaradas dentro de uma função pertencem apenas ao seu escopo, ou seja, elas não são acessíveis fora da função.

```
def exemplo():
    variavel_local = "Esta é uma variável local"
    print(variavel_local)
    
exemplo()
print(variavel_local)  # NameError
```

## Composição de funções

A composição de funções é uma técnica poderosa na programação que envolve usar o resultado de uma função como entrada para outra função. No Python, isso pode ser facilmente realizado combinando várias chamadas de função em uma expressão.


Vamos considerar duas funções simples, uma que dobra um número e outra que adiciona cinco a um número:

```
def dobro(x):
    return 2 * x

def adiciona_cinco(x):
    return x + 5
```

Agora, podemos compor essas duas funções chamando-as em sequência:

```
resultado = adiciona_cinco(dobro(3))
print(resultado)  # Saída: 11
```
