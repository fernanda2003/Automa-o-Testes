import unittest
#teste falhar por tipo
def validar_formato_cpf(cpf):
    if isinstance(cpf, str) and len(cpf) == 11 and cpf.isdigit():
        return True
    return False

class TestValidarFormatoCPF(unittest.TestCase):
    def teste_cpf_valido(self):
        self.assertTrue(validar_formato_cpf("12345678901"))
    def teste_tamanho_curto(self):
        self.assertFalse(validar_formato_cpf("1234567890"))
    def teste_tamanho_longo(self):
        self.assertFalse(validar_formato_cpf("1234567890123"))
    def teste_cpf_com_letras(self):
        self.assertFalse(validar_formato_cpf("1234567890A"))
    def teste_tipo_incorreto(self):
        self.assertFalse(validar_formato_cpf(12345678901)) 
if __name__ == '__main__':
    unittest.main()
