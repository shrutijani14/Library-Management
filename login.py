import tkinter as tk
from tkinter import Label,Button,Entry,Frame,messagebox
from home_stud import main1
from home_admin import main
import pymysql


root = tk.Tk()
root.title("Library Management System")
root.attributes('-fullscreen', True)
root.configure(bg='#006B38')

def clear():
    user_name.delete(0,'end')
    password.delete(0,'end')
    user_name.focus()

def close():
	root.destroy()	
    
def on_enter(e):
    e.widget['background'] = 'white'
    e.widget['foreground'] = 'black'

def on_leave(e):
    e.widget['background'] = 'black'   
    e.widget['foreground'] = 'white'
    

def hide_pass1():
    password['show']="*"
    show1['command'] = show_pass1
def show_pass1():
    password['show'] = ""
    show1['command'] = hide_pass1

def login():
    global uid,pswd1
    
    
    if user_name.get()=="" or password.get()=="":
        messagebox.showerror("Error","Enter User Name And Password")
    elif user_name.get()=="admin" and password.get()=="admin":
        messagebox.showinfo("Success" , "Successfully Login" )
        main() 
        clear()
    else:
        try:
            con = pymysql.connect(host="localhost",user="root",password="abc@123",database="library_management")
            cur = con.cursor()
            uid = user_name.get()
            pswd1 = password.get()
            cur.execute("select * from login_info where id=%s and password = %s",(user_name.get(),password.get()))
            data = cur.fetchone()
            
            if data==None:
                messagebox.showerror("Error" , "Invalid User Name or Password") 
                clear()
            else:
                messagebox.showinfo("Success" , "Successfully Login" )
                main1()
                clear()
        except Exception as es:
            messagebox.showerror("Error" , f"Error Dui to : {str(es)}")
				        



headingFrame1 = Frame(root, bg="#ffff99", bd=5)
headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

headingLabel = Label(headingFrame1, text="Login", bg='black', fg='white', font=('Courier', 15,'bold'))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)


labelFrame = Frame(root, bg='black')
labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.4)

uid = Label(labelFrame, text="User ID : ", bg='black', fg='white',font=('Courier', 15))
uid.place(relx=0.05, rely=0.2, relheight=0.08)

user_name = Entry(labelFrame,text="",font=('Courier', 15))
user_name.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)
user_name.focus()


passw = Label(labelFrame,text="Password: ", bg='black', fg='white',font=('Courier', 15))
passw.place(relx=0.05, rely=0.4, relheight=0.08)

password = Entry(labelFrame,text="",show='*',font=('Courier', 15))
password.place(relx=0.3, rely=0.4, relwidth=0.62, relheight=0.08)

show1 = Button(root,text = "show", bg="black",fg="white",command=show_pass1)
show1.place(relx=0.835,rely=0.46,relheight=0.035)
show1.bind("<Enter>", on_enter)
show1.bind("<Leave>", on_leave)


SubmitBtn = Button(labelFrame, text="SUBMIT", bg='#d1ccc0', fg='black',command=login)
SubmitBtn.place(relx=0.28, rely=0.6, relwidth=0.18, relheight=0.18)

clrBtn = Button(labelFrame, text="CLEAR", bg='#d1ccc0', fg='black',command=clear)
clrBtn.place(relx=0.55, rely=0.6, relwidth=0.18, relheight=0.18)

quitBtn = Button(root, text="X",fg="red", bg='#d1ccc0',command=root.destroy)
quitBtn.place(relx=1.0, y=0, anchor="ne")

root.mainloop()
