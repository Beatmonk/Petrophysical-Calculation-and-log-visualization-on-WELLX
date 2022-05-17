from tkinter import *
from tkinter.ttk import Combobox
from tkinter import scrolledtext

import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import Tobabackend


import matplotlib.pyplot as plt



window = Tk()
window.title("TOBA PETROPHYSICAL CALCULATOR")
window.geometry('600x370')
window.configure(bg="lightgreen")
mainframe=Frame(window,bg="red",width=100, highlightthickness=3)
window.resizable(width=False,height=False)
window.iconbitmap("T.ico")


#window.overrideredirect(True)


frame1=Frame(window,height= 10,width=10,bg="lightgreen" ,bd=1, relief=FLAT)
frame1.grid(column=2,row=6)

frame2=Frame(window,height= 20,width=10,bg="lightgreen" ,bd=1, relief=FLAT)
frame2.grid(column=2,row=16)

#frame3=Frame(window,height= 20,width=10,bg="violet" ,bd=1, relief=FLAT)
#frame3.grid(column=2,row=18)

menu=Menu(window)
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0, bg="antique white")
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Save as...")
filemenu.add_command(label="Close")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)



editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo")
editmenu.add_separator()
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
editmenu.add_command(label="Delete")
editmenu.add_command(label="Select All")
menubar.add_cascade(label="Edit")



helpmenu = Menu(menubar)
helpmenu.add_command(label="Help Index")
helpmenu.add_command(label="About...")
menubar.add_cascade(label="Help")


window.config(menu=menubar)



def CalculateIGR_command():
    grlog = float(e1.get())
    grmin = float(e2.get())
    grmax = float(e3.get())
    igr = Tobabackend.Gamma_Ray_index(grlog, grmin,grmax)
    e16.delete(0, END)
    e16.insert(END, "{:.2f}".format(igr))



def calculateDenPOR_command():

    rhoma = float(e4.get())
    rhob = float(e5.get())
    rhof = float(e6.get())
    Denpor = Tobabackend.DEN_POR(rhoma, rhob, rhof)
    
    e17.delete(0, END)
    e17.insert(END, "{:.2f}".format(Denpor))



    



    
    
def calculateVsh_command():
    Igr = float(e16.get())
    
    vsh = Tobabackend.Shale_volume(Igr)
    
    e13.delete(0, END)
    e13.insert(END, "{:.2f}".format(vsh))
    
    
def calculateEDenPor_command():
    vsh = float(e13.get())
    ShPor= float(e12.get())
    Denpor= float (e17.get())
    EDenPor = Tobabackend.EFF_DenPor(vsh,ShPor,Denpor) 
    e20.delete(0, END)
    e20.insert(END, "{:.2f}".format(EDenPor))
    
    
def calculateENPOR_command():
    vsh = float(e13.get())
    SHNPOR= float(e8.get())
    NPOR= float (e11.get())
    ENPOR = Tobabackend.EFFNPOR(vsh,SHNPOR,NPOR) 
    e26.delete(0, END)
    e26.insert(END, "{:.2f}".format(ENPOR))    
    
    
def calculateNDPOR_command():  
    EDenPor = float (e20.get())
    ENPOR = float(e26.get())
    NDPOR = Tobabackend.Porosity(EDenPor,ENPOR)
    e25.delete(0, END)
    e25.insert(END, "{:.2f}".format(NDPOR))
    
    
def calculateWater_porosity_command():  
    WDENPOR = float (e49.get())
    WNPOR = float(e50.get())
    WPOR = Tobabackend.Water_porosity(WNPOR,WDENPOR)
    e48.delete(0, END)
    e48.insert(END, "{:.2f}".format(WPOR))

def calculateRW_FT_command():
    
    WPOR = float(e48.get())
    M = float(e9.get())
    A = float(e10.get())
    ro = float(e55.get())
    RW = Tobabackend.RW_FT(WPOR,A,ro,M)
    e15.delete(0, END)
    e15.insert(END, "{:.2f}".format(RW))
    
    

def calculateAPPARENT_WATER_RESISTIVITY_command():
    RESD = float(e22.get())
    Denpor = float(e17.get())
    M = float(e9.get())
    A = float(e10.get())
    rwa = Tobabackend.APPARENT_WATER_RESISTIVITY(RESD, Denpor, M, A)
    e.delete(0, END)
    e.insert(END, "{:.2f}".format(rwa))
    
    
    
def calculatearchieSw_command():
    RWA = float(e.get())
    RW = float(e15.get())
    N = float(e14.get())
  
    sw = Tobabackend.Water_Saturation(RW,RWA,N)
    
    e18.delete(0, END)
    e18.insert(END, "{:.2f}".format(sw))    
    
    
    
def calculateSWIR_command():
    NDPOR = float(e25.get())
    M = float(e9.get())
    A = float(e10.get())
    RW = float(e20.get())
    N = float(e14.get())
    RT = float(e15.get())
    swir = Tobabackend.SWIR(RW,NDPOR,M,A,N,RT)
    
    e24.delete(0, END)
    e24.insert(END, "{:.2f}".format(swir))
    
    

 
l1 =Label(window, text="GRlog ", bg="lavender")
l1.grid(row =0, column =0)

l2 =Label(window, text="GRmin", bg="lavender")
l2.grid(row =0, column =2)

l3 =Label(window, text="GRmax", bg="lavender")
l3.grid(row =0, column =4)


grlog_text = StringVar()
e1 = Entry(window, textvariable = grlog_text,width=10,borderwidth=3, bg="antique white")
e1.grid(row = 0, column = 1)
grlog_text.set('50')

grmin_text = StringVar()
e2 = Entry(window, textvariable = grmin_text,width=10,borderwidth=3, bg="antique white")
e2.grid(row = 0, column = 3)
grmin_text.set('20')

grmax_text = StringVar()
e3 = Entry(window, textvariable = grmax_text,width=10,borderwidth=3, bg="antique white")
e3.grid(row = 0, column = 5)
grmax_text.set('75')

b1 = Button(window, text = "Calculate IGR",pady=2,padx=2, command=CalculateIGR_command) #height =10, width = 10
b1.grid(row =3, column=0)

e16=Entry(window,width=10,borderwidth=3, bg="antique white")
e16.grid(row=3,column=1)

b5 = Button(window, text = "Calculate Vsh",pady=2,padx=2, command=calculateVsh_command) #height =10, width = 10
b5.grid(row =3, column=2)

e13=Entry(window,width=10,borderwidth=3, bg="antique white")
e13.grid(row=3,column=3)

l4 =Label(window, text="RHOma", bg="lavender")
l4.grid(row =5, column =0)

l5 =Label(window, text="RHOb", bg="lavender")
l5.grid(row =5, column =2)

l6 =Label(window, text="RHOf", bg="lavender")
l6.grid(row =5, column =4)

l12 =Label(window, text="NPOR", bg="lavender")
l12.grid(row =7, column =2)

l11 =Label(window, text="DENSHPOR", bg="lavender")
l11.grid(row =7, column =4)


DENSHPOR_text = StringVar()
e12 = Entry(window, textvariable = DENSHPOR_text,width=10,borderwidth=3, bg="antique white")
e12.grid(row = 7, column = 5)
DENSHPOR_text.set('1')


rhob_text = StringVar()
e5 = Entry(window, textvariable = rhob_text,width=10,borderwidth=3, bg="antique white")
e5.grid(row = 5, column = 3)
rhob_text.set('1.65')


rhomax_text = StringVar()
e4 = Entry(window, textvariable = rhomax_text,width=10,borderwidth=3, bg="antique white")
e4.grid(row = 5, column = 1)
rhomax_text.set('2.65')

rhob_text = StringVar()
e5 = Entry(window, textvariable = rhob_text,width=10,borderwidth=3, bg="antique white")
e5.grid(row = 5, column = 3)
rhob_text.set('1.65')

rhof_text = StringVar()
e6 = Entry(window, textvariable = rhof_text,width=10,borderwidth=3, bg="antique white")
e6.grid(row = 5, column = 5)
rhof_text.set('1')

b2 = Button(window, text = "Calculate DenPOR",pady=2,padx=2, width= 13, command=calculateDenPOR_command) #height =10, width = 10
b2.grid(row =7, column=0)

e17=Entry(window,width=10,borderwidth=3, bg="antique white")
e17.grid(row=7,column=1)


NPOR_text = StringVar()
e11=Entry(window,textvariable = NPOR_text, width=10 ,borderwidth=3, bg="antique white")
e11.grid(row=7,column=3)
NPOR_text.set('0.45')


b2 = Button(window, text = "Calc EDenPOR",pady=2,padx=2, width= 13,command=calculateEDenPor_command) #height =10, width = 10
b2.grid(row =8, column=0)

e20=Entry(window,width=10,borderwidth=3, bg="antique white")
e20.grid(row=8,column=1)





l8 =Label(window, text="SHNPOR", bg="lavender")
l8.grid(row =8, column =2)

SHNPOR_text = StringVar()
e8 = Entry(window,textvariable= SHNPOR_text, width=10,borderwidth=3, bg="antique white")
e8.grid(row = 8, column = 3)
SHNPOR_text.set('2.65')



b2 = Button(window, text = "Calc NDPOR",pady=2,padx=2, width= 13, command=calculateNDPOR_command) #height =10, width = 10
b2.grid(row =9, column=0)

#NDPor_text = StringVar()
e25 = Entry(window,width=10,borderwidth=3, bg="antique white")
e25.grid(row = 9, column = 1)
#NDPor_text.set('2.65')




b26 = Button(window, text = "Calc ENPOR",pady=2,padx=2, width= 13, command=calculateENPOR_command) #height =10, width = 10
b26.grid(row =8, column=4)

e26 = Entry(window,width=10,borderwidth=3, bg="antique white")
e26.grid(row = 8, column = 5)



l9 =Label(window, text="m", bg="lavender")
l9.grid(row =17, column =2)

l9 =Label(window, text="a", bg="lavender")
l9.grid(row =17, column =0)







M_text = StringVar()
e9 = Entry(window, textvariable = M_text,width=10,borderwidth=3, bg="antique white")
e9.grid(row = 17, column = 3)
M_text.set('2.15')

A_text = StringVar()
e10 = Entry(window, textvariable = A_text,width=10,borderwidth=3, bg="antique white")
e10.grid(row = 17, column = 1)
A_text.set('0.62')





l10 =Label(window, text="RESD", bg="lavender")
l10.grid(row =17, column =4)


RESD_text = StringVar()
e22 = Entry(window, textvariable = RESD_text,width=10,borderwidth=3, bg="antique white")
e22.grid(row = 17, column = 5)
RESD_text.set('1.65')


l14 =Label(window, text="n", bg="lavender")
l14.grid(row =18, column =0)


N_text = StringVar()
e14 = Entry(window, textvariable = N_text,width=10,borderwidth=3, bg="antique white")
e14.grid(row = 18, column = 1)
N_text.set('2')


#l15 =Label(window, text="RW", bg="lavender")
#l15.grid(row =18, column =0)

b15 = Button(window, text = "Calculate RW",pady=2,padx=2,command=calculateRW_FT_command) #height =10, width = 10
b15.grid(row =20, column=2)

#RW_text = StringVar()
e15 = Entry(window,width=10,borderwidth=3, bg="antique white")
e15.grid(row = 20, column = 3)
#RW_text.set('1.65')


b3 = Button(window, text = "Calculate RWa",pady=2,padx=2,command=calculateAPPARENT_WATER_RESISTIVITY_command) #height =10, width = 10
b3.grid(row =21, column=0)

e=Entry(window,width=10,borderwidth=3, bg="antique white")
e.grid(row=21,column=1)


l7 =Label(window, text="Ro", bg="lavender")
l7.grid(row =18, column =2)

ro_text = StringVar()
e55 = Entry(window, textvariable = ro_text,width=10,borderwidth=3, bg="antique white")
e55.grid(row = 18, column = 3)
ro_text.set('0')


l50 =Label(window, text="WNPOR", bg="lavender")
l50.grid(row =18, column =4)

WNPOR_text = StringVar()
e50 = Entry(window, textvariable = WNPOR_text,width=10,borderwidth=3, bg="antique white")
e50.grid(row = 18, column = 5)
WNPOR_text.set('0')


l49 =Label(window, text="WDENPOR", bg="lavender")
l49.grid(row =19, column =0)

WDENPOR_text = StringVar()
e49 = Entry(window, textvariable = WDENPOR_text,width=10,borderwidth=3, bg="antique white")
e49.grid(row = 19, column = 1)
WDENPOR_text.set('0')


b48 = Button(window, text = "Calculate  WPOR",pady=2,padx=2,command=calculateWater_porosity_command) #height =10, width = 10
b48.grid(row =20, column=0)

WPOR_text = StringVar()
e48 = Entry(window, textvariable = WPOR_text, width=10,borderwidth=3, bg="antique white")
e48.grid(row = 20, column = 1)
WPOR_text.set('0')


#l16 =Label(window, text="F",fg=('darkseagreen4'))
#l16.grid(row =13, column =2)
#f_text = StringVar()
#e20 = Entry(window, textvariable = f_text,width=10,borderwidth=3)
#e20.grid(row = 13, column = 3)
#f_text.set('1.65')









b4 = Button(window, text = "Calculate ArchieSw",pady=2,padx=2, command=calculatearchieSw_command) #height =10, width = 10
b4.grid(row =23, column=0)

e18=Entry(window,width=10,borderwidth=3, bg="antique white")
e18.grid(row=23,column=1)

#b23 = Button(window, text = "Calculate SimandouxSw",pady=2,padx=2) #command=calculateSw_command) #height =10, width = 10
#b23.grid(row =20, column=2)

#e23=Entry(window,width=10,borderwidth=3, bg="antique white")
#e23.grid(row=20,column=3)

b24 = Button(window, text = "Calculate SWIR",pady=2,padx=2,command=calculateSWIR_command) #height =10, width = 10
b24.grid(row =23, column=4)

e24=Entry(window,width=10,borderwidth=3, bg="antique white")
e24.grid(row=23,column=5)

#b25 = Button(window, text = "Permeabilty",pady=2,padx=2) #command=calculateSw_command) #height =10, width = 10
#b25.grid(row =21, column=0)

#e25=Entry(window,width=10,borderwidth=3, bg="antique white")
#e25.grid(row=21,column=1)




window.mainloop()