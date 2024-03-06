# JSON

## Introdução ao JSON

JSON (JavaScript Object Notation) é um formato de dados leve e fácil de ler e escrever para humanos, e fácil de gerar e analisar para máquinas.

É um formato de dados comum usado para armazenar e trocar dados entre um cliente e um servidor, e entre diferentes partes de uma aplicação. JSON é baseado em uma estrutura de dados de chave-valor, onde os valores podem ser strings, números, objetos (que são conjuntos de pares de chave-valor), arrays, booleanos e `null`.

### Criando um Dado JSON a Partir de uma String

Em Python, a biblioteca padrão `json` fornece métodos para trabalhar com dados JSON. Para criar um dado JSON a partir de uma string, você pode usar a função `json.loads()`. Aqui está um exemplo:

``` python
import json

# String JSON
dados_json_str = '{"nome": "João", "idade": 30, "cidade": "São Paulo"}'

# Convertendo a string JSON em um dicionário Python
dados_python = json.loads(dados_json_str)

print(dados_python)
```

## Escrita e Leitura de Arquivos JSON

A biblioteca `json` em Python também facilita a escrita e leitura de arquivos JSON. Isso é útil para armazenar dados em um formato estruturado e legível, que pode ser facilmente lido e modificado posteriormente.

### Escrita de Arquivos JSON

Para escrever dados em um arquivo JSON, você pode usar a função `json.dump()`. Aqui está um exemplo:

``` python
import json

# Dados a serem escritos no arquivo JSON
dados = {
    "nome": "Maria",
    "idade": 25,
    "cidade": "Rio de Janeiro"
}

# Escrevendo os dados no arquivo JSON
with open('dados.json', 'w') as arquivo:
    json.dump(dados, arquivo)
```

### Leitura de Arquivos JSON

Para ler dados de um arquivo JSON, você pode usar a função `json.load()`. Aqui está um exemplo:

``` python
import json

# Abrindo o arquivo JSON para leitura
with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)

print(dados)
```

JSON é um formato de dados versátil e amplamente utilizado que facilita a troca de dados entre diferentes partes de uma aplicação ou entre um cliente e um servidor. A biblioteca `json` em Python oferece uma maneira simples e eficiente de trabalhar com dados JSON, permitindo que os desenvolvedores criem, leiam e escrevam arquivos JSON de forma eficiente. Ao dominar o uso da biblioteca `json`, os desenvolvedores podem facilmente integrar funcionalidades que envolvem o armazenamento e a manipulação de dados em seus projetos Python.