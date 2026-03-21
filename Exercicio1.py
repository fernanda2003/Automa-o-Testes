#Exercício 1: O Verificador de Idade
#Objetivo: Praticar a estrutura básica e assertEqual.
import unittest
def pode_dirigir(idade):
    if idade >= 18:
        return True
    else:       
        return False
class TestePodeDirigir(unittest.TestCase):
    def teste_menor_18(self):
            self.assertEqual(pode_dirigir(16), False)
    def teste_maior_18(self):
            self.assertEqual(pode_dirigir(20), True)
if __name__ == '__main__':
    unittest.main()
    
    