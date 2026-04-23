import tkinter as tk

# funciones
def agregar_valor(valor):
    texto = pantalla.get()

    # limpiar error
    if texto == "Error" or texto == "No se puede dividir por 0":
        pantalla.delete(0, tk.END)
        texto = ""

    if texto != "":
        ultimo = texto[-1]

        if ultimo in "+-*/" and valor in "+-*/":
            return

        if texto == "" and valor in "+*/":
            return

        if valor == "(" and (ultimo.isdigit() or ultimo == ")"):
            pantalla.insert(tk.END, "*")

        if valor.isdigit() and ultimo == ")":
            pantalla.insert(tk.END, "*")

    pantalla.insert(tk.END, valor)
    
def limpiar():
    pantalla.delete(0, tk.END)
    
def calcular():
    try:
        expresion = pantalla.get()

        if expresion == "":
            return

        resultado = eval(expresion)

        pantalla.delete(0, tk.END)
        pantalla.insert(0, resultado)

    except ZeroDivisionError:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "No se puede dividir por 0")

    except:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")

# ventana
ventana = tk.Tk()
ventana.title("Calculadora")

# pantalla
pantalla = tk.Entry(
    ventana,
    font=("Arial", 20),
    justify="right",
    bd=6
)
pantalla.grid(row=0, column=0, columnspan=4, sticky="nsew", ipady=15)


def crear_boton(texto, fila, columna, comando, colspan=1):
    boton = tk.Button(
        ventana,
        text=texto,
        command=comando,
        height=2
    )
    boton.grid(row=fila, column=columna, columnspan=colspan, sticky="nsew", padx=2, pady=2)


# fila 1
crear_boton("C", 1, 0, limpiar)
crear_boton("(", 1, 1, lambda: agregar_valor("("))
crear_boton(")", 1, 2, lambda: agregar_valor(")"))
crear_boton("%", 1, 3, lambda: agregar_valor("%"))


# fila 2
crear_boton("7", 2, 0, lambda: agregar_valor("7"))
crear_boton("8", 2, 1, lambda: agregar_valor("8"))
crear_boton("9", 2, 2, lambda: agregar_valor("9"))
crear_boton("/", 2, 3, lambda: agregar_valor("/"))


# fila 3
crear_boton("4", 3, 0, lambda: agregar_valor("4"))
crear_boton("5", 3, 1, lambda: agregar_valor("5"))
crear_boton("6", 3, 2, lambda: agregar_valor("6"))
crear_boton("*", 3, 3, lambda: agregar_valor("*"))


# fila 4
crear_boton("1", 4, 0, lambda: agregar_valor("1"))
crear_boton("2", 4, 1, lambda: agregar_valor("2"))
crear_boton("3", 4, 2, lambda: agregar_valor("3"))
crear_boton("-", 4, 3, lambda: agregar_valor("-"))


# fila 5
crear_boton("0", 5, 0, lambda: agregar_valor("0"), colspan=2)
crear_boton("=", 5, 2, calcular)
crear_boton("+", 5, 3, lambda: agregar_valor("+"))


#Responsive

for i in range(6):
    ventana.rowconfigure(i, weight=1)

for i in range(4):
    ventana.columnconfigure(i, weight=1)
    
    
# loop
ventana.mainloop()