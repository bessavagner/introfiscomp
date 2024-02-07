# Estruturas de repetição

Uma outra técnica fundamental na programação é a repetição de comandos (ou laço), permitindo a execução de um conjunto de instruções várias vezes. Existem duas maneiras comuns de implementar a repetição em pseudocódigo: usando o **PARA** e o **ENQUANTO**.

## PARA

O **PARA** é utilizado para repetir um conjunto de instruções um número determinado de vezes. Por exemplo, o seguinte código repete o comando escreva("Olá, mundo!") cinco vezes:

```
// Repetição usando PARA
para i de 1 até 5 faça
    escreva(i)
fim para
```

O código acima irá exibir o resultado:

```
1
2
3
4
5
```

### Estrutura do comando PARA

O comando PARA possui a seguinte estrutura:

```
para <variável> de <valor inicial> até <valor final> faça
    <conjunto de instruções>
fim para

```

- **variável**: é a variável que será utilizada para controlar o número de vezes que o laço será executado.

- **valor inicial**: é o valor inicial da variável.

- **valor final**: é o valor final da variável.

- **conjunto de instruções**: é o conjunto de instruções que serão executadas a cada iteração do laço.

## ENQUANTO

O **ENQUANTO**, por outro lado, é utilizado para repetir um conjunto de instruções enquanto uma condição específica for verdadeira. A execução continuará até que a condição não seja mais atendida.

```
// Repetição usando ENQUANTO
contador = 1
enquanto contador < 5 faça
    escreva(contador)
    contador = contador + 1
fim enquanto

```

O código acima irá exibir o resultado:

```
1
2
3
4
```

Note que neste exemplo acima, o número 5 não será exibido. Por quê?

### Estrutura do comando ENQUANTO

O comando ENQUANTO possui a seguinte estrutura:

```
enquanto <condição> faça
    <conjunto de instruções>
fim enquanto
```

- **condição**: é a condição que será avaliada para determinar se o laço será executado ou não.

- **conjunto de instruções**: é o conjunto de instruções que serão executadas a cada iteração do laço.

Ambas as estruturas de repetição são poderosas e oferecem flexibilidade para lidar com diferentes cenários de programação.