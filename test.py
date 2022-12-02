import tkinter as tk
from tkinter import ttk


v2 = tk.Tk()
v2.config(width=400, height = 500)
v2.title("Calculadora")


igual = ttk.Button(v2, text = "=")
igual.place(x = 265, y = 430, height = 70, width = 140)

delated = ttk.Button(v2, text = "borrar")
delated.place(x = -14, y = 430, height = 70, width = 140 )


n0 = ttk.Button(v2,text = "0")
n0.place(x= 125, y= 430, height = 70, width = 140)      

n1 = ttk.Button(v2,text = "1")
n1.place(x = -14, y = 361, height = 70, width = 140)

n2 = ttk.Button(v2, text = "2")
n2.place(x = 125, y = 361, height = 70, width = 140 )

n3 = ttk.Button(v2, text = "3")
n3.place(x = 265, y = 361, height = 70, width = 140)

n4 = ttk.Button(v2, text = "4")
n4.place(x = -14, y = 292, height = 70, width = 140)

n5 = ttk.Button(v2, text = "5")
n5.place(x = 125, y = 292, height = 70, width = 140)

n6  = ttk.Button(v2, text = "6")
n6.place(x = 265, y = 292, height = 70, width = 140)

n7 = ttk.Button(v2, text = "7")
n7.place(x = -14, y = 223, height = 70, width = 140)
    
n8 = ttk.Button(v2, text= "8")
n8.place(x = 125, y = 223, height = 70, width = 140)

n9 = ttk.Button(v2,text = "9")
n9.place(x = 265, y = 223, height = 70, width = 140)

suma = ttk.Button(v2, text = "+")
suma.place(x = 0, y  =  174, height = 50, width = 110)

resta = ttk.Button(v2, text = "-")
resta.place(x = 87.5, y  =  174, height = 50, width =110)

multiplicacion = ttk.Button(v2, text = "x")
multiplicacion.place(x = 185, y  =  174, height = 50, width = 110)

division = ttk.Button(v2, text = "÷")
division.place(x = 290, y  =  174, height = 50, width = 110)

v2.mainloop()


