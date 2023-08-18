#IMPORTAMOS LIBRERIAS

from tkinter import *
from math import *

def btnClik(num):
    global operador
    operador=operador+str(num)
    input_text.set(operador)


def resultado ():
    global operador
    try:
        opera_=str(eval(operador))
        input_text.set(opera_)
    except:
        input_text,set("ERROR")
    operador = ""
    

def clear ():
    global operador
    operador = ""
    input_text.set("")
   

def borrar_uno():
    global operador
    if operador:
        operador = operador[:-1] 
        input_text.set(operador)
                


#ESTRUCTURA DE LA VENTANA
ventana = Tk ()
ventana.geometry ('392x500')
ventana.config (bg= "pink")
ventana.resizable (0, 0)
ventana.title ('Calculadora')

#DIMENSIONES DE LOS BOTONES DE LA CALCULADORA
ancho_boton = 10
alto_boton = 3
color_boton = "white"
color_texto = "black"

input_text=StringVar()
operador=""

Frame = Frame (ventana, bg= color_boton, relief= SUNKEN)
Frame.grid(column=0, row=0, padx=6, pady=3)


#FILA 1
Button0= Button (ventana, text= "%", bg= color_boton, fg= color_texto, width= ancho_boton, height= alto_boton, command=lambda: btnClik ("%")) .place (x= 15, y= 150)
Button1= Button (ventana, text= "x^x", bg= color_boton, fg= color_texto, width= ancho_boton, height= alto_boton, command=lambda: btnClik ("x^x")) .place (x= 105, y= 150)
Button2= Button (ventana, text= "C", bg= color_boton, fg= color_texto, width= ancho_boton, height= alto_boton, command= clear) .place (x= 195, y= 150)
Button3= Button (ventana, text= "⌫", bg= color_boton, fg= color_texto, width= ancho_boton, height= alto_boton, command=borrar_uno) .place (x= 285, y= 150)
#FILA2
Button4= Button (ventana, text= "7", bg= color_boton, fg= color_texto, width= ancho_boton, height= alto_boton, command=lambda: btnClik (7)) .place (x= 15, y= 210)
Button5= Button (ventana, text= "8", bg= color_boton, fg= color_texto, width= ancho_boton, height= alto_boton, command=lambda: btnClik (8)) .place (x= 105, y= 210)
Button6= Button (ventana, text= "9", bg= color_boton, fg= color_texto, width= ancho_boton, height= alto_boton, command=lambda: btnClik (9)) .place (x= 195, y= 210)
Button7= Button (ventana, text= "/", bg= color_boton, fg= color_texto, width= ancho_boton, height= alto_boton, command=lambda: btnClik ("/")) .place (x= 285, y= 210)
#FILA 3
Button8= Button (ventana, text= "4", bg= color_boton, fg= color_texto, width= ancho_boton, height= alto_boton, command=lambda: btnClik (4)) .place (x= 15, y= 270)
Button9= Button (ventana, text= "5", bg= color_boton, fg= color_texto, width= ancho_boton, height= alto_boton, command=lambda: btnClik (5)) .place (x= 105, y= 270)
Button10= Button (ventana, text= "6", bg= color_boton, fg= color_texto, width= ancho_boton, height= alto_boton, command=lambda: btnClik (6)) .place (x= 195, y= 270)
Button11= Button (ventana, text= "*", bg= color_boton, fg= color_texto, width= ancho_boton, height= alto_boton, command=lambda: btnClik ("*")) .place (x= 285, y= 270)
#FILA 4 
Button12= Button (ventana, text= "1", bg= color_boton, fg= color_texto, width= ancho_boton, height= alto_boton, command=lambda: btnClik (1)) .place (x= 15, y= 330)
Button13= Button (ventana, text= "2", bg= color_boton, fg= color_texto, width= ancho_boton, height= alto_boton, command=lambda: btnClik (2)) .place (x= 105, y= 330)
Button14= Button (ventana, text= "3", bg= color_boton, fg= color_texto, width= ancho_boton, height= alto_boton, command=lambda: btnClik (3)) .place (x= 195, y= 330)
Button15= Button (ventana, text= "-", bg= color_boton, fg= color_texto, width= ancho_boton, height= alto_boton, command=lambda: btnClik ("-")) .place (x= 285, y= 330)
#FILA 5
Button12= Button (ventana, text= "+", bg= color_boton, fg= color_texto, width= ancho_boton, height= alto_boton, command=lambda: btnClik ("+")) .place (x= 15, y= 390)
Button13= Button (ventana, text= "0", bg= color_boton, fg= color_texto, width= ancho_boton, height= alto_boton, command=lambda: btnClik (0)) .place (x= 105, y= 390)
Button14= Button (ventana, text= ".", bg= color_boton, fg= color_texto, width= ancho_boton, height= alto_boton, command=lambda: btnClik (".")) .place (x= 195, y= 390)
Buttonresultado= Button (ventana, text="=", bg=color_boton,fg= color_texto, width=ancho_boton, height=alto_boton, command=resultado) .place (x=285,y=330)

input_field = Entry(ventana, font=('arial', 20, 'bold'), textvariable=input_text, width=22, bd=20, insertwidth=4, bg="white", justify="right")
input_field.place(x=10, y=60)

clear_button = Button(ventana, text="C", bg=color_boton, fg=color_texto, width=ancho_boton, height=alto_boton, command=clear)
clear_button.place(x=195, y=150)

borrar_button = Button(ventana, text="⌫", bg=color_boton, fg=color_texto, width=ancho_boton, height=alto_boton, command=borrar_uno)
borrar_button.place(x=285, y=150)

clear()

ventana.mainloop ()

