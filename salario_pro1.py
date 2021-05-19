import tkinter as tk
from tkinter import Canvas, filedialog
from tkinter import font
import pandas as pd
import numpy  as np
from openpyxl import *

root = tk.Tk()

Canvas1 = tk.Canvas(root, width= 300, height= 300, bg='lightsteelblue')
Canvas1.pack()
#ler = pd.read_excel ('C:/Desenvolvimento/python/salario.xls')
valor_salario_liquido = []

fechando = False

ler = 0
def getExcel():
    global ler
    import_file_path = filedialog.askopenfilename()
    ler = pd.read_excel(import_file_path)
    
browseButton_excel = tk.Button(
    text="Selecionar arquivo Excel",
    command=getExcel,
    bg='green', fg='white', font=('helvetica', 12, 'bold'))
Canvas1.create_window(150,150, window=browseButton_excel)

def fechar():
    global fechando

    root.quit()

browseButton_excel = tk.Button(
    text= 'Gerar arquivo',
    command= fechar,
    bg= 'red', fg = 'white', font=('helvetica', 12, 'bold'))
Canvas1.create_window(150, 200, window=browseButton_excel)


root.mainloop()

def DescontoINSS(Salario_bruto):    
    
    global reajuste
    
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
       
    #print(reajuste)
    
    return reajuste



def descontoIRRF(Salario_bruto, reajuste):    
    
    global reajuste_irrf

    global valor_final
    
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
    
    
    valor_final = Salario_bruto - reajuste - Dependentes * 189.59

    #print(reajuste_irrf, ',' , valor_final)
    

    return valor_final, reajuste_irrf

for index, linha in ler.iterrows():
    id = linha["Matricula"]
    nome = linha["Nome"]
    Dependentes = linha["Dependentes"]
    Descontos = linha["Desconto"]
    Salario_bruto = linha["Salario"]
    DescontoINSS(Salario_bruto)
    descontoIRRF(Salario_bruto, reajuste)
    
    print_valor = valor_final - reajuste_irrf

    valor_salario_liquido.append(f'''{print_valor:,.2f}''')
    valor_final = Salario_bruto - Descontos - (reajuste + reajuste_irrf)


ler['Salario Descontado'] = valor_salario_liquido

writer = pd.ExcelWriter('salario_com_os_descontos.xlsx')
ler.to_excel(writer,'new_sheet')
writer.save()

print(ler)