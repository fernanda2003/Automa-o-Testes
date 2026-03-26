def calcular_preco_final(preco_base,cupom=None, frete_gratis=False):
    if preco_base <= 0: 
        raise ValueError("não pode ser menor ou igual a zero")
    
    preco = preco_base

    if cupom == "PROMO10":
        preco = preco_base - preco_base * 0.1

    elif cupom == "PROMO20":
        preco = preco_base - preco_base * 0.2

    frete = 20
    if frete_gratis or preco> 500:
        frete = 0
    valor_final = preco + frete 
    return valor_final