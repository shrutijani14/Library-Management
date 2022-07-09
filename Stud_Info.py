import tkinter as tk
from tkinter import Button,Frame,Label,Entry,ttk,messagebox
import tkinter.font as tkFont
import pymysql
import random

def close():
	root.destroy()


def hide_pass1():
    pswd['show']="*"
    show1['command'] = show_pass1
    pswd['font']= font1
def show_pass1():
    pswd['show'] = ""
    show1['command'] = hide_pass1
    pswd['font']= tkFont.Font(family="Helvetica",size=9,weight="bold")
    
    

def clear():
    rno.delete(0,'end')
    name.delete(0,'end')
    class1.delete(0,'end')
    contact.delete(0,'end')
    sid.delete(0,'end')
    pswd.delete(0,'end')
    for item in listTree.get_children():
        listTree.delete(item)
    
def viewAll():
        clear()   
    
        try:
            con = pymysql.connect(host="localhost",user="root",password="abc@123",database="library_management")
            cur = con.cursor()
            
            cur.execute("select * from stud_info")
            rows = cur.fetchall()
            
            for row in rows:
                listTree.insert("",tk.END,values=row)
            
            ch = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
            dig = "0123456789"
            password = ""
            uid=""
    
   
            for i in range(0, 5):
                    password = password + random.choice(ch)
            pswd.insert(0,password)
            for i in range(0,4):
                    uid = uid + random.choice(dig)
            sid.insert(0,uid)
        except Exception as es:
            messagebox.showerror("Error" , f"Error Dui to : {str(es)}",parent=root)


def search():
    flag_validation=True 
    a = rno.get() 
    
    
    try:
       val = int(a)
    except:
       flag_validation=False 
       messagebox.showerror("Error","Invalid RollNo datatype",parent=root)
        
    if (flag_validation):
        clear()
        try:
            con = pymysql.connect(host="localhost",user="root",password="abc@123",database="library_management")
            cur = con.cursor()
            cur1 = con.cursor()
            cur.execute("select * from stud_info where rno=%s",(int(val)))
            rows1 = cur.fetchall()
            cur1.execute("select * from stud_info where rno=%s",(int(val)))
            rows=cur1.fetchone()
            #listTree.insert(0,[RNo,Name,Class,Contact,Sid,Pswd])    
        
            
            for row in rows1:
              listTree.insert("",tk.END,values=row)
            rno.insert(0,rows[0])
            name.insert(0,rows[1])
            class1.insert(0,rows[2])
            contact.insert(0,rows[3])
            sid.insert(0,rows[4])
            pswd.insert(0,rows[5])
            
                
        except Exception as es:
            messagebox.showerror("Error" , f"Error Dui to : {str(es)}",parent=root)
            
            
    
    


def update():    
    flag_validation=True 
    a = rno.get() 
    b = name.get()    
    c = class1.get()
    d = contact.get()
    e = sid.get() 
    f = pswd.get()
    try:
       val = int(a)
    except:
       flag_validation=False 
       messagebox.showerror("Error","Invalid RollNo datatype",parent=root)
        
    if (flag_validation):
        try:
            con = pymysql.connect(host="localhost",user="root",password="abc@123",database="library_management")
            cur = con.cursor()        
            cur1 = con.cursor() 
               
            cur.execute("update stud_info set name=%s,class=%s,contact=%s,id=%s,password=%s where rno=%s",(b,c,d,e,f,int(val)) )
            cur1.execute("update login_info set id=%s,password=%s where r_no=%s",(e,f,int(val)))
            if rno.get==None:
                messagebox.showerror("Error" , "Enter Book ID",parent=root)
            else:
                messagebox.showinfo("Success" , "Successfully Updated",parent=root )
                clear()
                ch = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
                dig = "0123456789"
                password = ""
                uid=""
    
   
                for i in range(0, 5):
                    password = password + random.choice(ch)
                pswd.insert(0,password)
                for i in range(0,4):
                    uid = uid + random.choice(dig)
                sid.insert(0,uid)
                con.commit()
        except Exception as es:
            messagebox.showerror("Error" , f"Error Dui to : {str(es)}",parent=root) 




def dele():
    flag_validation=True 
    a = rno.get() 
    
    try:
        val = int(a)
    except:
        flag_validation=False 
        messagebox.showerror("Error","Invalid RollNo datatype",parent=root)
	
    if(flag_validation):
        try:
            con=pymysql.connect(host="localhost",user="root",password="abc@123",database="library_management")
            cur=con.cursor()
            cur1=con.cursor()
            cur2=con.cursor()
            #cur3=con.cursor()
            #cur2.execute("Select sid from issue_book")
            #rows = cur2.fetchall()
            #if rows==sid.get:
             #   cur3.execute("delete from issue_book where sid=%s",(sid.get()))
            cur2.execute("delete from issue_book where sid=%s",(sid.get()))
            cur.execute("delete from login_info where r_no=%s",(int(val)))	
            cur1.execute("delete from stud_info where rno=%s",(int(val)))
            if rno.get()==None:
                messagebox.showerror("Error" , "Enter the data",parent=root)
            else:
                messagebox.showinfo("Success" , "Successfully Deleted",parent=root )
                clear()
                ch = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
                dig = "0123456789"
                password = ""
                uid=""
    
   
                for i in range(0, 5):
                    password = password + random.choice(ch)
                pswd.insert(0,password)
                for i in range(0,4):
                    uid = uid + random.choice(dig)
                sid.insert(0,uid)
                con.commit()
        except Exception as es:
            messagebox.showerror("Error" , f"Error Dui to : {str(es)}",parent=root) 		           
		
	

    
def insert():
     flag_validation=True 
     a = rno.get() 
     b = name.get()    
     c = class1.get()
     d = contact.get()
     e = sid.get() 
     f = pswd.get()
     issued='NO'
     try:
        val = int(a)
     except:
        flag_validation=False 
        messagebox.showerror("Error","Invalid RollNo datatype",parent=root)
     
     if(flag_validation):
         try:
             con = pymysql.connect(host="localhost",user="root",password="abc@123",database="library_management")
             cur = con.cursor()
             cur1 = con.cursor()
        
        
        
             cur.execute("insert into stud_info values(%s,%s,%s,%s,%s,%s,%s)",(int(val),b,c,d,e,f,issued))
             #cur1.execute("Insert into login values(%s,%s)",(e,f))
             cur1.execute("Insert into login_info values(%s,%s,%s)",(int(val),e,f))
             data = (int(val),b,c,d,e,f)
             
             
             if data==None:
                 messagebox.showerror("Error" , "Enter all data",parent=root)  
             else: 
                 messagebox.showinfo("Success" , "Successfully Inserted",parent=root )
                 con.commit()
                 
         except Exception as es:
             messagebox.showerror("Error" , f"Error Due to : {str(es)}",parent=root)


def on_enter(e):
    e.widget['background'] = 'white'
    e.widget['foreground'] = 'black'

def on_leave(e):
    e.widget['background'] = 'black'   
    e.widget['foreground'] = 'white'


def stud():
    global rno,name,class1,contact,sid,pswd,root,con,cur,listTree,show1,font1
    root = tk.Tk()
    root.title("Student Details")
    root.attributes('-fullscreen', True)
    root.configure(bg='#006B38')
    
    
    font1 = tkFont.Font(family="Helvetica",size=10,weight="bold")
    
    
    
    headingFrame1 = Frame(root, bg="#ffff99", bd=5)
    headingFrame1.place(relx=0.2, rely=0.04, relwidth=0.6, relheight=0.10)

    headingLabel = Label(headingFrame1, text="Student Info", bg='black', fg='white',
                         font=('Courier', 15))
    headingLabel.place(relx=0, rely=0.01, relwidth=1, relheight=1)
    
    lbl_rno = Label(root,text="Roll No",font=font1)
    lbl_rno.place(relx=0.20, rely=0.2, relwidth=0.09, relheight=0.04)
    rno = Entry(root,bd=3.5,font=font1)
    rno.place(relx=0.30, rely=0.2, relwidth=0.39, relheight=0.035)
    rno.focus()  
    
    lbl_name = Label(root,text="Name",font=font1)
    lbl_name.place(relx=0.20, rely=0.25, relwidth=0.09, relheight=0.04)
    name = Entry(root,bd=3.5,font=font1)
    name.place(relx=0.30, rely=0.25, relwidth=0.39, relheight=0.035)
    
    lbl_class = Label(root,text="Class",font=font1)
    lbl_class.place(relx=0.20, rely=0.30, relwidth=0.09, relheight=0.04)
    class1 = Entry(root,bd=3.5,font=font1) 
    class1.place(relx=0.30, rely=0.30, relwidth=0.39, relheight=0.035)
    
    lbl_contact= Label(root,text="Contact",font=font1)
    lbl_contact.place(relx=0.20, rely=0.35, relwidth=0.09, relheight=0.04)
    contact = Entry(root,bd=3.5,font=font1)
    contact.place(relx=0.30, rely=0.35, relwidth=0.39, relheight=0.035)
    
    lbl_sid = Label(root,text="Student_ID",font=font1)
    lbl_sid.place(relx=0.20, rely=0.40, relwidth=0.09, relheight=0.04)
    sid = Entry(root,bd=3.5,font=font1)
    sid.place(relx=0.30, rely=0.40, relwidth=0.39, relheight=0.035)
    
    lbl_pass = Label(root,text="Password",font=font1)
    lbl_pass.place(relx=0.20, rely=0.45, relwidth=0.09, relheight=0.04)
    pswd = Entry(root,bd=3.5,font=(False,20),show='*')
    pswd.place(relx=0.30, rely=0.45, relwidth=0.39, relheight=0.035)  
    
    
    
    
    listTree = ttk.Treeview(root,height=14,selectmode = "extended")
    listTree["columns"]=("1","2","3","4","5","6")
    listTree['show'] = 'headings'
    vsb = ttk.Scrollbar(root,orient="vertical",command=listTree.yview)
    hsb = ttk.Scrollbar(root,orient="horizontal",command=listTree.xview)
    listTree.configure(yscrollcommand=vsb.set,xscrollcommand=hsb.set)
    listTree.heading("1", text='Roll No')
    listTree.column("1", width=50,minwidth=50,anchor='center')
    listTree.heading("2", text='Name')
    listTree.column("2", width=250, minwidth=250,anchor='center')
    listTree.heading("3", text='Class')
    listTree.column("3", width=60, minwidth=60,anchor='center')
    listTree.heading("4", text='Contact')
    listTree.column("4", width=110, minwidth=110,anchor='center')
    listTree.heading("5", text='ID')
    listTree.column("5", width=70, minwidth=70,anchor='center')
    listTree.heading("6", text='Password')
    listTree.column("6", width=125, minwidth=125,anchor='center')
    listTree.place(relx=0.20, rely=0.50, relwidth=0.48, relheight=0.35)
    vsb.place(relx=0.68,rely=0.501,relheight=0.349)
    hsb.place(relx=0.201,rely=0.830,relwidth=0.49)
    ttk.Style().configure("Treeview",font=('Times new Roman',15))
    
    
    
    
    
    ch = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    dig = "0123456789"
    password = ""
    uid=""
    
   
    for i in range(0, 5):
        password = password + random.choice(ch)
    pswd.insert(0,password)
    for i in range(0,4):
        uid = uid + random.choice(dig)
    sid.insert(0,uid)
   
    
    
    search1 = Button(root, text="SEARCH", bg='black', fg='white',command=search)
    search1.place(relx=0.72, rely=0.2, relwidth=0.08, relheight=0.06)
    search1.bind("<Enter>", on_enter)
    search1.bind("<Leave>", on_leave)
    
    
    add = Button(root, text="ADD", bg='black', fg='white',command=insert)
    add.place(relx=0.72, rely=0.31, relwidth=0.08, relheight=0.06)
    add.bind("<Enter>", on_enter)
    add.bind("<Leave>", on_leave)
    
    delete = Button(root, text="DELETE", bg='black', fg='white',command=dele)
    delete.place(relx=0.72, rely=0.42, relwidth=0.08, relheight=0.06)
    delete.bind("<Enter>", on_enter)
    delete.bind("<Leave>", on_leave)
    
    update1 = Button(root, text="UPDATE", bg='black', fg='white',command=update)
    update1.place(relx=0.72, rely=0.53, relwidth=0.08, relheight=0.06)
    update1.bind("<Enter>", on_enter)
    update1.bind("<Leave>", on_leave)
    
    view = Button(root, text="VIEW ALL", bg='black', fg='white',command=viewAll)
    view.place(relx=0.72, rely=0.64, relwidth=0.08, relheight=0.06)
    view.bind("<Enter>", on_enter)
    view.bind("<Leave>", on_leave)    
    
    show1 = Button(root,text = "show", bg="black",fg="white",command=show_pass1)
    show1.place(relx=0.662,rely=0.45,relheight=0.035)
    show1.bind("<Enter>", on_enter)
    show1.bind("<Leave>", on_leave)
    
    clr = Button(root, text="CLEAR", bg='black', fg='white',command=clear)
    clr.place(relx=0.72, rely=0.75, relwidth=0.08, relheight=0.06)   
    clr.bind("<Enter>", on_enter)
    clr.bind("<Leave>", on_leave)
    
    
    
    
    
    quitBtn = Button(root, text="X",fg="red", bg='#d1ccc0',command=root.destroy)
    quitBtn.place(relx=1.0, y=0, anchor="ne")
    #root.mainloop()
    
    
#stud()




   