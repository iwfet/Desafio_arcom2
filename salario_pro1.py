import pandas as pd


ler = pd.read_excel ('C:/Desenvolvimento/python/salario.xls')

          
def DescontoINSS_IRRF():    
    if Salario_bruto <= 1100.00:
        reajuste = Salario_bruto/100 * 7.5

    elif (Salario_bruto >= 1100.01) and(Salario_bruto <= 2203.48):
        reajuste = (Salario_bruto*9/100)- 16.65    

    elif (Salario_bruto >= 2203.49 ) and (Salario_bruto <= 3305.22):
        reajuste = (Salario_bruto*12/100) - 78.36    

    elif (Salario_bruto >= 3305.23) and (Salario_bruto <= 6433.57):
        reajuste = (Salario_bruto*14/100) - 141.05    

    else:
        reajuste = 713.10 - 141.05           
       
    Valor_dependentes = Dependentes * 189.59 
    salarioBase = Salario_bruto - (reajuste + Valor_dependentes)

            
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
    
    
    valor_final = Salario_bruto - Descontos -(reajuste - reajuste_irrf)
    return reajuste,reajuste_irrf, valor_final, Valor_dependentes,valor_final

for index, linha in ler.iterrows():
    id = linha["Matricula"]
    nome = linha["Nome"]
    Dependentes = linha["Dependentes"]
    Descontos = linha["Desconto"]
    Salario_bruto = linha["Salario"]
    
    reajuste,reajuste_irrf, valor_final, Valor_dependentes,valor_final = DescontoINSS_IRRF()
    
    print(f"""
    \033[36mSalario bruto é de: {Salario_bruto:,.2f}
    Numero de matricula {id}
    Outros descontos {Descontos}
    Valor do desconto INSS: {reajuste:,.2f}
    Valor do desconto IRRF: {reajuste_irrf:,.2f}
    Valor do desconto por Dependentes: {Valor_dependentes:,.2f}
    Valor total dos descontos: {reajuste + reajuste_irrf:,.2f}
    Salario liquido com desconto INSS e IRRF: {valor_final :,.2f}
    """)       
   
   
   
   
   
   
   
