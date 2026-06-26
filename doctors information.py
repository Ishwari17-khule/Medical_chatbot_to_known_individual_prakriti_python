import tkinter as tk
from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re


##############################################+=============================================================
root = tk.Tk()
root.configure(background="black")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.title("Form")



        

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('book appointment.jpg')
image2 = image2.resize((w,h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)

label_l2 = tk.Label(root,text="Doctor Information",font=("Times New Roman",20, 'bold','italic'),width=98,
                    background="pink", fg="black")
label_l2.place(x=0, y=0)
    
# import sqlite3
# my_conn = sqlite3.connect('Doctors.db')
# r_set=my_conn.execute("SELECT * from List")
# i=0 # row value inside the loop 
# for student in r_set: 
#     for j in range(len(student)):
#         e = tk.Entry(root, width=10, fg='blue') 
#         e.grid(row=i, column=j) 
#         e.insert(END, student[j])
#     i=i+1
def submit():
    # l2 = tk.Label(root, text="Appoinment sucessful", width=12, font=("Times new roman", 15, "bold"),bd=5, fg="black")
    # l2.place(x=100, y=100)
    ms.showinfo('Success!', 'Appointment Successfully !')
    
from tkinter import ttk
#1st Disease
l2 = tk.Label(root, text="Fever :", width=12, font=("Times new roman", 15, "bold"),bd=5, bg="black", fg="white")
l2.place(x=30, y=100)
    
monthchoosen = ttk.Combobox(root, width = 35)

    # Adding combobox drop down list
monthchoosen['values'] = ('1. Dr. Khurana,	(9090909090),Akurdi,Pune',
'2. Dr. Patil, (9898989898),Chinchwad,Pune',
'3. Dr. Shinde,(8989898989),Akurdi,Pune',
'4. Dr. Rustam,(9999999999),Chinchwad,Pune',
'5. Dr. Sharma,(8080808080),Pimpri,Pune')
monthchoosen.place(x=250,y=100)
    #monthchoosen.grid(column = 1, row = 1)
monthchoosen.current()


#2nd disease
l2 = tk.Label(root, text="COUGH :", width=12, font=("Times new roman", 15, "bold"),bd=5, bg="black", fg="white")
l2.place(x=30, y=200)
    
monthchoosen = ttk.Combobox(root, width = 35)

    # Adding combobox drop down list
monthchoosen['values'] = ('1. Dr. Jadhav,(7070707070),Chinachwad,Pune',
'2.Dr. Pawar,(7878787878),Akurdi,Pune',
'3.Dr. Tikone,(9191919191),	Akurdi,Pune',
'4.Dr. Saxena,(9292929292),	Ravet,Pune',
'5.Dr. Raheja	(8787878787) Pimpri,Pune')
monthchoosen.place(x=250,y=200)
    #monthchoosen.grid(column = 1, row = 1)
monthchoosen.current()

#3rd disease
l2 = tk.Label(root, text="COLD :", width=12, font=("Times new roman", 15, "bold"),bd=5, bg="black", fg="white")
l2.place(x=30, y=300)
    
monthchoosen = ttk.Combobox(root, width = 35)

    # Adding combobox drop down list
monthchoosen['values'] = ('1. Dr. Ahuja	(8181818181)Pimpri,Pune',
'2.	Dr. Mandrekar	(8686868686)	Chinchwad,Pune',
'3.Dr. Upadhyay	(9393939393)	Ravet,Pune',
'4.Dr. Budhwani	(9494949494)	Akurdi,Pune',
'5.Dr. Survase	(9797979797)	Chikhli,Pune')
monthchoosen.place(x=250,y=300)
    #monthchoosen.grid(column = 1, row = 1)
monthchoosen.current()

#4TH DISEASE
l2 = tk.Label(root, text="CHICKEN POX :", width=12, font=("Times new roman", 15, "bold"),bd=5, bg="black", fg="white")
l2.place(x=30, y=400)
    
monthchoosen = ttk.Combobox(root, width = 35)

    # Adding combobox drop down list
monthchoosen['values'] = ('1.Dr. Wadia	(8181818181)Chinchwad,Pune',
'2.Dr. Sahara	(8282828282)Akurdi,Pune',
'3.Dr. Gupta	(8383838383)	Walhekarwadi,Pune',
'4.Dr. Shah	(8585858585)	Pimpri,Pune',
'5.Dr. Khamkar	(7272727272)	Akurdi,Pune')
monthchoosen.place(x=250,y=400)
    #monthchoosen.grid(column = 1, row = 1)
monthchoosen.current()

#5TH diSEASE

l2 = tk.Label(root, text="Contact Dermatitis :", width=12, font=("Times new roman", 15, "bold"),bd=5, bg="black", fg="white")
l2.place(x=30, y=500)
    
monthchoosen = ttk.Combobox(root, width = 35)

    # Adding combobox drop down list
monthchoosen['values'] = ('1.Dr. Shrinivas	(9293949596)Pimpri, Pune',
'2.Dr. Kashyap	9897969594	Swargate, Pune')
monthchoosen.place(x=250,y=500)
    #monthchoosen.grid(column = 1, row = 1)
monthchoosen.current()


#6TH disease
l2 = tk.Label(root, text="Eye Allergies :", width=12, font=("Times new roman", 15, "bold"),bd=5, bg="black", fg="white")
l2.place(x=30, y=600)
    
monthchoosen = ttk.Combobox(root, width = 35)

    # Adding combobox drop down list
monthchoosen['values'] = ('1.Dr. R. R. Madhavan	(8089789765)	Pimpri , Pune',
'2.Dr. Shaila Ahuluia	(9089675634)	Ravet , Pune')
monthchoosen.place(x=250,y=600)
    #monthchoosen.grid(column = 1, row = 1)
monthchoosen.current()


#7TH disease

l2 = tk.Label(root, text="Sinus Infection :", width=12, font=("Times new roman", 15, "bold"),bd=5, bg="black", fg="white")
l2.place(x=750, y=100)
    
monthchoosen = ttk.Combobox(root, width = 35)

    # Adding combobox drop down list
monthchoosen['values'] = ('1Dr. Vasikaran	(8078651273)Karve Road , Pune',
'2.Dr. Ashish Chawla	(7835298462)	Paud Road , Pune')
monthchoosen.place(x=950,y=100)
    #monthchoosen.grid(column = 1, row = 1)
monthchoosen.current()

#8th disease

l2 = tk.Label(root, text="Allergic Rhinitis :", width=12, font=("Times new roman", 15, "bold"),bd=5, bg="black", fg="white")
l2.place(x=750, y=200)
    
monthchoosen = ttk.Combobox(root, width = 35)

    # Adding combobox drop down list
monthchoosen['values'] = ('1.Dr. Shashidharan	(9025648284)Baner , Pune',
'2.Dr. Balkrishna	7815263750	Bavdhan , Pune')
monthchoosen.place(x=950,y=200)
    #monthchoosen.grid(column = 1, row = 1)
monthchoosen.current()

#9th disease

l2 = tk.Label(root, text="Food Allergy :", width=12, font=("Times new roman", 15, "bold"),bd=5, bg="black", fg="white")
l2.place(x=750, y=300)
    
monthchoosen = ttk.Combobox(root, width = 35)

    # Adding combobox drop down list
monthchoosen['values'] = ('1.Dr. Priya Sharma	(9989836271)Kothrud , Pune',
'2.Dr. Riya Agnihotri	(8976564323)	Koregaon Park , Pune')
monthchoosen.place(x=950,y=300)
    #monthchoosen.grid(column = 1, row = 1)
monthchoosen.current()

#10th disease

l2 = tk.Label(root, text="Anaphylaxis :", width=12, font=("Times new roman", 15, "bold"),bd=5, bg="black", fg="white")
l2.place(x=750, y=400)
    
monthchoosen = ttk.Combobox(root, width = 35)

    # Adding combobox drop down list
monthchoosen['values'] = ('1.Dr. Nutan Bose	8927374829	Kalyaninagar , Pune',
'2.Dr. Arun Saxena	9090876543	Nigdi , Pune')
monthchoosen.place(x=950,y=400)
    #monthchoosen.grid(column = 1, row = 1)
monthchoosen.current()



#11th disease
l2 = tk.Label(root, text="Anaphylaxis :", width=12, font=("Times new roman", 15, "bold"),bd=5, bg="black", fg="white")
l2.place(x=750, y=500)
    
monthchoosen = ttk.Combobox(root, width = 35)

    # Adding combobox drop down list
monthchoosen['values'] = ('1.Dr. Pawar	(9898787887)	Pune',
'2.Dr. Sharma	(9898798767)	Nigdi , Pune')
monthchoosen.place(x=950,y=500)
    #monthchoosen.grid(column = 1, row = 1)
monthchoosen.current()

  #12th disease
l2 = tk.Label(root, text="Eczema :", width=12, font=("Times new roman", 15, "bold"),bd=5,bg="black", fg="white")
l2.place(x=750, y=600)
    
monthchoosen = ttk.Combobox(root, width = 35)

    # Adding combobox drop down list
monthchoosen['values'] = ('1.Dr.Patil	(9098765449)	Katraj,Pune',
'2.Dr.Pande	9876543338	Vadgav,Pune')
monthchoosen.place(x=950,y=600)
    #monthchoosen.grid(column = 1, row = 1)
monthchoosen.current()






































button1 = tk.Button(root, text="Appointment", command=submit, width=12, height=1,font=('times 15 bold italic '),bd=5, bg="blue", fg="white")
button1.place(x=500, y=100)

button1 = tk.Button(root, text="Appointment", command=submit, width=12, height=1,font=('times 15 bold italic '),bd=5, bg="blue", fg="white")
button1.place(x=500, y=200)

button1 = tk.Button(root, text="Appointment", command=submit, width=12, height=1,font=('times 15 bold italic '),bd=5, bg="blue", fg="white")
button1.place(x=500, y=300)

button1 = tk.Button(root, text="Appointment", command=submit, width=12, height=1,font=('times 15 bold italic '),bd=5, bg="blue", fg="white")
button1.place(x=500, y=400)


button1 = tk.Button(root, text="Appointment", command=submit, width=12, height=1,font=('times 15 bold italic '),bd=5, bg="blue", fg="white")
button1.place(x=500, y=500)

button1 = tk.Button(root, text="Appointment", command=submit, width=12, height=1,font=('times 15 bold italic '),bd=5, bg="blue", fg="white")
button1.place(x=500, y=600)

button1 = tk.Button(root, text="Appointment", command=submit, width=12, height=1,font=('times 15 bold italic '),bd=5, bg="blue", fg="white")
button1.place(x=1200, y=100)

button1 = tk.Button(root, text="Appointment", command=submit, width=12, height=1,font=('times 15 bold italic '),bd=5, bg="blue", fg="white")
button1.place(x=1200, y=200)

button1 = tk.Button(root, text="Appointment", command=submit, width=12, height=1,font=('times 15 bold italic '),bd=5, bg="blue", fg="white")
button1.place(x=1200, y=300)

button1 = tk.Button(root, text="Appointment", command=submit, width=12, height=1,font=('times 15 bold italic '),bd=5, bg="blue", fg="white")
button1.place(x=1200, y=400)


button1 = tk.Button(root, text="Appointment", command=submit, width=12, height=1,font=('times 15 bold italic '),bd=5, bg="blue", fg="white")
button1.place(x=1200, y=500)

button1 = tk.Button(root, text="Appointment", command=submit, width=12, height=1,font=('times 15 bold italic '),bd=5, bg="blue", fg="white")
button1.place(x=1200, y=600)







root.mainloop()