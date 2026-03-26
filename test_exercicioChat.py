import pytest
from exercicio_chat import *

def test_invalido():
    with pytest.raises(ValueError):
        calcular_bonus(0, 5, True)

def test_novo_salario_alto():
    assert calcular_bonus (100, 5, True)

def test_novo_salario_alto_sem_meta():
    assert calcular_bonus (100, 5, False)

def test_novo_salario_medio():
    assert calcular_bonus (100, 2, True)

def test_novo_salario_medio_sem_meta():
    assert calcular_bonus (100, 2, False)

def test_salario():
    assert calcular_bonus (100, 1, False)

def test_salario_com_meta():
    assert calcular_bonus (100, 1, True)