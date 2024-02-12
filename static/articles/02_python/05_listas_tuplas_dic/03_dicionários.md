# Dicionários

Os dicionários são outra estrutura de dados fundamental em Python. Eles permitem armazenar pares chave-valor, facilitando a organização e recuperação de informações de forma eficiente.

## Criando e acessando dicionários

Para criar um dicionário em Python, utilizamos chaves `{}` e especificamos os pares chave-valor. Veja um exemplo:

```
# Criando um dicionário de informações de uma pessoa
pessoa = {
    'nome': 'João',
    'idade': 30,
    'cidade': 'São Paulo'
}

# Acessando valores do dicionário
print(pessoa['nome'])  # Saída: João
print(pessoa['idade'])  # Saída: 30
```

## Iterando sobre dicionários

Assim como nas listas, podemos iterar sobre os elementos de um dicionário em Python. Veja um exemplo:

###  Iterando sobre chaves

```
# Criando um dicionário
movel = {"massa": 1.0, "posicao": [1, 0], "velocidade": [2, 1]}

# Iterando sobre as chaves do dicionário
for chave in movel:
    print(f"Chave: {chave}")
```

Saída:

```
Chave: massa
Chave: posicao
Chave: velocidade
```

### Iterando sobre valores

```
# Iterando sobre os valores do dicionário
for valor in objeto.values():
    print(f"Valor: {valor}")
```

Saída:

```
Valor: 1.0
Valor: [1, 0]
Valor: [2, 1]
```

### Iterando sobre ambos valores e chaves

```
# Iterando sobre as chaves e valores do dicionário pessoa
for variavel, valor in objeto.values():
    print(f'{variavel}: {valor}')
```

Saída:

```
massa: 1.0
posicao: [1, 0]
velocidade: [2, 1]
```

### Observações:

- A ordem de iteração das chaves em um dicionário não é garantida para Python versão < 3.7
- A ordem de iteração das chaves é de acordo com a ordem de inserção do element para Python versão >= 3.7
- Se você precisa iterar sobre as chaves em uma ordem crescente, você pode usar a função sorted().
- A função dict.keys() retorna um objeto que é uma sequência das chaves do dicionário.
- A função dict.values() retorna um objeto que é uma sequência dos valores do dicionário.
- A função dict.items() retorna um objeto que é uma sequência de tuplas, onde cada tupla contém uma chave e um valor.


## Métodos de dicionários

Python oferece diversos métodos embutidos para manipular dicionários. Aqui estão alguns exemplos:

```
# Adicionar um novo par chave-valor
pessoa['email'] = 'joao@email.com'

# Remover um item do dicionário
pessoa.pop('cidade')

# Verificar se uma chave existe no dicionário
if 'idade' in pessoa:
    print('A chave idade existe no dicionário')

# Limpar o dicionário
pessoa.clear()
```

## Compreensão de dicionários

Assim como as listas, é possível utilizar a compreensão de dicionários em Python para criar dicionários de forma concisa. Veja um exemplo:

```
# Criar um dicionário com o quadrado dos números de 1 a 5
quadrados = {num: num**2 for num in range(1, 6)}

print(quadrados)
```

Neste exemplo, o dicionário `quadrados` terá chaves de 1 a 5 e os valores serão os quadrados correspondentes.
