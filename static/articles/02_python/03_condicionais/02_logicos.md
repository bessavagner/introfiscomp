# Operadores lógicos

Os operadores lógicos são usados para combinar expressões booleanas. Eles são fundamentais para construir condições mais complexas em estruturas de decisão.

## 'E' lógico (and)

Retorna `True` apenas se ambas as expressões booleanas forem verdadeiras.

```
temperature = 22
weather = "ensolarado"
print(temperature > 20 and weather == "ensolarado")  # Saída: True

# Verificando se um número está dentro de um intervalo
number = 15
print(number > 10 and number < 20)  # Saída: True
```

## 'Ou' lógico (or)

Retorna `True` se pelo menos uma das expressões booleanas for verdadeira.

```
day = "sábado"
holiday = False
print(day == "domingo" or holiday)  # Saída: False

# Verificando disponibilidade de produto
product_available_online = False
product_available_store = True
print(product_available_online or product_available_store)  # Saída: True
```

## Negação lógica (`not`)

Inverte o valor da expressão booleana. Se for `True`, torna-se `False` e vice-versa.

```
raining = False
print(not raining)  # Saída: True

# Verificando se um usuário não está logado
user_logged_in = False
print(not user_logged_in)  # Saída: True
```
