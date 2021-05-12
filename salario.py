while True:
    
    try:
        Salario_bruto = float(input("Informe seu salario bruto com os centavos R$"))
        Dependentes = int(input("informe o numero de dependentes "))
        if not float and int :
            raise ValueError()
    except ValueError:
        print("Valor não permitido, coloque apenas numeros!")
    
    else:
        break

    if Salario_bruto <= 1100.00:
        reajuste = Salario_bruto/100 * 7.5

    elif (Salario_bruto >= 1100.01) and(Salario_bruto <= 2203.48):
        reajuste = (Salario_bruto*9/100)- 16.65    

    elif (Salario_bruto >= 2203.49 ) and (Salario_bruto <= 3305.22):
        reajuste = (Salario_bruto*12/100) - 78.36    

    elif (Salario_bruto >= 3305.23) and (Salario_bruto <= 6433.57):
        reajuste = (Salario_bruto*14/100) - 141.05    

    else:
        reajuste = (Salario_bruto*14/100) - 141.05    
        
        
        
    if Salario_bruto <= 1903.98:
        reajuste_irrf = 0
        
    elif (Salario_bruto >= 1903.99) and (Salario_bruto <= 2826.65):
        reajuste_irrf = (Salario_bruto*7.5/100)- 142.80    

    elif (Salario_bruto >= 2826.66 ) and (Salario_bruto <= 3751.05):
        reajuste_irrf = (Salario_bruto*15/100)- 354.80    

    elif (Salario_bruto >= 3751.06) and (Salario_bruto <= 4664.68):
        reajuste_irrf = (Salario_bruto*22.5/100)- 636.13    

    else:
        reajuste_irrf = (Salario_bruto*27.5/100)- 869.36
        
    Valor_dependentes = Dependentes * 189.59

    valor_final = Salario_bruto - (reajuste + reajuste_irrf)
        
    print(f"""
    Salario bruto é de: {Salario_bruto:,.2f}
    Valor do desconto INSS: {reajuste:,.2f}
    Valor do desconto IRRF: {reajuste_irrf:,.2f}
    Valor do desconto por Dependentes: {Valor_dependentes:,.2f}
    Valor total dos descontos: {reajuste + reajuste_irrf:,.2f}
    Salario liquido com desconto INSS e IRRF: {valor_final + Valor_dependentes:,.2f}
    """)


