from tkinter import ttk, StringVar
import tkinter as tk

windows = tk.Tk()
windows.title("Ejercicio 10-2 - Lista desplegable")
windows.columnconfigure(0)
windows.rowconfigure(6)


marcas = ["Marcas de arco", "Kinetic", "Hoyt", "PSE", "A&F", "Cartel", "Samick", "Fivics", "W&W"]
tipos = ["Tipos de arcos", "Target recurve bows", "Compound bows", "Traditional bows"]

opcionmarcas = StringVar()
desplegable1 = ttk.Combobox(windows, width=25, state="readonly", textvariable=opcionmarcas, values=marcas)
desplegable1.grid(row=1, column=0, padx=25)
desplegable1.current(0)

opciontipos = StringVar()
desplegable2 = ttk.Combobox(windows, width=25, state="readonly", textvariable=opciontipos, values=tipos)
desplegable2.grid(row=3, column=0, padx=25)
desplegable2.current(0)

etiqueta1 = tk.Label(windows, text="Arcos")
etiqueta1.grid(row=0, column=0)

rellenoinferior = tk.Label(windows, text="")
rellenoinferior.grid(row=6, column=0)

def busqueda():
    print(opcionmarcas.get())
    print(opciontipos.get())

def primeraseleccion():
    if opcionmarcas.get() == marcas[0] or opciontipos.get() == tipos[0]:
        print("selecciona una opción")
    else:
        busqueda()

entrada1 = ttk.Entry(windows, width=25, state="readonly", textvariable=opcionmarcas)
entrada1.grid(row=4, column=0)

entrada2 = ttk.Entry(windows, width=25, state="readonly", textvariable=opciontipos)
entrada2.grid(row=5, column=0)

buscar = tk.Button(windows, text = "buscar", padx= 30, pady=6, command=primeraseleccion, bg ="white")
buscar.grid(row=4, column=1)



windows.mainloop()






