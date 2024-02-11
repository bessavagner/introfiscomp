# Por que usar funções?

Implementar funções em um códdigo é uma prática que promove a modularidade, a reutilização de código e a manutenção de programas de forma eficiente e organizada.

Segue aqui uma lista de alguns princípios para o uso de funções:

1. **Organização do Código**: Funções permitem dividir o código em partes menores e mais gerenciáveis, o que facilita a compreensão e a manutenção do programa. Em vez de ter todo o código em um único bloco, ele é dividido em seções lógicas, tornando-o mais legível e compreensível.

2. **Reutilização de Código**: Uma vez que uma função é definida, ela pode ser chamada várias vezes em diferentes partes do programa. Isso elimina a necessidade de repetir o mesmo bloco de código várias vezes, promovendo a reutilização e evitando a duplicação de código. Quando uma mudança é necessária, ela só precisa ser feita em um único lugar, dentro da função, em vez de em várias partes do código.

3. **Abstração**: Funções permitem abstrair detalhes de implementação complexos, fornecendo uma interface simples para os usuários. Isso significa que os usuários da função só precisam conhecer sua interface (os parâmetros que ela aceita e o que ela retorna), sem precisar entender como a função realiza suas tarefas internamente. Isso torna o código mais modular e fácil de usar.

4. **Testabilidade**: Ao dividir o código em funções pequenas e independentes, cada função pode ser testada separadamente para garantir que funcione corretamente. Isso facilita a identificação e a correção de erros, pois é mais fácil isolar e testar partes específicas do código.

5. **Legibilidade e Manutenção**: O uso adequado de funções pode melhorar significativamente a legibilidade do código, tornando-o mais claro e compreensível. Além disso, como as funções encapsulam lógicas específicas, torna-se mais fácil entender e manter o código, pois as mudanças e atualizações podem ser feitas em partes individuais do programa sem afetar o restante do código.

## Depuração

A depuração é uma etapa crucial no desenvolvimento de software, pois envolve identificar e corrigir erros ou bugs em um programa. Utilizar funções pode ser extremamente útil durante o processo de depuração por vários motivos:

1. **Isolamento de Partes do Código**: Ao encapsular partes do código em funções, é possível isolar áreas específicas que podem estar causando problemas. Isso torna mais fácil identificar e resolver erros, pois você pode se concentrar em uma parte do código de cada vez, em vez de examinar todo o programa de uma vez.

2. **Facilidade de Teste**: Funções bem definidas podem ser testadas individualmente, o que ajuda a garantir que cada parte do código funcione conforme o esperado. Isso é especialmente útil ao depurar, pois permite verificar o comportamento de cada função separadamente, identificando assim onde os erros estão ocorrendo.

3. **Mensagens de Erro Mais Claras**: Ao dividir o código em funções com nomes descritivos, as mensagens de erro tornam-se mais informativas e direcionadas. Isso facilita a identificação da origem do erro e a compreensão do problema.

Além disso, as funções podem ser usadas para implementar técnicas específicas de depuração, como logging e tratamento de exceções, tornando o processo de depuração mais eficiente e robusto.

### Exemplo

Considere a função divisao definida abaixo:

```
def divisao(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Erro: divisão por zero")

divisao(10, 0)
```

Neste exemplo, a função divisao tenta dividir dois números (a e b), mas lança uma exceção ZeroDivisionError se b for igual a zero. Ao chamar divisao(10, 0), ocorrerá um erro de divisão por zero. Utilizando a depuração e as funcionalidades de exceção do Python, podemos identificar e lidar com esse erro de maneira adequada.

Em resumo, o uso de funções durante a depuração não só ajuda a identificar e corrigir erros mais rapidamente, mas também promove boas práticas de desenvolvimento de software, como modularidade, testabilidade e legibilidade do código.

Em seções futuras você verá como se utilizar exceções e _loggins_.