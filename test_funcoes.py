from funcao import *
import pytest

def test_deve_retornar_true_para_numero_par():
    resultado = eh_par(4)
    assert resultado is True
def test_deve_retornar_false_para_numero_impar():
    resultado = eh_par(5)
    assert resultado is False