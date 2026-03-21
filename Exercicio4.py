
import unittest


def validar_senha_avancada(senha):
    if len(senha) < 8:
        return False
    if not any(char.isdigit() for char in senha):
        return False
    if not any(char.isupper() for char in senha):
        return False
    return True


class TestValidarSenhaAvancada(unittest.TestCase):

    def test_senha_valida(self):
        self.assertTrue(validar_senha_avancada("Senha123"))

    def test_senha_curta(self):
        self.assertFalse(validar_senha_avancada("Curta1"))

    def test_senha_sem_numero(self):
        self.assertFalse(validar_senha_avancada("SemNumero"))

    def test_senha_sem_maiuscula(self):
        self.assertFalse(validar_senha_avancada("semliteramaiuscula1"))
if __name__ == '__main__':
    unittest.main()