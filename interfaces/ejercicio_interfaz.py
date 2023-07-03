#En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.
#Al principio no tiene que haber una opción seleccionada.

import tkinter as tk
from tkinter import ttk
ventana= tk.Tk()
ventana.columnconfigure(0, weight=5) #config de columnas
seleccionado= tk.StringVar() #variable donde guardamos resultado
r1 = ttk.Radiobutton(ventana,text="Opción 1", value="1", variable=seleccionado) #creamos botones
r2 = ttk.Radiobutton(ventana,text="Opción 2", value="2", variable=seleccionado)
r3 = ttk.Radiobutton(ventana,text="Opción 3", value="3", variable=seleccionado)
r4 = ttk.Radiobutton(ventana,text="Opción 4", value="4", variable=seleccionado)
r1.grid(column=0, row=0) #lo mostramos con la gramática grid
r2.grid(column=0, row=1)
r3.grid(column=0, row=2)
r4.grid(column=0, row=3)

def reiniciar(event): #función que reinicia
    print("Reiniciando")
    seleccionado.set(None)  # Establece la selección en None

login_botón= ttk.Button(ventana,text="Reiniciar") #botón de reinicio
login_botón.grid(column =0, row= 4, sticky= tk.E, padx=10, pady=10) 
login_botón.bind("<Button-1>",reiniciar) #asignamos función al click

ventana.mainloop() #loop


