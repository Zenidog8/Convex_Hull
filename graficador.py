import turtle
import gc
import geometriaComputacional as gc
import Tkinter

# Seteo de algunas cosas

ventana = turtle.Screen()
ventana.setup(640, 540, 400, 200)
ventana.title("Visualizacion de la envolvente")
tortu = turtle.Turtle()
tortu.speed(0)
s = 240
escala = 5


def dibujar_plano(s):
    '''
    Dibuja el plano donde se graficatan los puntos
    '''
    tortu.speed(0)
    tortu.setpos(0, 0)
    tortu.ht()
    tortu.color("blue")
    tortu.pensize(3)

    for i in range(4):
        tortu.fd(s)
        tortu.pu()
        tortu.goto(0, 0)
        tortu.pd()
        tortu.lt(90)

    tortu.ht()


def dibujar_punto(a, b):
    '''
    Dibuja un punto con escala de 3x
    '''
    tortu.pensize(3)
    tortu.speed(1)
    tortu.ht()
    tortu.penup()
    tortu.setpos(a * 3, b * 3)
    tortu.pendown()
    tortu.dot(8, 0, 0, 0)


def graficar_puntos(puntos):
    '''
    Dibuja el vector de puntos
    '''
    for i in range(0, len(puntos)):
        dibujar_punto(puntos[i][0], puntos[i][1])


def marcarVector(a, b, c, d):
    '''
    Dibuja una raya entre dos puntos de un plano
    '''
    tortu.pensize(3)
    tortu.speed(1)
    tortu.ht()
    tortu.penup()
    tortu.setpos(c * 3, d * 3)
    tortu.pendown()
    tortu.color("red")
    tortu.goto(a * 3, b * 3)


def marcarPerimetro(puntos):
    '''
    Dibuja todo el perimetro del convex hull
    '''
    for i in range(0, len(puntos)):
        marcarVector(puntos[i][0], puntos[i][1], puntos[i - 1][0], puntos[i - 1][1])


def escribir_area(s):
    '''
    Escribe en la esquina superior izquierda del plano el area del poligono
    '''
    tortu.color("black")
    tortu.speed(0)
    tortu.penup()
    tortu.goto(-240, 240)
    tortu.pendown()
    tortu.write(s, False, align="center")

#Centra la ventana
def centrar(ventana):
    ventana.update_idletasks()
    w=ventana.winfo_width()
    h=ventana.winfo_height()
    extraW=ventana.winfo_screenwidth()-w
    extraH=ventana.winfo_screenheight()-h
    ventana.geometry("%dx%d%+d%+d" % (w,h,extraW/2,extraH/2))

def main(pCantidad):

    def cerrarVentana():
        ventanaPrincipal.destroy()
    #VENTANA PARES
    ventanaPrincipal = Tkinter.Tk()
    ventanaPrincipal.title("Pares Ordenados")
    ventanaPrincipal.geometry("270x250")
    centrar(ventanaPrincipal)
    
    lblInstruccion = Tkinter.Label(ventanaPrincipal, text= "    Los pares generados son:")
    lblInstruccion.pack()
    lblInstruccion.place(x=20,y=10)

    btnCerrar = Tkinter.Button(ventanaPrincipal, text = "Cerrar", command = cerrarVentana)
    btnCerrar.pack()
    btnCerrar.place(x=130, y=80)
    
    dibujar_plano(s)
    global cantidad
    cantidad = pCantidad
    puntosA = gc.generarPuntos(cantidad)

    #Desplegar los pares en pantalla
    pares = ""
    for i in range(cantidad):
        pares = pares + "\n" + str(i+1) + ") " + str(puntosA[i])
    lblPuntos = Tkinter.Label(ventanaPrincipal, text= pares).place(x=30,y=30)
    
    con = gc.convexhull(puntosA)
    graficar_puntos(puntosA)
    marcarPerimetro(con)
    escribir_area("Area del poligono: " + str(gc.calcularArea(con)))

    ventana.exitonclick()

    ventanaPrincipal.mainloop()


if __name__ == '__main__':
    main()
