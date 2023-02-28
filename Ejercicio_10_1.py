import tkinter

windows = tkinter.Tk()
windows.title("Ejercicio 10-1")
windows.columnconfigure(1)
windows.rowconfigure(4)

etiqueta = tkinter.Label(windows, text="Selecciona 1 opción")
etiqueta.grid(row=0, column=1)

def reset():
    opcionselect.set(None)

def resultado():
    print(opcionselect.get())

opcionselect = tkinter.StringVar(None, "B")

opcion1 = tkinter.Radiobutton(windows, text="SI", variable=opcionselect, value="SI", command=resultado)
opcion2 = tkinter.Radiobutton(windows, text="NO", variable=opcionselect, value="NO", command=resultado)
opcion3 = tkinter.Radiobutton(windows, text="QUIZAS", variable=opcionselect, value="QUIZAS", command=resultado)

opcion1.grid(row=1, column=1)
opcion2.grid(row=2, column=1)
opcion3.grid(row=3, column=1)

#opcion1.grid

breset = tkinter.Button(windows, text = "Quitar seleccion", padx= 30, pady=6, command=reset, bg ="orange")
breset.grid(row=4, column=1)

windows.mainloop()