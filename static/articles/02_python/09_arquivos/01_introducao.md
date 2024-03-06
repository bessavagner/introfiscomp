# Leitura e escrita

A leitura e escrita de arquivos são operações fundamentais em muitos programas, permitindo que os dados sejam armazenados e recuperados de forma persistente.

Python oferece uma maneira simples e eficiente de realizar essas operações, tornando-o uma escolha popular para tarefas que envolvem manipulação de arquivos.

Este artigo visa introduzir os conceitos básicos de leitura e escrita de arquivos em Python, fornecendo uma compreensão sólida que permitirá aos desenvolvedores começarem a trabalhar com arquivos de forma eficaz.

## Leitura de Arquivos

Para ler um arquivo em Python, você pode usar a função `open()` com o modo `'r'` (leitura). A função `open()` retorna um objeto de arquivo, que pode ser usado para acessar o conteúdo do arquivo. Aqui está um exemplo simples de como ler um arquivo:

``` python
# Abrindo o arquivo para leitura
arquivo = open('meu_arquivo.txt', 'r')

# Lendo o conteúdo do arquivo
conteudo = arquivo.read()

# Fechando o arquivo
arquivo.close()

print(conteudo)
```

## Escrita de Arquivos

Para escrever em um arquivo, você pode usar a função `open()` com o modo `'w'` (escrita). Se o arquivo especificado não existir, ele será criado. Se já existir, seu conteúdo será sobrescrito. Aqui está um exemplo de como escrever em um arquivo:

``` python
# Abrindo o arquivo para escrita
arquivo = open('meu_arquivo.txt', 'w')

# Escrevendo no arquivo
arquivo.write('Olá, mundo!')

# Fechando o arquivo
arquivo.close()
```

## Modos de Abertura de Arquivos

A função `open()` aceita vários modos de abertura de arquivos, que determinam como o arquivo será acessado. Os modos mais comuns são:

- `'r'`: Abre o arquivo para leitura.
- `'w'`: Abre o arquivo para escrita, sobrescrevendo o conteúdo existente.
- `'a'`: Abre o arquivo para escrita, adicionando ao conteúdo existente.
- `'x'`: Cria um novo arquivo para escrita, falhando se o arquivo já existir.

## Leitura e Escrita em um Único Bloco

Python oferece uma maneira mais segura e eficiente de trabalhar com arquivos usando a declaração `with`. Isso garante que o arquivo seja fechado corretamente após a operação, mesmo se ocorrerem exceções. Aqui está um exemplo de como usar `with` para ler e escrever em um arquivo:

``` python
# Leitura de arquivo usando 'with'
with open('meu_arquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Escrita de arquivo usando 'with'
with open('meu_arquivo.txt', 'w') as arquivo:
    arquivo.write('Novo conteúdo')
```
