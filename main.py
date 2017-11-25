# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 20:08:51 2017

@author: rishi
"""




from tkinter import *
import time
from currency_converter import CurrencyConverter

root=Tk()
root.geometry("1600x800+0+0")
root.title("Currency Converter")
cInput=StringVar() 
operator=""
coi = 0.0

Tops=Frame(root,width=1600,height=50,bg="sienna2",relief=SUNKEN)
Tops.pack(side=TOP)

f2=Frame(root,width=300,height=700,relief=SUNKEN)
f2.pack(side=LEFT)
f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side = LEFT)
localtime=time.asctime(time.localtime(time.time()))


lblInfo=Label(Tops,font=('arial',50,'bold'),text="Currency Converter",fg ="sienna2",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg ="sienna2",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)


def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    cInput.set(operator)

def btnClearDisplay():
    global coi
    coi = 0.0
    global operator
    operator = ""
    cInput.set(0.0)




     
      
def Ref():
    
    
    cof=str(cFrom.get())
    cob=str(cTo.get())
    
    
    global coi
    coi = float(cInput.get())
    c = CurrencyConverter()
    value = c.convert(coi,cof,cob)
    Cost.set(value)
    
    

def qExit():
    root.destroy()
    
def Reset():
    
    cFrom.set("USD")
    cTo.set("INR")
    Cost.set("")
    


  
txtDisplay=Entry(f2,font=('arial',20,'bold'),textvariable=cInput,bd=30,insertwidth=4,bg="alice blue",justify='right')
txtDisplay.grid(columnspan=4)
btn7=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),
            text="7",bg="gray50",command=lambda: btnClick(7)).grid(row=2,column=0)
btn8=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),
            text="8",bg="gray50",command=lambda: btnClick(8)).grid(row=2,column=1)
btn9=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),
            text="9",bg="gray50",command=lambda: btnClick(9)).grid(row=2,column=2)



btn4=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),
            text="4",bg="gray50",command=lambda: btnClick(4)).grid(row=3,column=0)
btn5=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),
            text="5",bg="gray50",command=lambda: btnClick(5)).grid(row=3,column=1)
btn6=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),
            text="6",bg="gray50",command=lambda: btnClick(6)).grid(row=3,column=2)




btn1=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),
            text="1",bg="gray50",command=lambda: btnClick(1)).grid(row=4,column=0)
btn2=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),
            text="2",bg="gray50",command=lambda: btnClick(2)).grid(row=4,column=1)
btn3=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),
            text="3",bg="gray50",command=lambda: btnClick(3)).grid(row=4,column=2)




btn0=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),
            text="0",bg="gray50",command=lambda: btnClick(0)).grid(row=5,column=0)
btnClear=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),
            text="C",bg="dark orange",command= btnClearDisplay).grid(row=5,column=1)
btnEquals=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),
            text="=",bg="dark orange",command= Ref).grid(row=5,column=2)










cFrom=StringVar()
cTo=StringVar()

cFrom.set("USD")
cTo.set("INR")
cInput.set(0.0)

Cost=StringVar()



lblcFrom=Label(f1,font=('arial',16,'bold'),text="FROM",bd=16,anchor='w')
lblcFrom.grid(row=1,column=0)
txtcFrom=Entry(f1,font=('arial',16,'bold'),textvariable=cFrom,bd=10,insertwidth=4,bg="alice blue",justify="right")
txtcFrom.grid(row=1,column=1)

lblcTo=Label(f1,font=('arial',16,'bold'),text="TO",bd=16,anchor='w')
lblcTo.grid(row=2,column=0)
txtcTo=Entry(f1,font=('arial',16,'bold'),textvariable=cTo,bd=10,insertwidth=4,bg="alice blue",justify="right")
txtcTo.grid(row=2,column=1)



lblCost=Label(f1,font=('arial',16,'bold'),text="Conversion",bd=16,anchor='w')
lblCost.grid(row=1,column=2)
txtCost=Entry(f1,font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="#ffffff",justify="right")
txtCost.grid(row=1,column=3)

btnTotal=Button(f1,padx=16,pady=16,bd=8,fg="white",font=('arial',16,'bold'),width=10,text="Total",bg="dark orange",command=Ref).grid(row=7,column=1)
btnReset=Button(f1,padx=16,pady=16,bd=8,fg="white",font=('arial',16,'bold'),width=10,text="Reset",bg="firebrick",command=Reset).grid(row=7,column=2)
btnExit=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',16,'bold'),width=10,text="Quit",bg="powder blue",command=qExit).grid(row=7,column=3)




root.mainloop()


