#1)Crear una ventana básica con el título "Mi ventana".
#2)Crear una etiqueta con el texto "Hola, mundo!" y mostrarla en la ventana.
#3)Crear un botón con el texto "Haz clic aquí" y mostrarlo en la ventana.
#4)Crear una caja de entrada de texto para que el usuario pueda escribir un mensaje.
#5)Crear un botón que, al hacer clic en él, imprima el contenido de la caja de entrada en la consola.
#6)Crear una barra de menú con las opciones "Archivo", "Editar" y "Ayuda".
#7)Crear un menú desplegable dentro de la opción "Archivo" con las opciones "Abrir", "Guardar" y "Salir".
#8)Crear un menú desplegable dentro de la opción "Editar" con las opciones "Cortar", "Copiar" y "Pegar".
#9)Crear un menú desplegable dentro de la opción "Ayuda" con la opción "Acerca de".
#10)Crear una ventana de diálogo que permita al usuario seleccionar un archivo de su computadora.

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
#! 
ventana= tk.Tk()
ventana.title("Mi ventana")
ventana.columnconfigure(0 , weight=3)
ventana.columnconfigure(1 , weight=3)
ventana.columnconfigure(2 , weight=3)

#! 2)
label_saludo= tk.Label(ventana,text="Hola , mundo!")
label_saludo.grid(column=0, row=0,padx=5,pady=5,sticky=tk.W)

#! 3)
botón=ttk.Button(ventana,text="Haz clic aquí")
botón.grid(column=0,row=1,padx=5,pady=5,sticky=tk.W)

#! 4)
caja_entrada=ttk.Entry(ventana)
caja_entrada.grid(column=1,row=1,padx=5,pady=5,sticky=tk.W)

#! 5)
def imprimir_resultado(event):
    contenido= caja_entrada.get()
    print(contenido)

botón_imprimir= ttk.Button(ventana,text="Imprimir contenido ingresado.",)
botón_imprimir.bind("<Button-1>",imprimir_resultado)
botón_imprimir.grid(column=2, row=1)

#! 6) MENÚ
menú_barra = tk.Menu(ventana)

file_menú = tk.Menu(menú_barra, tearoff=0)
edit_menú = tk.Menu(menú_barra, tearoff=0)
help_menú = tk.Menu(menú_barra, tearoff=0)

menú_barra.add_cascade(label="Archivo", menu=file_menú)
menú_barra.add_cascade(label="Editar", menu=edit_menú)
menú_barra.add_cascade(label="Ayuda", menu=help_menú)

ventana.config(menu=menú_barra)

#! 7) 
file_menú.add_command(label="Abrir")
file_menú.add_command(label="Guardar")
file_menú.add_separator()
file_menú.add_command(label="Salir", command=ventana.quit)

#! 8)
edit_menú.add_command(label="Cortar")
edit_menú.add_command(label="Copiar")
edit_menú.add_command(label="Pegar")

#! 9)
help_menú.add_command(label="Acerca de")

#! 10)

def abrir_archivos(event):
    archivo=filedialog.askopenfilename()
    print (archivo)

botón_archivo=tk.Button(ventana, text="Abrir Archivos")
botón_archivo.bind("<Button-1>",abrir_archivos)
botón_archivo.grid(column=2, row=3, sticky=tk.W)


ventana.mainloop()
