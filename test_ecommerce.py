import pytest
from ecommerce import *
def test_cupom_sucesso():
    assert calcular_preco_final(100, "PROMO10", frete_gratis=False) == pytest.approx(110)
def test_cupom_sucesso_20():
    assert calcular_preco_final(100, "PROMO20", frete_gratis=False) == pytest.approx(100)
def test_sem_cupom():
    assert calcular_preco_final(100, "ata", frete_gratis=False) == pytest.approx(120)
def test_com_frete_gratis ():
    assert calcular_preco_final(100, "a", frete_gratis=True)
def test_preco_invalido():
    with pytest.raises(ValueError):
        calcular_preco_final(0, "a", frete_gratis=False) 