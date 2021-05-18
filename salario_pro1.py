import pandas as pd
import numpy  as np
from openpyxl import *

ler = pd.read_excel ('C:/Desenvolvimento/python/salario.xls')
valor_salario_liquido = []
          
def DescontoINSS(salarioBruto):    
    if salarioBruto <= 1100.00:
        reajuste = salarioBruto/100*7.5

    elif (salarioBruto >= 1100.01) and(salarioBruto <= 2203.48):
        reajuste = (salarioBruto*9/100)- 16.65    

    elif (salarioBruto >= 2203.49 ) and (salarioBruto <= 3305.22):
        reajuste = (salarioBruto*12/100) - 78.36    

    elif (salarioBruto >= 3305.23) and (salarioBruto <= 6433.57):
        reajuste = (salarioBruto*14/100) - 141.05    

    else :
        reajuste = 713.10 - 141.05           
       
    print(reajuste)
    return reajuste 
    

def DescontoIRRF(salariobruto,desc,dep):
    
    salariobase = salariobruto - desc - (dep * 189.59)
             
    if salariobase <= 1903.98:
        reajuste_irrf = 0
            
    elif (salariobase >= 1903.99) and (salariobase <= 2826.65):
        reajuste_irrf = (salariobase*7.5/100)- 142.80    

    elif (salariobase >= 2826.66 ) and (salariobase <= 3751.05):
        reajuste_irrf = (salariobase*15/100)- 354.80    

    elif (salariobase >= 3751.06) and (salariobase <= 4664.68):
        reajuste_irrf = (salariobase*22.5/100)- 636.13    

    else:
        reajuste_irrf = (salariobase*27.5/100)- 869.36   
    print(reajuste_irrf)       
      
    return reajuste_irrf


for index, linha in ler.iterrows():
    id = linha["Matricula"]
    nome = linha["Nome"]
    Dependentes = linha["Dependentes"]
    Descontos = linha["Desconto"]
    Salario_bruto = linha["Salario"]
    
    desconto_inss = DescontoINSS(Salario_bruto)
    desconto_irrf = DescontoIRRF(Salario_bruto,desconto_inss,Dependentes)
    valor_final = Salario_bruto - desconto_irrf- desconto_inss
    
    valor_salario_liquido.append(f'''{valor_final:,.2f}''')

ler['Salario Descontado'] = valor_salario_liquido

writer = pd.ExcelWriter('salario_com_os_descontos.xlsx')
ler.to_excel(writer,'new_sheet')
writer.save()

print(ler)