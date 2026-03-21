import pytest
from   operacoes import *
def test_soma_T():
    resultado = soma (2,0) == 2
    assert resultado is True
def test_soma_F():
    resultado = soma (2,1) == 2
    assert resultado is False
def test_subtracao():
    assert subtracao (2,1) == 1
def test_multiplicacao():
    assert multiplicacao (2,1) == 2
def test_divisao():
    assert divisao (4,2) == 2
def test_divisao_por_zero():
    with pytest.raises(ValueError):
        divisao(10, 0) 
def test_raiz_quadrada():
    with pytest.raises(ValueError):
        raiz_quadrada(-3)
def test_calcular_media():
    assert calcular_media(lista_numeros=[1.5,4]) == pytest.approx(2.75)