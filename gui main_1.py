# -*- coding: utf-8 -*-ss
"""
Created on Tue May  4 17:28:41 2021

@author: user
"""

from tkinter import *
import tkinter as tk


from PIL import Image ,ImageTk

from tkinter.ttk import *
from pymsgbox import *


root=tk.Tk()

root.title(" ")
w,h = root.winfo_screenwidth(),root.winfo_screenheight()

image2 =Image.open('dash.jpg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)
#, relwidth=1, relheight=1)

#w = tk.Label(root, text="Medical Chatbot using BMI Calculator",width=40,background="brown",fg="White",height=2,font=("Times new roman",19,"bold"))
#w.place(x=450,y=20)



w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.configure(background="skyblue")


from tkinter import messagebox as ms




def Book():
    from subprocess import call
    call(["python","doctors information.py"])

def log():
    from subprocess import call
    call(["python","GUI_main.py"])

def chatbot():
    from subprocess import call
    call(["python","CHAT_1.py"])
    
def BMI():
    from subprocess import call
    call(["python","BMI.py"])
    
    
    
   # background_label.place(x=0, y=0) #, relwidth=1, relheight=1)
# #
lbl = tk.Label(root, text="Innovative Virtual Healthcare Assistant With BMI Calculator", font=('times', 35,' bold '), width=50,height=1,bg="black",fg="white")
lbl.place(x=0, y=0)


#frame_display = tk.LabelFrame(root, text=" --Display-- ", width=900, height=250, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
#frame_display.grid(row=0, column=0, sticky='nw')
#frame_display.place(x=300, y=100)

#frame_display1 = tk.LabelFrame(root, text=" --Result-- ", width=900, height=200, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
#frame_display1.grid(row=0, column=0, sticky='nw')
#frame_display1.place(x=300, y=430)

#frame_display2 = tk.LabelFrame(root, text=" --Calaries-- ", width=900, height=50, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
#frame_display2.grid(row=0, column=0, sticky='nw')
#frame_display2.place(x=300, y=380)

frame_alpr = tk.LabelFrame(root, text=" --Chatbot-- ", width=500, height=350, bd=5, font=('times', 14, ' bold '),bg="SeaGreen1")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=500, y=200) 
    
lbl = tk.Label(root, text="Chatbots are not just software in the modern era. \n Chatbots are like our personal assistants\n who understand us and can be microconfigured.\n They remember our likes and dislikes and \n never tend to disappoint us by \n forgetting what we taught them already, \n and this is the reason why \n everyone loves chatbot.", font=('times', 15,' bold '), width=40,height=10,bg="SeaGreen1",fg="black")
lbl.place(x=500, y=300)
    
    
    
    
    
    
    
    





d2=tk.Button(root,text="Home",command=log,width=15,height=2,bd=2,background="black",foreground="white",font=("times new roman",14,"bold"))
d2.place(x=400,y=100)

# d2=tk.Button(root,text="About Us",width=15,height=2,bd=2,background="black",foreground="white",font=("times new roman",14,"bold"))
# d2.place(x=400,y=100)

d2=tk.Button(root,text="Medical Chatbot",command=chatbot,width=15,height=2,bd=2,background="black",foreground="white",font=("times new roman",14,"bold"))
d2.place(x=600,y=100)


d3=tk.Button(root,text="Book Appointment",command=Book,width=15,height=2,bd=2,background="black",foreground="white",font=("times new roman",14,"bold"))
d3.place(x=800,y=100)

d3=tk.Button(root,text="BMI Calculator",command=BMI,width=15,height=2,bd=2,background="black",foreground="white",font=("times new roman",14,"bold"))
d3.place(x=1000,y=100)



root.mainloop()
