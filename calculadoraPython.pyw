from tkinter import *

root = Tk()

frame1 = Frame(root, bg="darkblue", width="400", height="600")
frame1.pack()

#------------ Pantalla -------------#

numerosPantalla = StringVar(value="0")

pantalla = Entry(frame1, textvariable=numerosPantalla)
pantalla.grid(row=0, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(bg="black", fg="#03f943", justify="right")

#------------ Funciones -------------#

operacion = ""
operacion_alt = ""
resultado = 0
comma = False

def introducirNumero(num):
    global operacion

    if numerosPantalla.get() == "0":
        numerosPantalla.set(num)

    elif operacion != "":
        numerosPantalla.set(num)

        operacion = ""
    else:
        numerosPantalla.set(numerosPantalla.get()+num)

    
def borrarPantalla():
    global operacion
    global operacion_alt
    global resultado

    if numerosPantalla.get() != "0":
        numerosPantalla.set("0")

        operacion = ""
        operacion_alt = operacion
        resultado = 0

def sumarNumeros(num):
    global resultado
    global operacion
    global operacion_alt

    resultado += float(num)
    operacion = "sumar"
    operacion_alt = operacion

    numerosPantalla.set(resultado)

def restarNumeros(num):
    global resultado
    global operacion
    global operacion_alt

    if resultado == 0:
        resultado += float(num)
    else:
        resultado -= float(num)
    operacion = "restar"
    operacion_alt = operacion

    numerosPantalla.set(resultado)

def multiplicarNumeros(num):
    global resultado
    global operacion
    global operacion_alt

    if resultado == 0:
        resultado += float(num)
    else:
        resultado *= float(num)

    operacion = "multiplicar"
    operacion_alt = operacion

    numerosPantalla.set(resultado)

def dividirNumeros(num):
    global resultado
    global operacion
    global operacion_alt

    if resultado == 0:
        resultado += float(num)
    else:
        resultado /= float(num)

    operacion = "dividir"
    operacion_alt = operacion

    numerosPantalla.set(resultado)

def introducir_coma(num):
    global comma
    if comma == False:
        numerosPantalla.set(numerosPantalla.get()+num)
    comma = True

def resultadoTotal(num):
    global resultado
    global operacion_alt
    global comma

    if operacion_alt == "sumar":
        numerosPantalla.set(resultado+float(num))
    elif operacion_alt == "restar":
        numerosPantalla.set(resultado-float(num))
    elif operacion_alt == "multiplicar":
        numerosPantalla.set(resultado*float(num))
    elif operacion_alt == "dividir":
        numerosPantalla.set(resultado/float(num))

    operacion_alt = operacion
    resultado = 0
    comma = False


#------------ Fila   0 -------------#
    
botonDEL = Button(frame1, text="C", width=3, command=lambda:borrarPantalla())
botonDEL.grid(row=1, column=1, pady=2, padx=2)

botonCE = Button(frame1, text="CE", width=3)
botonCE.grid(row=1, column=2, pady=2, padx=2)

botonBACK = Button(frame1, text="<<", width=3)
botonBACK.grid(row=1, column=3, pady=2, padx=2)

#------------ Fila   1 -------------#

boton7 = Button(frame1, text="7", width=3, command=lambda:introducirNumero("7"))
boton7.grid(row=2, column=1, pady=2, padx=2)

boton8 = Button(frame1, text="8", width=3, command=lambda:introducirNumero("8"))
boton8.grid(row=2, column=2, pady=2, padx=2)

boton9 = Button(frame1, text="9", width=3, command=lambda:introducirNumero("9"))
boton9.grid(row=2, column=3, pady=2, padx=2)

botonDividir = Button(frame1, text="/", width=3, command=lambda:dividirNumeros(numerosPantalla.get()))
botonDividir.grid(row=2, column=4, pady=2, padx=6)

#------------ Fila   2 -------------#

boton4 = Button(frame1, text="4", width=3, command=lambda:introducirNumero("4"))
boton4.grid(row=3, column=1, pady=2, padx=2)

boton5 = Button(frame1, text="5", width=3, command=lambda:introducirNumero("5"))
boton5.grid(row=3, column=2, pady=2, padx=2)

boton6 = Button(frame1, text="6", width=3, command=lambda:introducirNumero("6"))
boton6.grid(row=3, column=3, pady=2, padx=2)

botonMultiplicar = Button(frame1, text="x", width=3, command=lambda:multiplicarNumeros(numerosPantalla.get()))
botonMultiplicar.grid(row=3, column=4, pady=2, padx=6)

#------------ Fila   3 -------------#

boton1 = Button(frame1, text="1", width=3, command=lambda:introducirNumero("1"))
boton1.grid(row=4, column=1, pady=2, padx=2)

boton2 = Button(frame1, text="2", width=3, command=lambda:introducirNumero("2"))
boton2.grid(row=4, column=2, pady=2, padx=2)

boton3 = Button(frame1, text="3", width=3, command=lambda:introducirNumero("3"))
boton3.grid(row=4, column=3, pady=2, padx=2)

botonRestar = Button(frame1, text="-", width=3, command=lambda:restarNumeros(numerosPantalla.get()))
botonRestar.grid(row=4, column=4, pady=2, padx=6)

#------------ Fila   4 -------------#

botonComa = Button(frame1, text=",", width=3, command=lambda:introducir_coma("."))
botonComa.grid(row=5, column=1, pady=2, padx=2)

boton0 = Button(frame1, text="0", width=3, command=lambda:introducirNumero("0"))
boton0.grid(row=5, column=2, pady=2, padx=2)

botonIgual = Button(frame1, text="=", width=3, command=lambda:resultadoTotal(numerosPantalla.get()))
botonIgual.grid(row=5, column=3, pady=2, padx=2)

botonSumar = Button(frame1, text="+", width=3, command=lambda:sumarNumeros(numerosPantalla.get()))
botonSumar.grid(row=5, column=4, pady=2, padx=6)

root.mainloop()