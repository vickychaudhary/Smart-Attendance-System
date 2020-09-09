from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from playsound import playsound
import os
from datetime import datetime
import append_encodings
import recognize


#creating instance of TK
root=Tk()
root.configure(background="#111")
root.geometry("600x400")


def function1():
    top = Tk()
    top.filename = filedialog.askopenfilename(initialdir = "/home/vicky/Desktop",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    f = top.filename
    top.destroy()
    # print(f)
    fi = f.split("/")
    # print(fi)


    append_encodings.fun1(fi[-1])
    
    
def function2():
    
    top = Tk()
    top.filename = filedialog.askopenfilename(initialdir = "/home/vicky/Desktop",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    f = top.filename
    top.destroy()
    # print(f)
    fi = f.split("/")
    # print(fi)

    recognize.fun2(fi[-1])

def function5():
    pass    
#    os.startfile(os.getcwd()+"/developers/diet1frame1first.html")
    
   
def function6():
    root.destroy()


#stting title for the window
root.title("SMART ATTENDANCE MANAGMENT USING FACE RECOGNITION")

#creating a text label
Label(root, text="     S.A.M.     ",font=("TkIconFont",40),fg="linen",bg="maroon",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=3)

#creating first button
Button(root,text="ADD STUDENT",font=("times new roman",20),bg="#111",fg='orange',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=10)

#creating second button
Button(root,text="RECOGNIZE FACE",font=("times new roman",20),bg="#111",fg='orange',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=10)

#creating third button
Button(root,text="DEVELOPERS",font=('times new roman',20),bg="#111",fg="orange",command=function5).grid(row=8,columnspan=2,sticky=N+E+W+S,padx=5,pady=10)

#creating fourth button
Button(root,text="Exit",font=('times new roman',20),bg="maroon",fg="white",command=function6).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=10)

root.grid_columnconfigure(1,weight=1)

root.mainloop()