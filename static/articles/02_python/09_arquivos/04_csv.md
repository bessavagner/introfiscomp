# Arquivos CSV

## Introdução ao CSV

CSV (Comma-Separated Values) é um formato de arquivo simples que armazena dados tabulares, como uma planilha ou banco de dados, em texto simples.

Cada linha do arquivo representa um registro, e cada campo dentro de um registro é separado por uma vírgula. O CSV é um formato de arquivo muito popular para trocar dados entre diferentes sistemas, pois é fácil de ler e escrever tanto para humanos quanto para máquinas.

### A Biblioteca `csv` em Python

A biblioteca padrão `csv` em Python fornece funcionalidades para ler e escrever arquivos CSV. Ela oferece uma maneira simples e eficiente de trabalhar com dados tabulares, permitindo que os desenvolvedores manipulem esses dados de forma eficiente em seus projetos Python.

## Exemplo de Arquivo CSV com Duas Colunas: Tempo e Posição

Vamos considerar um arquivo CSV simples com duas colunas: `tempo` e `posição`. Cada linha representa um ponto no tempo e a posição correspondente.

```
tempo,posição
0,10
1,15
2,20
3,25
```

### Lendo Dados de um Arquivo CSV em Duas Listas

Para ler os dados do arquivo CSV em duas listas, uma para `tempo` e outra para `posição`, você pode usar a função `csv.reader()`. Aqui está um exemplo:

``` python
import csv

tempo = []
posicao = []

with open('dados.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor) # Pula a primeira linha (cabeçalho)
    for linha in leitor:
        tempo.append(float(linha[0]))
        posicao.append(float(linha[1]))

print("Tempo:", tempo)
print("Posição:", posicao)
```

### Salvando Dados em um Arquivo CSV

Para salvar dados de duas listas em um arquivo CSV, você pode usar a função `csv.writer()`. Aqui está um exemplo:

``` python
import csv

tempo = [0, 1, 2, 3]
posicao = [10, 15, 20, 25]

with open('dados_salvos.csv', 'w', newline='') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(['tempo', 'posicao']) # Escreve o cabeçalho
    for t, p in zip(tempo, posicao):
        escritor.writerow([t, p])
```

## Exemplo de Arquivo CSV com Quatro Colunas: Nome, Nota1, Nota2 e Nota3

Vamos considerar um arquivo CSV mais complexo com quatro colunas: `nome`, `nota1`, `nota2` e `nota3`. Cada linha representa um estudante e suas notas.

```
nome,nota1,nota2,nota3
Ana,85,90,88
João,78,82,85
Maria,92,95,90
```

### Lendo Dados de um Arquivo CSV em um Dicionário

Para ler os dados do arquivo CSV em um dicionário, onde as chaves são os nomes dos estudantes e os valores são listas que representam as notas, você pode usar a função `csv.DictReader()`. Aqui está um exemplo:

``` python
import csv

dados_estudantes = {}

with open('notas.csv', 'r') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        nome = linha['nome']
        notas = [float(linha['nota1']), float(linha['nota2']), float(linha['nota3'])]
        dados_estudantes[nome] = notas

print(dados_estudantes)
```

Trabalhar com arquivos CSV em Python é uma tarefa essencial para muitos projetos que envolvem dados tabulares. A biblioteca `csv` em Python oferece uma maneira simples e eficiente de ler e escrever arquivos CSV, permitindo que os desenvolvedores manipulem esses dados de forma eficiente em seus projetos. Ao dominar o uso da biblioteca `csv`, os desenvolvedores podem facilmente integrar funcionalidades que envolvem o armazenamento e a manipulação de dados tabulares em seus projetos Python.