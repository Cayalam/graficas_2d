from tkinter import PhotoImage,Tk,Frame,BOTH,Canvas
from tracemalloc import start
import random


# Variables Glovales
BASE= 460
ALTURA= 380

ventana_principal= Tk()
ventana_principal.title("Graficas 2D_ TEXTO")
ventana_principal.resizable(False,False)
ventana_principal.config(bg="blue")

# Frame de Graficacion
frame_graficacion=Frame(ventana_principal)
frame_graficacion.config(bg="white", width=480,height=400)
frame_graficacion.pack(fill=BOTH, padx=10,pady=10 )
# Creacion canvas
C=Canvas(frame_graficacion, width=BASE, height=ALTURA)
C.place(x=10, y=10)

# Texto
texto =C.create_text(BASE/2,ALTURA/2,anchor="center",text="UIS Socorro",font=["Arial", "30" ,"bold"],fill="blue",activefill="red")

# lineas
#linea1= C.create_line(0,0,BASE,ALTURA,fill="green")
#linea2= C.create_line(0,ALTURA,BASE,0, fill= "green")
#linea2= C.create_line(230,0,230,360,fill="red")
#linea2= C.create_line(0,190,460,190,fill="red")

#for i in range(100):
    #X1=BASE
   # Y1=ALTURA
    #X2=X1+20
    #Y2=Y1+20
    #color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
    #i=C.create_oval(X1,Y1,X2,Y2, fill=color)
    #X1=random.randint(0,BASE-20)
    #Y1=random.randint(0,ALTURA-20)
   
   

    
    


# Cuadrados y rectangulos
#rect1=C.create_rectangle(10,10,BASE/2-10,ALTURA/2-10,fill="pink",outline="pink")
#rect2=C.create_rectangle(10,10,110,110,fill="green")
#oli1= C.create_polygon(0,ALTURA,BASE/2,0,BASE,ALTURA,fill="green",outline="red",width=5)

#rombo = C.create_polygon(0, ALTURA/2, BASE/2,0, BASE, ALTURA/2, BASE/2, ALTURA, fill="yellow", outline="green")
# Elipses  o circulos
#elip1=C.create_oval(0,0,BASE,ALTURA,fill="pink")
#arc1=C.create_arc(10,10,210,210,start=45,extent=90)
X1=0
Y1=0
for i in range(100):
    
    color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
    i=C.create_oval(X1,Y1,X1+20,Y1+20, fill=color)
    X1=random.randint(0,BASE-20)
    Y1=random.randint(0,ALTURA-20)
Img=PhotoImage(file="balon-futbol-04.gif")
pelota=C.create_image(300,300,image=Img, anchor="center")
    




# Deaplegar ventana principal.Queda a la espera de eventos
ventana_principal.mainloop()

