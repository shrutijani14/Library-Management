import tkinter as tk
from tkinter import Button,Frame,Label,Entry,messagebox
import tkinter.font as tkFont
import pymysql


def close():
	root.destroy()
    
def userID():
    flag_validation=True 
    a = rno.get() 
    
    
    try:
            val = int(a)
    except:
            flag_validation=False 
            messagebox.showerror("Error","Invalid RollNo datatype or field is empty!!",parent=root)
    if (flag_validation):
                try:                  
                    if(new.get()==old.get()):
                        messagebox.showinfo("UserID","New password entered is same old one!!",parent=root)
                    else:
                        if(new.get()==renter.get()):
                            try:
                               con = pymysql.connect(host="localhost",user="root",password="abc@123",database="library_management")
                               cur = con.cursor()
                               cur1 = con.cursor()
                               cur2 = con.cursor()
                               cur3 = con.cursor()
                               cur2.execute('SET foreign_key_checks = 0')
                               cur1.execute("update stud_info INNER JOIN issue_book on stud_info.id = issue_book.sid set issue_book.sid = %s where stud_info.id= %s",(new.get(),old.get()))
                               cur.execute("update stud_info INNER JOIN login_info on stud_info.rno=login_info.r_no set login_info.id=%s,stud_info.id=%s where stud_info.rno=%s",(new.get(),new.get(),int(val)))
                               cur3.execute('SET foreign_key_checks = 1')
                               messagebox.showinfo("Success" , "UserID Changed Successfully!!",parent=root )
                               con.commit()
                            except Exception as es:
                                messagebox.showerror("Error" , f"Error Dui to : {str(es)}",parent=root) 
                        else:
                            messagebox.showerror("Error","you re-entered the wrong id!!",parent=root)
                except Exception as es:
                    messagebox.showerror("Error" , f"Error Dui to : {str(es)}",parent=root)


        

        
    
def clear():
    old.delete(0,'end')
    new.delete(0,'end')
    renter.delete(0,'end')
    rno.delete(0,'end')

def on_enter(e):
    e.widget['background'] = 'white'
    e.widget['foreground'] = 'black'

def on_leave(e):
    e.widget['background'] = 'black'   
    e.widget['foreground'] = 'white'

def change_id():
    global root,old,new,renter,rno
    root = tk.Tk()
    root.title("User_ID")
    #root.minsize(width=400, height=400)
    #root.geometry("600x500")
    root.resizable(False, False)  # This code helps to disable windows from resizing

    window_height = 350
    window_width = 350  

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    root.configure(bg='#006B38')
       
    
    font1 = tkFont.Font(family="Helvetica",size=9,weight="bold") 
    
    
    
    headingFrame1 = Frame(root, bg="#ffff99", bd=5)
    headingFrame1.place(relx=0.1, rely=0.04, relwidth=0.8, relheight=0.10)
    headingLabel = Label(headingFrame1, text="Change User_ID", bg='black', fg='white',
                         font=('Courier', 15 , 'bold'))
    headingLabel.place(relx=0, rely=0.01, relwidth=1, relheight=1)
    
    lbl_rno = Label(root,text="Roll_No",font=font1)
    lbl_rno.place(relx=0.15, rely=0.20, relwidth=0.25, relheight=0.06)
    rno = Entry(root,bd=3.5,font=font1,fg='red')
    rno.place(relx=0.43, rely=0.20, relwidth=0.39, relheight=0.06)
    rno.focus()
    #sid.insert(0,a1)
    
    lbl_old_id = Label(root,text="Old User_ID",font=font1)
    lbl_old_id.place(relx=0.15, rely=0.30, relwidth=0.25, relheight=0.06)
    old = Entry(root,bd=3.5,font=font1)
    old.place(relx=0.43, rely=0.30, relwidth=0.39, relheight=0.06)
    
    
    lbl_new_id = Label(root,text="New User_ID",font=font1)
    lbl_new_id.place(relx=0.15, rely=0.40, relwidth=0.25, relheight=0.06)
    new = Entry(root,bd=3.5,font = font1)
    new.place(relx=0.43, rely=0.40, relwidth=0.39, relheight=0.06)
    
    lbl_id = Label(root,text="Renter",font=font1)
    lbl_id.place(relx=0.15, rely=0.50, relwidth=0.25, relheight=0.06)
    renter = Entry(root,bd=3.5,font=font1)
    renter.place(relx=0.43, rely=0.50, relwidth=0.39, relheight=0.06)
    
    change = Button(root, text="Change", bg='black', fg='white',font=font1,command=userID)
    change.place(relx=0.23, rely=0.70, relwidth=0.20, relheight=0.06)   
    change.bind("<Enter>", on_enter)
    change.bind("<Leave>", on_leave)
   
    
    
    
    clr = Button(root, text="Clear", bg='black', fg='white',command=clear,font=font1)
    clr.place(relx=0.58, rely=0.70, relwidth=0.20, relheight=0.06)   
    clr.bind("<Enter>", on_enter)
    clr.bind("<Leave>", on_leave)
    
    root.mainloop()


    