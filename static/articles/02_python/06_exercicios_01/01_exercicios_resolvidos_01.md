# Exercícios resolvidos

## Cálculo da média de uma lista de números

Crie um programa em Python que calcula a média de uma lista de números. A média é calculada somando todos os números da lista e dividindo pelo total de números.

### Solucão

```
numeros = [10, 20, 30, 40, 50]
soma = sum(numeros)
media = soma / len(numeros)
print(f"A média dos números é: {media}")
```

## Verificação de números pares em uma lista

Escreva um programa que percorre uma lista de números e verifica se cada número é par ou ímpar.

### Solucão

```
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    if numero % 2 == 0:
        print(f"{numero} é um número par.")
    else:
        print(f"{numero} é um número ímpar.")
```

## Contagem de vogais em uma string

Crie um programa que conta o número de vogais em uma string fornecida pelo usuário.

### Solucão

```
string = "Python é uma linguagem de programação"
vogais = "aeiou"
contador = 0
for letra in string:
    if letra.lower() in vogais:
        contador += 1
print(f"O número de vogais na string é: {contador}")
```

## Soma dos dígitos de um número

Escreva um programa que calcula a soma dos dígitos de um número inteiro fornecido pelo usuário.

### Solucão

```
numero = 12345
soma = sum(int(digito) for digito in str(numero))
print(f"A soma dos dígitos do número é: {soma}")
```

## Números primos

Escreva um programa que verifica e imprime todos os números primos em um intervalo fornecido pelo usuário.

### Solucão

```
inicio = input("Forneça o primeiro número do intervalo: ")
fim = input("Forneça o segundo número do intervalo: ")
for numero in range(inicio, fim+1):
    if numero > 1:
        for i in range(2, numero):
            if (numero % i) == 0:
                break
            else:
                print(numero, "é um número primo")
```

## Média

O dicionário abaixo contém o nome de estudantes (chaves) e três notas de avaliações (valores), que são listas. Crie uma função que deve receber um dicionário nesse formato e retornar outro dicionário, com as mesmas chaves, e cujos valores são as médias das notas de cada estudante.

```
notas = {
    'Albertina':[3, 5, 8],
    'Janderson':[7, 5, 6],
    'Keila':[10, 7.5, 8],
    'Tâmara':[6, 8.5, 9],
    'Walldisney':[2, 1, 1.5],
    'Xandy':[5, 5.5, 8]
}
```

### Solução

```
def calcular_medias(notas):
    medias = {}
    for estudante, lista_notas in notas.items():
        media = sum(lista_notas) / len(lista_notas)
        medias[estudante] = media
    return medias

# Chamando a função para calcular as médias
medias = calcular_medias(notas)

# Imprimindo o dicionário com as médias
print(medias)
```

## Força gravitacional 1

Crie uma função que calcule o peso de um corpo de massa m, mas utilizando a lei da Gravitaçao Universal de Newton: F = G &times; (M &times; m) / d&sup2;

Onde d é a distância do centro de um planeta ao objeto em questão. Para efeitos práticos, faça d = R + h, onde h é a distância da superfície do planta ao objeto, e R o raio do planeta. Aqui também, G é a constante universal da gravitação de Newton.
    
Sua função deve conter os parâmetros posicionais m, h e nomeados M e R (use os valores da Terra como padrão).

### Solução

```
CONSTANTE_GRAV = 6.67384e-11
RAIO_TERRA = 6.371e3
MASSA_TERRA = 5.972e24

def forca_grav(m, h, M=MASSA_TERRA, R=RAIO_TERRA):
    return CONSTANTE_GRAV*m*M/(R + h)**2
```

### Note

Aqui usamos a notação de potência de 10 para _float_: `6.67384e-11` é o mesmo que <math display="inline">6,67384 &times 10<sup>-11</sup></math>

## Força gravitacional 2

Use os dados abaixo para obter uma lista do seu peso em diferentes corpos celestes, com base na função criada no problema anterior. (use necessariamente o conceito de unpacking para exibir o resultado)

```
dados = {
    'Marte': [641.85e21, 3389.5],
    'Titã': [134.5e21, 2576], # lua de Saturno
    'Calisto': [107.6e21, 2410] # Lua de Jupiter
}
```

### Solução

```
for nome, (massa, raio) in dados.items():
  peso = forca_grav(70, raio, massa, raio)
  print(f"Seu peso em {nome} seria de {peso:.2f} N.")
```

Saída:

```
Seu peso em Marte seria de 65249337.77 N.
Seu peso em Titã seria de 23672515.32 N.
Seu peso em Calisto seria de 21636749.92 N.
```

### Note

Usamos o _unpacking_ de tuplas no laço `for nome, (massa, raio) in dados.items()`: Cada elemento da sequência `dados.items() ` uma tupla com dois elementos, a chave e o valor do dicionário. Assim, `nome` recebe as chaves, e os valores de `dados`, como são listas de tamanho 2, eles acabam sendo desempacotados em `massa` e em `raio`, a cada iteração.