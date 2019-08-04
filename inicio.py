import Tkinter
import sys
import tkMessageBox
    
#Centra la ventana
def centrar(ventana):
    ventana.update_idletasks()
    w=ventana.winfo_width()
    h=ventana.winfo_height()
    extraW=ventana.winfo_screenwidth()-w
    extraH=ventana.winfo_screenheight()-h
    ventana.geometry("%dx%d%+d%+d" % (w,h,extraW/2,extraH/2))
    
def main():

    def tomarDatos():
        #Valida que el numero de puntos esta en el rango
        if (txtCantidad.get() == "") or (txtCantidad.get().isalpha() or (int(txtCantidad.get())<1) or (int(txtCantidad.get())>100)):
            tkMessageBox.showwarning('Atencion', 'Debe ingresar un numero entero entre 1 y 100.')
        else:
            global cantidad
            cantidad = int(txtCantidad.get())
            ventanaPrincipal.destroy()
            import graficador as g
            g.main(cantidad)            
            
    #VENTANA Inicial
    ventanaPrincipal = Tkinter.Tk()
    ventanaPrincipal.title("Datos de entrada")
    ventanaPrincipal.geometry("350x200")
    centrar(ventanaPrincipal)

    #OBJETOS PARA LA ENTRADA DE DATOS
    lblInstruccion = Tkinter.Label(ventanaPrincipal, text= "  Digite la cantidad de puntos a generar:")
    lblInstruccion.pack()
    lblInstruccion.place(x=20,y=10)
    btnAceptar = Tkinter.Button(ventanaPrincipal, text = "Aceptar", command = tomarDatos)
    btnAceptar.pack()
    btnAceptar.place(x=60, y=100)
    txtCantidad = Tkinter.Entry(ventanaPrincipal)
    txtCantidad.pack(padx=30, pady=50, ipadx=5, ipady=5)
    
    ventanaPrincipal.mainloop()
    

if __name__ == '__main__':
    main()

