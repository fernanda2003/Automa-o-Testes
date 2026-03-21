import unittest
#faz a função de soma entre dois números
def soma(a, b):
    return a + b
# diz que a classe herda de unittest
# identificando ele como um teste
class TesteSoma(unittest.TestCase):
# só executa métodos que comecem com test_ (ATENÇÃO A ESTE TÓPICO)
# teste para verificar se a função soma retorna o resultado correto, e se retorna o resultado errado com o . ou o F
    def test_funcao_soma(self):
        self.assertEqual(soma(10, 5), 15)
    def test_funcao_somaErrada(self):
         self.assertEqual(soma(10,5), 10)


# permite que execute o arquivo como um script Python comum
if __name__ == '__main__':
        unittest.main()


