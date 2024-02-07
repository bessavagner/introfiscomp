# Dicionários/Mapas

Um dicionário é uma estrutura de dados que armazena uma coleção de pares de chave-valor. Cada chave é única e está associada a um único valor. Dicionários são usados para armazenar dados de forma organizada e de fácil acesso.

Em pseudocódigo, podemos criar um dicionário da seguinte forma:

```
dicionario = {'nome': 'Fulano', 'idade': 30, 'cidade': 'São Paulo'}
dicionario_vazio = {}
```

Dicionários podem armazenar pares de chave-valor de diversos tipos, incluindo inteiros, números reais, textos e até mesmo outros dicionários.

Aqui estão alguns exemplos:

```
diccionario_numeros = {'um': 1, 'dois': 2, 'três': 3}
diccionario_nomes = {'Fulano': 30, 'Beltrana': 25, 'João Ninguém': 40}
diccionario_misto = {'nome': 'Fulano', 'idade': 30, 'cidade': 'São Paulo', 'hobbies': ['viajar', 'ler', 'assistir filmes']}
```

## Aplicações

Os dicionários são uma estrutura de dados fundamental em muitas linguagens de programação, incluindo Python, JavaScript e outras. Eles são úteis para uma variedade de casos de uso, incluindo:

1. **Armazenamento de dados indexados por chaves**: Os dicionários permitem associar valores a chaves únicas, proporcionando um meio eficiente de armazenar e recuperar dados.

2. **Acesso rápido a dados**: Como os dicionários são implementados com tabelas de hash (em muitas linguagens), eles oferecem acesso rápido aos dados com base na chave, em vez de precisar percorrer uma lista ou matriz.

3. **Configurações e opções de aplicativos**: Os dicionários são frequentemente usados para armazenar configurações e opções de aplicativos devido à sua capacidade de associar chaves descritivas a valores específicos.

4. **Tradução de chaves**: Em muitos casos, dicionários são usados para mapear chaves de entrada para chaves de saída, como em tradução de idiomas ou em sistemas de substituição de variáveis em strings de formatação.

5. **Armazenamento de metadados**: Os dicionários podem ser usados para armazenar metadados sobre objetos, como atributos adicionais em objetos de banco de dados ou propriedades de objetos em linguagens orientadas a objetos.

6. **Cache de dados**: Dicionários são frequentemente usados para implementar caches de dados em memória, onde os resultados de cálculos anteriores ou consultas a banco de dados são armazenados para acesso rápido posteriormente.

7. **Indexação de documentos**: Em sistemas de busca e indexação de documentos, os dicionários podem ser usados para armazenar índices que mapeiam termos de pesquisa para documentos nos quais esses termos aparecem.

8. **Armazenamento de grafos e relacionamentos**: Em implementações simples de grafos, os dicionários podem ser usados para representar listas de adjacência, onde cada nó é mapeado para uma lista de seus vizinhos.

9.  **Validação de entrada de dados**: Dicionários podem ser usados para validar e filtrar dados de entrada em aplicativos, garantindo que apenas chaves específicas estejam presentes e que os valores correspondentes atendam a determinados critérios.

## Operações

Vamos usar notação de métodos para apresentar operações em dicionários aqui.

### 1. Acessar valores

Para acessar um valor em um dicionário, podemos usar a operação obter. Essa operação recebe a chave do par chave-valor que queremos acessar e retorna o valor associado a essa chave.

```
diccionario = {'nome': 'Fulano', 'idade': 30, 'cidade': 'São Paulo'}
nome = diccionario.obter('nome')
escrever(nome)  # Fulano

// ou
idade = diccionario['idade']
escrever(idade)  # 30
```

### 2. Adicionar pares de chave-valor

Para adicionar um par de chave-valor a um dicionário, podemos usar a operação adicionar. Essa operação recebe a chave e o valor do novo par e os adiciona ao dicionário.

```
diccionario = {'nome': 'Fulano', 'idade': 30, 'cidade': 'São Paulo'}
diccionario.adicionar('profissão', 'programador')
escrever(diccionario)  # {'nome': 'Fulano', 'idade': 30, 'cidade': 'São Paulo', 'profissão': 'programador'}
```

### 3. Remover pares de chave-valor

Para remover um par de chave-valor de um dicionário, podemos usar a operação remover. Essa operação recebe a chave do par que queremos remover e o remove do dicionário.

```
diccionario = {'nome': 'Fulano', 'idade': 30, 'cidade': 'São Paulo'}
diccionario.remover('idade')
escrever(diccionario)  # {'nome': 'Fulano', 'cidade': 'São Paulo'}
```

### 4. Verificar se uma chave está presente

Para verificar se uma chave está presente em um dicionário, podemos usar a operação contem. Essa operação recebe a chave que queremos verificar e retorna True se a chave estiver presente no dicionário e False caso contrário.

```
diccionario = {'nome': 'Fulano', 'idade': 30, 'cidade': 'São Paulo'}
contem_chave = diccionario.contem('idade')
escrever(contem_chave)  # True
```

### 5. Iterar sobre os pares de chave-valor

Para iterar sobre os pares de chave-valor de um dicionário, podemos usar a operação iterar. Essa operação retorna uma sequência de pares de chave-valor, que podem ser iterados usando um laço for.

```
diccionario = {'nome': 'Fulano', 'idade': 30, 'cidade': 'São Paulo'}

// iterar nas chaves
PARA chave NO diccionario:
    escrever("Chave: ", chave, "| Valor:", diccionario[chave])
    # "chave: nome | valor: Fulano
    # "chave: idade | valor: 30
    # "chave: ciddade | valor: São Paulo
FIM PARA

// iterar nos valores
PARA valor NO diccionario.valores():
    escrever(Valor:", valor)
    # "Valor: Fulano
    # "Valor: 30
    # "Valor: São Paulo
FIM PARA

// iterar nos elementos (itens)
PARA elemento NO diccionario.itens():
    escrever("Chave: ", element[0], "| Valor:", elemento[1])
    # "chave: nome | valor: Fulano
    # "chave: idade | valor: 30
    # "chave: ciddade | valor: São Paulo
FIM PARA
```
