def calcular_bonus(salario, tempo_empresa, meta_batida):
    
    if salario <= 0:
        raise ValueError("Não é um valor válido")
    novo_salario = salario
    if tempo_empresa >= 5:
        novo_salario = salario + salario * 0.2

    elif tempo_empresa >= 2:
        novo_salario = salario + salario * 0.1

    acrescimo = novo_salario * 0.05
    if meta_batida == True:
        novo_salario = novo_salario + acrescimo
        return novo_salario
    else:
        return novo_salario

