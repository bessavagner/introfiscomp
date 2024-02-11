# Operadores lógicos

Os operadores lógicos são usados para combinar expressões booleanas. Eles são fundamentais para construir condições mais complexas em estruturas de decisão.

## 'E' lógico (and)

Retorna `True` apenas se ambas as expressões booleanas forem verdadeiras.

```python
temperatura = 22
clima = "ensolarado"
print(temperatura > 20 and clima == "ensolarado")  # Saída: True

# Verificando se um número está dentro de um intervalo
numero = 15
print(numero > 10 and numero < 20)  # Saída: True
```

## 'Ou' lógico (or)

Retorna `True` se pelo menos uma das expressões booleanas for verdadeira.

```python
dia = "sábado"
feriado = False
print(dia == "domingo" or feriado)  # Saída: False

# Verificando disponibilidade de produto
produtoDisponivelOnline = False
produtoDisponivelLojaFisica = True
print(produtoDisponivelOnline or produtoDisponivelLojaFisica)  # Saída: True
```

## Negação lógica (`not`)

Inverte o valor da expressão booleana. Se for `True`, torna-se `False` e vice-versa.

```python
chovendo = False
print(not chovendo)  # Saída: True

# Verificando se um usuário não está logado
usuarioLogado = False
print(not usuarioLogado)  # Saída: True
```