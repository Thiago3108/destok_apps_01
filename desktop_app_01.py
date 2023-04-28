# se import a la libreria tkinter con todas sus funciones
from tkinter import *

#------------------------------
# funciones de la app
#------------------------------

#------------------------------
#ventana principal
#------------------------------

#se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objetp Tk()
ventana_principal = Tk()

#titulo de la ventana
ventana_principal.title("Sistemas uis socorro")

ventana_principal.geometry("500x500")

ventana_principal.resizable(0,0)

#color de fondo de la ventana
ventana_principal.config(bg="medium sea green")

#------------------------------
#frame entrada datos
#------------------------------

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="black", width=500, height=250)
frame_entrada.place(x = 0, y = 0)

#------------------------------
#frame operaciones
#------------------------------

frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="red", width=500, height=125)
frame_operaciones.place(x = 0, y = 250)


#------------------------------
#frame resultados
#------------------------------

frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="gold", width=500, height=125)
frame_resultados.place(x = 0, y = 375)





# run 
ventana_principal.mainloop()