import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from tkinter import scrolledtext

def init_window():
    window = tk.Tk()
    window.title('Mi primera aplicacion')
    window.geometry('500x250')

    label = tk.Label(window, text="Hello", font = ('Arial bond', 20))
    label.grid(column=1, row=0)

    label = tk.Label(window, text = 'Calculadora', font = ('Arial bond', 15))
    label.grid(column = 0, row = 0)

    entrada1 = tk.Entry(window, width = 10)
    entrada2 = tk.Entry(window, width = 10)

    entrada1.grid(column = 1, row = 1)
    entrada2.grid(column = 1, row = 2)

    label_entrada1 = tk.Label(window, text = 'Ingrese primer numero', font = ('Arial bold', 10))
    label_entrada1.grid(column = 0, row = 1)

    label_entrada2 = tk.Label(window, text = 'Ingrese segundo numero', font = ('Arial bond', 10))
    label_entrada2.grid(column = 0, row = 2)

    label_operador = tk.Label(window, text = 'Escoja un operador', font = ('Arial bond', 10))
    label_operador.grid(column = 0, row = 3)

    combo_operadores = ttk.Combobox(window)
    combo_operadores['values'] = ['+','-','*','/','pow']
    combo_operadores.current(0)
    combo_operadores.grid(column = 1, row = 3)

    label_resultado = tk.Label(window, text= 'Resultado: ', font = ('Arial bold', 15))
    label_resultado.grid(column = 0, row = 5)

    boton = tk.Button(window,
                      command = lambda: click_calcular(
                          label_resultado,
                          entrada1.get(),
                          entrada2.get(),
                          combo_operadores.get()),
                      text = 'Calcular',
                      bg = "orange",
                      fg = "white")
    boton.grid(column = 1, row = 4)

    def clicked():

        messagebox.showinfo('Bienvenido', '¡Gracias por usar la calculadora!')

    btn = tk.Button(window, text = 'Haga Click', command = clicked)
    btn.grid (column = 1, row = 5)

    label = tk.Label(window, text="Hello")
    label.grid(column=0, row=6)
    def clicked():
    
        label.configure(text="Hola :D, ¿Como estas?")
        txt = scrolledtext.ScrolledText(window,width=45,height=5)
        txt.grid(column=3,row=7)
        txt.insert(INSERT, """███    ███ ██████████ ███         ████████
███    ███ ███    ███ ███        ███    ███
██████████ ███    ███ ███        ██████████
███    ███ ███    ███ ███        ███    ███
███    ███ ██████████ ██████████ ███    ███ """)
    

    btn = Button(window, text="Dame un click", command=clicked)
    btn.grid(column=1, row=6)

    

    window.mainloop()
def calculadora(num1, num2, operador):
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        resultado = round(num1/num2,2)
    else:
        resultado = num1 ** num2
    return resultado

def click_calcular(label, num1, num2, operador):
    valor1 = float(num1)
    valor2 = float(num2)

    res = calculadora(valor1, valor2, operador)

    label.configure(text = 'Resultado '+ str(res))
def main():
    init_window()
main()