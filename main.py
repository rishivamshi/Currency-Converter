# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 20:08:51 2017

@author: rishi
"""




from tkinter import *
import time
from currency_converter import CurrencyConverter as CC
import pandas as pd
import csv
from tables import createStandardTable as cst


def init():
    root=Tk()
    root.geometry("1600x800+0+0")
    root.title("Currency Converter")
    cInput=StringVar() 
    operator=""
    coi = 0.0

    Tops=Frame(root,width=1600,height=5,bg="sienna2",relief=SUNKEN)
    Tops.pack(side=TOP)

    f2=Frame(root,width=300,height=700,relief=SUNKEN)
    f2.pack(side=LEFT)
    f1=Frame(root,width=400,height=700,relief=SUNKEN)
    f1.pack(side = LEFT)
    f3=Frame(root,width=900,height=700,relief=SUNKEN)
    f3.pack(side=LEFT)

    localtime=time.asctime(time.localtime(time.time()))


    lblInfo=Label(Tops,font=('arial',50,'bold'),text="Currency Converter",fg ="sienna2",bd=10,anchor='w')
    lblInfo.grid(row=0,column=0)
    lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg ="sienna2",bd=10,anchor='w')
    lblInfo.grid(row=1,column=0)


def buttonClick(numbers):
    global operator
    operator=operator+str(numbers)
    cInput.set(operator)

def buttonClearDisplay():
    global coi
    coi = 0.0
    global operator
    operator = ""
    cInput.set(0.0)



newlist = [['','','','',0.0] for i in range(12)]

def Ref():
    
    
    cof=str(cFrom.get())
    cob=str(cTo.get())
   
    global coi
    coi = float(cInput.get())
    c = CC()
    value = c.convert(coi,cof,cob)
    Cost.set(value)
    
    global newlist

    for i in range(0,12):   
        newlist[i][1] = cof      
    
    x = ['USD','INR','GBP','AUD','EUR','BRL','CAD','CNY','HKD','JPY','NZD','SGD']
    y = ['US Dollar','Indian Ruppee','UK - Pound Sterling','Australian Dollar','EURO','Brazilian Real','Canadian Dollar','Yuan Renminbi - China','Honkong Dollar','Yen - Japan','New Zealand Dollar','Singapore Dollar']
       
    for j in range(0,len(x)):
        newlist[j][0] = y[x.index(cof)]
        newlist[j][2] = y[j]
        newlist[j][3] = x[j]
        newlist[j][4] = c.convert(coi,cof,x[j])
        
    my_df1 = pd.DataFrame(newlist)
    my_df1.columns = ['FROM COUNTRY','FROM COUNTRY CODE','TO COUNTRY','TO COUNTRY CODE','VALUE']
    my_df1.to_csv('list.csv',index=False,header = True)
    ct()

f = open("list.csv")
newtable = cst(f,f3)    

def createTableFrame():
    f = open("list.csv")
    global newtable
    newtable = cst(f,f3)
    newtable.grid(padx=20,pady=20)  

def ct():
    global newtable
    newtable.destroy()
    createTableFrame()
      
def qExit():
    root.destroy()
    
def Reset():    
    cFrom.set("USD")
    cTo.set("INR")
    Cost.set("")
    
  
def main():
    txtDisplay=Entry(f2,font=('arial',20,'bold'),textvariable=cInput,bd=30,insertwidth=4,bg="alice blue",justify='right')
    txtDisplay.grid(columnspan=4)
    button7=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),
                text="7",bg="gray50",command=lambda: buttonClick(7)).grid(row=2,column=0)
    button8=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),
                text="8",bg="gray50",command=lambda: buttonClick(8)).grid(row=2,column=1)
    button9=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),
                text="9",bg="gray50",command=lambda: buttonClick(9)).grid(row=2,column=2)



    button4=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),
                text="4",bg="gray50",command=lambda: buttonClick(4)).grid(row=3,column=0)
    button5=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),
                text="5",bg="gray50",command=lambda: buttonClick(5)).grid(row=3,column=1)
    button6=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),
                text="6",bg="gray50",command=lambda: buttonClick(6)).grid(row=3,column=2)




    button1=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),
                text="1",bg="gray50",command=lambda: buttonClick(1)).grid(row=4,column=0)
    button2=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),
                text="2",bg="gray50",command=lambda: buttonClick(2)).grid(row=4,column=1)
    button3=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),
                text="3",bg="gray50",command=lambda: buttonClick(3)).grid(row=4,column=2)




    button0=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),
                text="0",bg="gray50",command=lambda: buttonClick(0)).grid(row=5,column=0)
    buttonClear=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),
                text="C",bg="dark orange",command= buttonClearDisplay).grid(row=5,column=1)
    buttonEquals=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),
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

    lblCost=Label(f1,font=('arial',16,'bold'),text="------------",bd=16,anchor='w')
    lblCost.grid(row=3,column=0)
    lblCost=Label(f1,font=('arial',16,'bold'),text="-------------------------------------",bd=16,anchor='w')
    lblCost.grid(row=3,column=1)

    lblCost=Label(f1,font=('arial',16,'bold'),text="Conversion",bd=16,anchor='w')
    lblCost.grid(row=4,column=0)
    txtCost=Entry(f1,font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="#ffffff",justify="right")
    txtCost.grid(row=4,column=1)

    buttonTotal=Button(f1,padx=16,pady=16,bd=8,fg="white",font=('arial',16,'bold'),width=10,text="Total",bg="dark orange",command=Ref).grid(row=1,column=3)
    buttonReset=Button(f1,padx=16,pady=16,bd=8,fg="white",font=('arial',16,'bold'),width=10,text="Reset",bg="firebrick",command=Reset).grid(row=2,column=3)
    buttonExit=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',16,'bold'),width=10,text="Quit",bg="powder blue",command=qExit).grid(row=4,column=3)


    root.mainloop()


init()
main()
