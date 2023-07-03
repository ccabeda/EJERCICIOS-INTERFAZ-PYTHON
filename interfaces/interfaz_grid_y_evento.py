from tkinter import ttk #importamos ttk
import tkinter #importamos todo

ventana= tkinter.Tk() #creamos ventana


def saludar (event): #creamos la función de evento de 1 click
    print("Hola, hizo 1 click.")

def saludo_doble(event): #creamos la función de evento de doble click
    print("Hola, hizo 2 click.")
#! GEOMETRÍA GRID
ventana.columnconfigure(0, weight=3) #configuramos las ventanas ya que grid es como excel 
ventana.columnconfigure(1, weight=3) #el número es la columna i weight las cosas que se pueden poner en ella
ventana.columnconfigure(2, weight=5)
ventana.columnconfigure(3, weight=5)

#! WIDGET LABEL
username_label= ttk.Label(ventana,text="Username: ", ) 
username_label.grid(column=0, row=0, sticky=tkinter.W, padx=10, pady=10)#column= columna row= fila sticky= lado que aparece (norte,sur,este u oeste) padx y pady = tamaño

#! WIDGET ENTRY
password_entry= ttk.Entry(ventana)
password_entry.grid(column=1, row=0, sticky= tkinter.E)
#!WIDGET BOTÓN
login_botón= ttk.Button(ventana,text="Enviar")
login_botón.grid(column =2, row= 3, sticky= tkinter.E, padx=10, pady=10) 
login_botón.bind("<Button-1>",saludar) #le agregamos la función al botón
login_botón.bind("<Double-1>",saludo_doble)

#! WIDGET LISTBOX
lista=["Messi", "Mbappe", "Ronaldo","Trent Alex-Arnold"] #creamos lista de cosas
lista_nombres= tkinter.StringVar(value=lista) #le damos valor a la lista
lista_box=tkinter.Listbox(ventana,listvariable=lista_nombres) #la hacemos listbox
lista_box.grid(column=0, row=3, sticky= tkinter.W) #la mostramos

#! WIDGET SITCKBOTTONS
seleccionado= tkinter.StringVar() #creamos una variable donde guardar el resultado
r1= ttk.Radiobutton(ventana, text="Si", value="1", variable=seleccionado) #la creamos y le damos atributos
r2= ttk.Radiobutton(ventana, text="No", value="2", variable=seleccionado)
r3= ttk.Radiobutton(ventana, text="Probablemente", value="3", variable=seleccionado)
r4= ttk.Radiobutton(ventana, text="Probablemente no", value="4", variable=seleccionado)

r1.grid(column=2, row=0, padx=5,pady=5) #la mostramos 
r2.grid(column=2, row=1, padx=5,pady=5)
r3.grid(column=2, row=2, padx=5,pady=5)
r4.grid(column=2, row=3, padx=5,pady=5)

#! WIDGET CHECK
seleccionado= tkinter.StringVar()
botón = ttk.Checkbutton(ventana, text="Acepto las condiciones", variable=seleccionado)
botón.grid(column=2, row=4)

#! WIDGET MENÚ
menú_barra = tkinter.Menu(ventana) #creamos menú
#creamos tres objetos Menu
file_menú = tkinter.Menu(menú_barra, tearoff=0)
edit_menú = tkinter.Menu(menú_barra, tearoff=0)
help_menú = tkinter.Menu(menú_barra, tearoff=0)

# agregamos las opciones "Archivo", "Editar" y "Ayuda" a menú_barra
menú_barra.add_cascade(label="Archivo", menu=file_menú)
menú_barra.add_cascade(label="Editar", menu=edit_menú)
menú_barra.add_cascade(label="Ayuda", menu=help_menú)

#agregamos las opciones correspondientes a cada menú
file_menú.add_command(label="Abrir")
file_menú.add_command(label="Guardar")
file_menú.add_separator()
file_menú.add_command(label="Salir", command=ventana.quit)

edit_menú.add_command(label="Cortar")
edit_menú.add_command(label="Copiar")
edit_menú.add_command(label="Pegar")

help_menú.add_command(label="Acerca de")

#configuramos la barra de menú en la ventana principal
ventana.config(menu=menú_barra)




ventana.mainloop()






ventana.mainloop() #loop