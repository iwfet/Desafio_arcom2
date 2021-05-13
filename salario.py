dado = False

while True:
    while dado == True:
        try:
            continuar = int(input("\033[33m Informe 1 continuar ou 2 para finalizar: "))
            if not int or ( continuar < 1 or continuar > 2):
                raise ValueError("\033[31m Valor inválido!sd")
        except ValueError:
            print("\033[31m Valor inválido!")
            continue
        if continuar == 1:
            break
        
        elif continuar == 2:
            print("\033[33m Encerrando...")
            quit()
        
    while True:
        
        try:
            Salario_bruto = float(input("\033[33m Informe seu salario bruto com os centavos R$"))
            Dependentes = int(input("\033[33m Informe o numero de dependentes: "))
            if not float and int or (Salario_bruto < 0 or Dependentes < 0) :
                raise ValueError()
        except ValueError:
            print("\033[31m Valor não permitido, coloque apenas numeros!")
            
        else:
            break
                
            

    if Salario_bruto <= 1045.00:
        reajuste = Salario_bruto/100 * 7.5

    elif (Salario_bruto >= 1045.01) and(Salario_bruto <= 2089.60):
        reajuste = (Salario_bruto*9/100)- 16.65    

    elif (Salario_bruto >= 2089.61 ) and (Salario_bruto <= 3134.40):
        reajuste = (Salario_bruto*12/100) - 78.36    

    elif (Salario_bruto >= 3134.41) and (Salario_bruto <= 6101.06):
        reajuste = (Salario_bruto*14/100) - 141.05    

    else:
        reajuste = (Salario_bruto*14/100) - 141.05    
            
    Valor_dependentes = Dependentes * 189.59 
    salarioBase = Salario_bruto - reajuste -Valor_dependentes      
            
    if salarioBase <= 1903.98:
        reajuste_irrf = 0
            
    elif (salarioBase >= 1903.99) and (salarioBase <= 2826.65):
        reajuste_irrf = (salarioBase*7.5/100)- 142.80    

    elif (salarioBase >= 2826.66 ) and (salarioBase <= 3751.05):
        reajuste_irrf = (salarioBase*15/100)- 354.80    

    elif (salarioBase >= 3751.06) and (salarioBase <= 4664.68):
        reajuste_irrf = (salarioBase*22.5/100)- 636.13    

    else:
        reajuste_irrf = (salarioBase*27.5/100)- 869.36
            
    

    valor_final = Salario_bruto - (reajuste + reajuste_irrf)
            
    print(f"""
        \033[36mSalario bruto é de: {Salario_bruto:,.2f}
        Valor do desconto INSS: {reajuste:,.2f}
        Valor do desconto IRRF: {reajuste_irrf:,.2f}
        Valor do desconto por Dependentes: {Valor_dependentes:,.2f}
        Valor total dos descontos: {reajuste + reajuste_irrf:,.2f}
        Salario liquido com desconto INSS e IRRF: {valor_final :,.2f}
        """)
    dado = True



    
 