# Introdução à Física Computacional

Este projeto tem duas finalizades:

1. Praticar desenvolvimento web em uma applicação estática com as tecnologias:
   - html/css (tailwindcss como framework);
   - Javascript vanilla (frontend);
   - Flask (servidor/backend)

2. Produzir material de consulta e estudo para os estudantes matriculados na disciplina de *Introdução à Física Computacional* do Instituto Federal de Educação, Ciências e Tecnologia do Estado do Ceará, *campus* Crateús, do curso de Licenciatura em Física.

## Editor

Para produzir um artido a ser renderizado, você deve uma uma notação mínima de Markdow

TODO:
- Tablas:
  - apenas 1 header, seguido do separador, e as linhas em seguida
  - Espaço entre '|' e o restante. Modelo:
  
```Markdown
| Operando 1 | Operando 2 | Resultado  |
| ---------- | ---------- | ---------  |
| Verdadeiro | Verdadeiro | Verdadeiro |
| Verdadeiro | Falso      | Falso      |
| Falso      | Verdadeiro | Falso      |
| Falso      | Falso      | Falso      |
```


## Para desenvolvedores

Esta é uma documentação para componentes desta applicação web.

### static/js/modules/base.js

#### Classe `Compoenent`

Esta seção descreve a classe `Compoenent`, um utilitário simples para criar e manipular elementos HTML em JavaScript.

#### Finalidade

A classe `Compoenent` simplifica a criação e inserção de elementos no DOM, oferecendo uma API clara e concisa para operações comuns.

##### Usage
###### Instalação

Essa classe não requer instalação externa. Você pode usá-la diretamente no seu código JavaScript.
###### Creating components
```javascript
const paragraph = new Component('p'); // Creates a paragraph element
const heading = new Component('h2');   // Creates a heading element
```
###### Rendering Components

Use the render method to insert the element into the DOM:
Use o método `render` para inserir o elemento no DOM:

`render(into=null, how='a', before=null)`
    
- into: (HTMLElement) O elemento parent onde inserir, se fornecido
- how (string, opcional): Método de inserção (padrão: 'a').
    - a: Anexar como último filho.
    - b: Inserir antes do elemento 'before'.
    - r: Substituir o elemento 'before'.
- before (HTMLElement, opcional): Elemento de referência para 'b' e 'r'.

Este método retorna o tipo `HTMLElement`.

### static/js/modules/components.js

#### Índice

* [Visão Geral](#Visão-Geral)
* [Regras de Uso](#Regras-de-Uso)
* [Classes](#Classes)
    * [Paragraph](#Paragraph)
    * [ParagraphJustified](#ParagraphJustified)
    * [Lead](#Lead)
    * [Heading](#Heading)
    * [Code](#Code)
    * [PreCode](#PreCode)
    * [MockupCode](#MockupCode)
    * [Article](#Article)
    * [ArticleSet](#ArticleSet)

#### Visão Geral

O arquivo 'components.js' contém um conjunto de classes JavaScript que podem ser usadas para criar diversos elementos HTML. Essas classes são projetadas para serem fáceis de usar e flexíveis, para que possam ser usadas para criar uma ampla variedade de designs de sites.

#### Regras de Uso

Para usar as classes neste arquivo, você precisará incluí-lo em seu projeto JavaScript. Você pode fazer isso usando uma tag `<script>` ou importando o arquivo usando um sistema de módulos.

```html
<script src="components.js"></script>
```

#### Classes

O arquivo 'components.js' contém as seguintes classes:

* **Paragraph:** Cria um elemento `<p>` HTML.
* **ParagraphJustified:** Cria um elemento `<p>` HTML com texto justificado.
* **Lead:** Cria um elemento `<p>` HTML com a classe "lead".
* **Heading:** Cria um elemento `<h{level}>` HTML, onde `{level}` é o nível do cabeçalho (de 1 a 6).
* **Code:** Cria um elemento `<code>` HTML.
* **PreCode:** Cria um elemento `<pre>` HTML com um elemento `<code>` filho.
* **MockupCode:** Cria um contêiner para exibir código de forma estilizada.
* **Article:** Cria um elemento `<article>` HTML.
* **ArticleSet:** Cria um conjunto de artigos HTML.

##### Paragraph

A classe `Paragraph` pode ser usada para criar um elemento `<p>` HTML. O construtor aceita dois parâmetros:

* `text`: O texto a ser exibido no parágrafo.
* `classList`: Uma lista de classes CSS a serem aplicadas ao parágrafo.

```javascript
const paragraph = new Paragraph("Este é um parágrafo.", ["text-center", "text-lg"]);
```

### ParagraphJustified

A classe `ParagraphJustified` é uma subclasse da classe `Paragraph` que cria um elemento `<p>` HTML com texto justificado. O construtor aceita um parâmetro:

* `text`: O texto a ser exibido no parágrafo.

```javascript
const paragraphJustified = new ParagraphJustified("Este é um parágrafo justificado.");
```

##### Lead

A classe `Lead` é uma subclasse da classe `Paragraph` que cria um elemento `<p>` HTML com a classe "lead". O construtor aceita um parâmetro:

* `text`: O texto a ser exibido no parágrafo.

```javascript
const lead = new Lead("Este é um parágrafo de introdução.");
```

##### Heading

A classe `Heading` pode ser usada para criar um elemento `<h{level}>` HTML, onde `{level}` é o nível do cabeçalho (de 1 a 6). O construtor aceita dois parâmetros:

* `text`: O texto a ser exibido no cabeçalho.
* `level`: O nível do cabeçalho (de 1 a 6).

```javascript
const heading = new Heading("Este é um título de nível 1.", 1);
```

##### Code

A classe `Code` pode ser usada para criar um elemento `<code>` HTML. O construtor aceita um parâmetro:

* `code`: O código a ser exibido no elemento.

```javascript
const code = new Code("const x = 1;");
```

##### PreCode

A classe `PreCode` pode ser usada para criar um elemento `<pre>` HTML com um elemento `<code>` filho. O construtor aceita dois parâmetros:

* `code`: O código a ser exibido no elemento.
* `dataPrefix`: Um prefixo a ser aplicado ao elemento `<pre>`.

```javascript
const preCode = new PreCode("const x = 1;", "prefix-");
```

##### MockupCode

A classe `MockupCode` pode ser usada para criar um contêiner para exibir código de forma estilizada. O construtor não aceita parâmetros.

```javascript
const mockupCode = new MockupCode();
```

##### Article

A classe `Article` pode ser usada para criar um elemento `<article>` HTML. O construtor aceita dois parâmetros:

* `title`: O título do artigo.
* `leadText`: O texto de introdução do artigo.

```javascript
const article = new Article("Este é um artigo.", "Este é o texto de introdução do artigo.");
```

##### ArticleSet

A classe `ArticleSet` pode ser usada para criar um conjunto de artigos HTML. O construtor aceita dois parâmetros:

* `jsonPath`: O caminho para um arquivo JSON que contém os dados dos artigos.
* `into`: O elemento HTML em que os artigos serão renderizados.

```javascript
const articleSet = new ArticleSet("articles.json", document.body);
```

