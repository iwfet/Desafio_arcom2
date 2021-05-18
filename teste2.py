import tkinter as tk
from tkinter import Canvas, filedialog
import pandas as pd


root = tk.Tk()

Canvas1 = tk.Canvas(root, width= 300, height= 300, bg='lightsteelblue')
Canvas1.pack()

def getExcel():
    global ler
    import_file_path = filedialog.askopenfilename()
    ler = pd.read_excel(import_file_path)
    print(ler)
browseButton_excel = tk.Button(
    text="importe excel file",
    command=getExcel,
    bg='green', fg='white', font=('helvetica', 12, 'bold'))
Canvas1.create_window(150,150, window=browseButton_excel)


root.mainloop()