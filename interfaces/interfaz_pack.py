import tkinter #importamos tkinter

ventana= tkinter.Tk() #creamos una ventana 
#! WIDGET LABEL
label_saludo = tkinter.Label(ventana, text="label" ,bg="red", fg="blue") #creamos un widgets label
#text= texto que aparecerá, bg= color de fondo fg= color de las letras
#! GEOMETRÍA PACK
label_saludo.pack(ipadx=20, ipady=20, expand= True,side="left",fill="both" ) #mostramos el widgets con la geometría llamada pack
#ipadx= tamaño horizontal ipady= tamaño vertical expand=True expande por toda su zona fill= x ,y o both rellena vertical,horizontalmente o ambas
#side=left, right, bottom o top zona donde aparecerá 
label_saludo2 = tkinter.Label(ventana, text="label2" ,bg="brown", fg="green")
label_saludo2.pack(ipadx=10, ipady=10,side="right",fill="y" )

label_saludo3 = tkinter.Label(ventana, text="label3" ,bg="yellow", fg="green")
label_saludo3.pack(ipadx=50, ipady=50,side="bottom",fill="x" )

label_saludo4 = tkinter.Label(ventana, text="label4" ,bg="green", fg="blue")
label_saludo4.pack(ipadx=10, ipady=10,side="top",fill="y" )

ventana.mainloop()#hacemos un loop asi no se cierra la ventana