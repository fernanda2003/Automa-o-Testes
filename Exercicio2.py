# Exercício 2: Calculadora de Descontos
# Objetivo: Praticar lógica de negócio e múltiplos asserts.
# Crie uma função calcular_desconto(valor, percentual).
# ‣ Se o percentual for maior que 50%, a função deve limitar o desconto a 50%
# (regra de negócio).
import unittest
def calcular_desconto(valor,percentual):
    if percentual > 50:
        percentual = 50
    return valor-(valor*percentual/100)
class TesteCalcularDesconto(unittest.TestCase):
    def teste_desconto_10(self):
        self.assertEqual(calcular_desconto(100, 10), 90)
    def teste_desconto_70(self):
        self.assertEqual(calcular_desconto(150, 70), 75)
    def teste_valor_zero(self):
        self.assertEqual(calcular_desconto(0, 20), 0)
if __name__ == '__main__':
    unittest.main()