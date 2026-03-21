import unittest
def cadastrar_senha(senha):
    if len (senha) < 8:
        return "Senha muito curta"
    class TesteCadastrarSenha(unittest.TestCase):
        def teste_senha_valida(self):
            self.assertTrue(cadastrar_senha("senha12345") == "Senha válida")
        def teste_senha_curta(self):
            self.assertRaises(ValueError, cadastrar_senha, "123")

if __name__ == '__main__':
    unittest.main()