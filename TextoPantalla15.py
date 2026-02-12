from tkinter import *
from tkinter import ttk
import tkinter
import webbrowser

def open_link():
    webbrowser.open("https://www.patreon.com/misa22/shop/overlay-notes-1326761?utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=productshare_creator&utm_content=join_link")

def atajo_teclado(event):
        #print(event.keysym)
        nuevoentry()#atajo teclado crea nuevo entry

def fuentemas(xnombre,tam):
        print("+")
        print(tam[0])
        tam[0]+=1
        xnombre.configure(font=("Arial",tam[0]))
        print("+")

def aumenta(event,xnombre,tam):
        tam[0]+=1
        xnombre.configure(font=("Arial",tam[0]))
    
def disminuye(event,xnombre,tam):
        tam[0]-=1
        xnombre.configure(font=("Arial",tam[0]))

def colorcam(event,xnombre,colores,colindex):
        if (colindex[0]< 2):
            colindex[0]+=1
        else:
            colindex[0]=0       
        xnombre.configure(foreground=(colores[colindex[0]]))

def color(xnombre,colores,colindex):
        print("c")
        print(colores[colindex[0]])
        if (colindex[0]< 2):
            colindex[0]+=1
        else:
            colindex[0]=0       
        
        xnombre.configure(foreground=(colores[colindex[0]]))
        print("c")

def fuentemenos(xnombre,tam):
        print("-")
        print(tam[0])
        tam[0]-=1
        xnombre.configure(font=("Arial",tam[0]))
        print("-")

def ocultartitulo(event,rootx):  
    #rootx.overrideredirect(True)
    print(event)

def visibilizar(event,ba,bd,bc):
    # print(event)
    # print(ba)
    # print(bc)
    # print(bd)
    if(ba.winfo_viewable()):
          ba.grid_forget()
    else:
        ba.grid(column=1, row=0)

    if(bd.winfo_viewable()):
          bd.grid_forget()
    else:
        bd.grid(column=2, row=0)

    if(bc.winfo_viewable()):
          bc.grid_forget()
    else:
        bc.grid(column=3, row=0)



def nuevoentry():
    tam=[20] #la paso como lista para poderla modificar en la funcin
    colindex=[0]
    colores=['red','blue','green']
    rootx = Tk()
    #rootx = Toplevel()# sugerido por chargpt pero me genera una ventana demas
    rootx.attributes('-topmost',True)#encima de todo
    rootx.title("etiqueta")
    x, y = rootx.winfo_pointerxy()
    rootx.geometry("+{}+{}".format(x, y))
    #asi lanzo los entry donde quedo el cursor

#     rootx.wait_visibility(rootx)
#     rootx.wm_attributes("-alpha", 0.5)

    rootx.bind('<B2-Motion>', lambda e:  rootx.geometry("+{}+{}".format(e.x_root, e.y_root)))
    #con click del medio muevo los entry

    #rootx.overrideredirect(True)#sin barra de titulo
    #no me deja escribir en el entry

    

    #rootx.attributes('-alpha', 0) trasparente no funciona

    rootx.rowconfigure(0, weight=1)# hay que especificarle al root tambien
    rootx.columnconfigure(0, weight=1)# hay que especificarle al root tambien
    rootx.minsize(100,20)
    frmx = ttk.Frame(rootx)
    frmx.grid(sticky='nsew')# el frame pegado a la ventana
    frmx.rowconfigure(index=0,weight=1)
    frmx.columnconfigure(index=0,weight=1)

    style = ttk.Style()
    style.theme_use('clam')  # Use a theme that supports transparency
    style.configure('Transparent.TEntry', background='SystemTransparent')  # Set background to transparent
    print("tam es "+str(tam))

        #entry no me toma widget
    rootx.wm_attributes("-alpha", 0.5)
    frase = StringVar()
    xnombre = ttk.Entry(frmx,justify=tkinter.CENTER, textvariable=frase,width=20,style='Transparent.TEntry')
    xnombre.grid(column=0, row=0,sticky='nsew')
    


    

    print(xnombre.configure().get('style'))

    ba=ttk.Button(frmx,text="+",command=lambda: fuentemas(xnombre,tam))
    ba.grid(column=1, row=0,sticky='nsew')

    aumenta_arg = lambda event: aumenta(event,xnombre,tam)


    rootx.bind('+',aumenta_arg)# + aumenta

    bd=ttk.Button(frmx,text="-",command=lambda: fuentemenos(xnombre,tam))
    bd.grid(column=2, row=0,sticky='nsew')

    disminuye_arg = lambda event: disminuye(event,xnombre,tam)
    rootx.bind('-',disminuye_arg)# - disminuy


    bc=ttk.Button(frmx,text="c",command=lambda: color(xnombre,colores,colindex))
    bc.grid(column=3, row=0,sticky='nsew')

    colorcam_arg = lambda event: colorcam(event,xnombre,colores,colindex)
    rootx.bind('c',colorcam_arg)# c cambia color


    visibilizar_argu = lambda event: visibilizar(event,ba,bd,bc)

    rootx.bind('<Alt_L>',visibilizar_argu)#toco alt para configurar + - color


    ocultartitulo_argu = lambda event: ocultartitulo(event,rootx)
    rootx.bind('<Shift_L>',ocultartitulo_argu)#toco Shift_L para ocultar titulo


    rootx.mainloop()

#estas 3 me duplican una ventana
# estilo = ttk.Style()
# estilo.theme_use('clam')  
# estilo.configure('Transparent.TFrame', background='systemTransparent')

root = Tk()
# icono = tkinter.PhotoImage(file="IconoHL2.png")
# root.iconphoto(True, icono)
#no levanta imagen ?ruta mal
root.title("Principal")
#root.overrideredirect(True)
root.wait_visibility(root)
root.wm_attributes("-alpha", 0.5)

root.rowconfigure(0, weight=1)# hay que especificarle al root tambien
root.columnconfigure(0, weight=1)# hay que especificarle al root tambien
root.minsize(100,100)
frm = ttk.Frame(root,style='Transparent.TFrame')
#frm.place(relx=0, rely=0, relwidth=1, relheight=1)  #comentado 10/4
frm.grid(sticky='nsew')# el frame pegado a la ventana

frm.rowconfigure(index=0,weight=1)
frm.columnconfigure(index=0,weight=1)

frase = StringVar()
enombre = ttk.Entry(frm, textvariable=frase,width=20)
enombre.grid(column=0, row=0,sticky='nsew')
#no cumple rol en el principal #comantado 10/4

menubar = Menu(root)


file = Menu(menubar, tearoff = 1)
menubar.add_cascade(label ='NewText', menu = file)
#menubar.add_cascade(label ='Donate',command=open_link)

donate_menu = Menu(menubar, tearoff=1)
menubar.add_cascade(label='Donate', menu=donate_menu)
donate_menu.add_command(label='Go Patreon', command=open_link)

 #segun chatpgt se ejecutaba nuevoentry al cargar el programa
file.add_command(label ='Nuevo Texto',command= lambda: nuevoentry())  #asi no la deberia llamar




root.bind('<Control_L><n>', atajo_teclado)

root.config(menu = menubar) 
root.mainloop()