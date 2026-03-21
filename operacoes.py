def soma (a, b):
    return a + b
    if a + b == 2:
         return True
    else:
         return False
def subtracao (a, b):
    return a - b
def multiplicacao (a, b):
    return a * b
def divisao (a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b
def raiz_quadrada(numero):
    if numero < 0:
        raise ValueError("não pode ser negativo")
    return numero ** 0.5 
def calcular_media(lista_numeros):
        return sum(lista_numeros) / len (lista_numeros)
