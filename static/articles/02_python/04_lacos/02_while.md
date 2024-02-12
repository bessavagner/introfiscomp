# Instrução while

A instrução `while` em Python é usada para criar loops que continuam a ser executados enquanto uma condição especificada é verdadeira. Isso significa que o bloco de código dentro do `while` será repetido até que a condição se torne falsa.

## Sintaxe

A sintaxe básica da instrução `while` em Python é a seguinte:

```
while condição:
    # Bloco de código a ser repetido
```

O bloco de código dentro do while é chamado de corpo do loop. Ele continuará a ser executado repetidamente enquanto a condição especificada for verdadeira. Assim que a condição se tornar falsa, a execução do loop será interrompida e o controle será transferido para a próxima linha de código após o bloco do while.

### Exemplo básico

Vamos considerar um exemplo simples onde queremos imprimir os números de 1 a 5 usando um loop while:

```
contador = 1
while contador <= 5:
    print(contador)
    contador += 1
```

Neste exemplo, inicializamos a variável contador com 1 e, em seguida, entramos em um loop while que continua a ser executado enquanto o valor de contador for menor ou igual a 5. Dentro do loop, imprimimos o valor atual de contador e depois incrementamos o valor de contador em 1. O loop continuará até que o valor de contador seja maior que 5.

## Evitando loops infinitos

É importante ter cuidado ao usar a instrução while para evitar loops infinitos, onde a condição nunca se torna falsa e o loop continua para sempre. Por exemplo:

```
# Exemplo de loop infinito
while True:
    print("Este é um loop infinito!")
```

Neste exemplo, a condição True sempre será verdadeira, então o loop continuará a ser executado para sempre, imprimindo a mensagem "Este é um loop infinito!" repetidamente.

Para evitar loops infinitos, certifique-se de que a condição especificada no while eventualmente se torne falsa, ou use uma estrutura de controle, como break, dentro do loop para sair dele quando necessário.

## Usando o break

Para sair de um loop while antes que a condição se torne falsa, você pode usar a instrução `break`. Isso interrompe imediatamente a execução do loop e transfere o controle para a próxima linha de código após o bloco while. Aqui está um exemplo:

```
contador = 1
while True:
    print(contador)
    contador += 1
    if contador > 5:
        break
```

Neste exemplo, o loop while é iniciado com a condição True, o que o tornaria um loop infinito. No entanto, dentro do loop, há uma verificação com a declaração if que verifica se o contador ultrapassou 5. Se isso acontecer, a instrução break é acionada, interrompendo o loop.

Ao usar break, certifique-se de ter uma condição de saída clara para evitar loops infinitos.

## Exercícios resolvidos

### 1. Lançamento vertical

Crie um programa que atualize a velocidade de um corpo lançado verticalmente para cima, e imprime na tela a mensagem `"Objeto está subindo com velocidade de {v} m/s"`, onde v é a velocidade desse objeto.

```
import time  # para vermos a mensagem em tempo real

def velocidade(t, vo=0, a=-9.8):
    return vo + a*t

def lancamento(v0, dt=0.1):
    t = 0
    v = v0
    while v > 0:
        print(f"Objeto está subindo com velocidade de {v:.2f} m/s")
        t = t + dt
        v = velocidade(t, v0)
        time.sleep(dt)  # pausa a execução por 'dt' segundos

    print("Objeto começa a cair agora.")

lancamento(10, dt=0.1)
```

Saída:

```
Objeto está subindo com velocidade de 10.00 m/s
Objeto está subindo com velocidade de 9.02 m/s
Objeto está subindo com velocidade de 8.04 m/s
Objeto está subindo com velocidade de 7.06 m/s
Objeto está subindo com velocidade de 6.08 m/s
Objeto está subindo com velocidade de 5.10 m/s
Objeto está subindo com velocidade de 4.12 m/s
Objeto está subindo com velocidade de 3.14 m/s
Objeto está subindo com velocidade de 2.16 m/s
Objeto está subindo com velocidade de 1.18 m/s
Objeto está subindo com velocidade de 0.20 m/s
Objeto começa a cair agora.
```

Acima usamos interpolação de string para imprimir a mensagem de acordo com a velocidade, e formatamos o número para duas casas decimais: dentro das chaves inserimos o especificador de formato `.2f`. O `f` indica que o valor deve ser tratado como `float`, e `.2` indica que o valor deve ser impresso com duas casas decimais. <a href="https://realpython.com/python-f-strings/">Veja mais sobre f-string</a>.