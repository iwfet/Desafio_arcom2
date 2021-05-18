import tkinter as tk
from tkinter import Canvas, filedialog
import pandas as pd
import numpy  as np
from openpyxl import *

root = tk.Tk()

Canvas1 = tk.Canvas(root, width= 300, height= 300, bg='lightsteelblue')
Canvas1.pack()
#ler = pd.read_excel ('C:/Desenvolvimento/python/salario.xls')
valor_salario_liquido = []

ler = 0
def getExcel():
    global ler
    import_file_path = filedialog.askopenfilename()
    ler = pd.read_excel(import_file_path)
    
browseButton_excel = tk.Button(
    text="importe excel file",
    command=getExcel,
    bg='green', fg='white', font=('helvetica', 12, 'bold'))
Canvas1.create_window(150,150, window=browseButton_excel)

root.mainloop()

valor_salario_liquido = []
valor_desconto_inss = []
valor_desconto_irrf = []

          
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
          
      
    return reajuste_irrf


for index, linha in ler.iterrows():
    id = linha["Matricula"]
    nome = linha["Nome"]
    Dependentes = linha["Dependentes"]
    Descontos = linha["Desconto"]
    Salario_bruto = linha["Salario"]
    
    desconto_inss = DescontoINSS(Salario_bruto)
    desconto_irrf = DescontoIRRF(Salario_bruto,desconto_inss,Dependentes)
    valor_final = Salario_bruto - desconto_irrf - Descontos- desconto_inss
    
    valor_salario_liquido.append(f'''{valor_final:,.2f}''')
    valor_desconto_inss.append(f'''{desconto_inss:,.2f}''')
    valor_desconto_irrf.append(f'''{desconto_irrf:,.2f}''')

ler['Salario aplicado descontos'] = valor_salario_liquido
ler['Desconto do inss'] = valor_desconto_inss
ler['Desconto do irrf'] =  valor_desconto_irrf

writer = pd.ExcelWriter('salario_com_os_descontos.xlsx')
ler.to_excel(writer,'new_sheet')
writer.save()

print(ler)