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

ventana_principal.geometry("1000x700")

ventana_principal.resizable(0,0)

#color de fondo de la ventana
ventana_principal.config(bg="blue4")

#------------------------------
#frame 1
#------------------------------

frame_1 = Frame(ventana_principal)
frame_1.config(bg="snow", width=250, height=300)
frame_1.place(x = 0, y = 0)

#------------------------------
#frame 2
#------------------------------

frame_2 = Frame(ventana_principal)
frame_2.config(bg="red", width=200, height=250)
frame_2.place(x = 0, y = 0)


#------------------------------
#frame 3
#------------------------------

frame_3 = Frame(ventana_principal)
frame_3.config(bg="snow", width=250, height=300)
frame_3.place(x = 0, y = 400)

#------------------------------
#frame 4
#------------------------------
frame_4 = Frame(ventana_principal)
frame_4.config(bg="red", width=200, height=250)
frame_4.place(x = 0, y = 450)

#------------------------------
#frame 5
#------------------------------
frame_5 = Frame(ventana_principal)
frame_5.config(bg="snow", width=650, height=300)
frame_5.place(x = 350, y = 0)

#------------------------------
#frame 6
#------------------------------
frame_6 = Frame(ventana_principal)
frame_6.config(bg="red", width=600, height=250)
frame_6.place(x = 400, y = 0)

#------------------------------
#frame 7
#------------------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="snow", width=650, height=300)
frame_resultados.place(x = 350, y = 400)

#------------------------------
#frame 8
#------------------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="red", width=600, height=250)
frame_resultados.place(x = 400, y = 450)

# run 
ventana_principal.mainloop()