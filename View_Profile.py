import tkinter as tk
from tkinter import Button,Frame,Label,Entry,messagebox
import tkinter.font as tkFont
import pymysql
from pswd_change import change_pass
from id_change import change_id


def close():
	root.destroy()


def hide_pass():
    pswd['show']="*"
def show_pass():
    pswd ['show'] = ""
    pswd['command'] = hide_pass
    
    
           
        

def clear():
    rno['state']='normal'
    name['state']='normal'
    class1['state']='normal'
    contact['state']='normal'
    sid['state']='normal'
    rno.delete(0,'end')
    name.delete(0,'end')
    class1.delete(0,'end')
    contact.delete(0,'end')
    sid.delete(0,'end')
    pswd.delete(0,'end')
    


def edit():
    rno['state']='readonly'
    name['state']='readonly'
    class1['state']='readonly'
    contact['state']='readonly'
    sid['state']='readonly'
    
        
   
    
def view_info():
        global a1,a2  
        try:
            con = pymysql.connect(host="localhost",user="root",password="abc@123",database="library_management")
            cur = con.cursor()
            
            cur.execute("select * from stud_info where rno = %s",rno.get())
            rows = cur.fetchone()
            #rno.insert(0,rows[0])
            name.insert(0,rows[1])
            class1.insert(0,rows[2])
            contact.insert(0,rows[3])     
            sid.insert(0,rows[4])
            
            a1 = sid.get()
            a2 = rno.get()
            
            edit()
            #pswd.insert(0,rows[5])
            #if(rows):
                
            #else:
             #   messagebox.showerror("Error","Wrong input!!")
           
        except Exception as es:
            messagebox.showerror("Error" , f"Error Dui to : {str(es)}",parent=root)



            



def on_enter(e):
    e.widget['background'] = 'white'
    e.widget['foreground'] = 'black'

def on_leave(e):
    e.widget['background'] = 'black'   
    e.widget['foreground'] = 'white'


def stud_info():
    global rno,name,class1,contact,sid,pswd,root,con,cur
    root = tk.Tk()
    root.title("Student Details")
    root.attributes('-fullscreen', True)
    root.configure(bg='#006B38')
    
    
    font1 = tkFont.Font(family="Helvetica",size=10,weight="bold")
    
    
    
    headingFrame1 = Frame(root, bg="#ffff99", bd=5)
    headingFrame1.place(relx=0.2, rely=0.04, relwidth=0.6, relheight=0.10)

    headingLabel = Label(headingFrame1, text="Personal Info", bg='black', fg='white',
                         font=('Courier', 15))
    headingLabel.place(relx=0, rely=0.01, relwidth=1, relheight=1)
    
    lbl_rno = Label(root,text="Roll No",font=font1)
    lbl_rno.place(relx=0.25, rely=0.2, relwidth=0.09, relheight=0.04)
    rno = Entry(root,bd=3.5,font=font1)
    rno.place(relx=0.38, rely=0.2, relwidth=0.39, relheight=0.035)
    rno.focus()  
    
    lbl_name = Label(root,text="Name",font=font1)
    lbl_name.place(relx=0.25, rely=0.3, relwidth=0.09, relheight=0.04)
    name = Entry(root,bd=3.5,font=font1)
    name.place(relx=0.38, rely=0.3, relwidth=0.39, relheight=0.035)
    
    lbl_class = Label(root,text="Class",font=font1)
    lbl_class.place(relx=0.25, rely=0.4, relwidth=0.09, relheight=0.04)
    class1 = Entry(root,bd=3.5,font=font1) 
    class1.place(relx=0.38, rely=0.4, relwidth=0.39, relheight=0.035)
    
    lbl_contact= Label(root,text="Contact",font=font1)
    lbl_contact.place(relx=0.25, rely=0.5, relwidth=0.09, relheight=0.04)
    contact = Entry(root,bd=3.5,font=font1)
    contact.place(relx=0.38, rely=0.5, relwidth=0.39, relheight=0.035)
    
    lbl_sid = Label(root,text="User_ID",font=font1)
    lbl_sid.place(relx=0.25, rely=0.6, relwidth=0.09, relheight=0.04)
    sid = Entry(root,bd=3.5,font=font1,show='*')
    sid.place(relx=0.38, rely=0.6, relwidth=0.39, relheight=0.035)
    
    
    #lbl_pass = Label(root,text="Password",font=font1)
    #lbl_pass.place(relx=0.25, rely=0.7, relwidth=0.09, relheight=0.04)
    #pswd = Entry(root,bd=3.5,font=(False,20),show='*')
    #pswd.place(relx=0.38, rely=0.7, relwidth=0.39, relheight=0.035)  
    
    
    #show = Button(root,text = "show", bg="black",fg="white",command=show_pass)
    #show.place(relx=0.75,rely=0.7)
    #show.bind("<Enter>", on_enter)
    #show.bind("<Leave>", on_leave)
    
    view = Button(root, text="View Profile", bg='black', fg='white',command=view_info)
    view.place(relx=0.30, rely=0.75, relwidth=0.08, relheight=0.06)
    view.bind("<Enter>", on_enter)
    view.bind("<Leave>", on_leave)
    
    pswd = Button(root,text="Change Password",bg = 'black',fg='white',command=change_pass)
    pswd.place(relx=0.41, rely=0.75, relwidth=0.08, relheight=0.06)
    pswd.bind("<Enter>", on_enter)
    pswd.bind("<Leave>", on_leave)
    
    id1 = Button(root,text="Change UserID",bg = 'black',fg='white',command=change_id)
    id1.place(relx=0.52, rely=0.75, relwidth=0.08, relheight=0.06)
    id1.bind("<Enter>", on_enter)
    id1.bind("<Leave>", on_leave)
    
    
    
    
    clr = Button(root, text="CLEAR", bg='black', fg='white',command=clear)
    clr.place(relx=0.63, rely=0.75, relwidth=0.08, relheight=0.06)   
    clr.bind("<Enter>", on_enter)
    clr.bind("<Leave>", on_leave)
      
    
    
    
    quitBtn = Button(root, text="X",fg="red", bg='#d1ccc0',command=root.destroy)
    quitBtn.place(relx=1.0, y=0, anchor="ne")
    root.mainloop()
    





   