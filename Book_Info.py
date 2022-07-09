import tkinter as tk
from tkinter import Button,Frame,Label,Entry,ttk,messagebox
import tkinter.font as tkFont
import pymysql
import random


def clear():
    bid.delete(0,'end')
    title.delete(0,'end')
    author.delete(0,'end')
    genre.delete(0,'end')
    status.delete(0,'end')
    for item in listTree.get_children():
        listTree.delete(item)
    
    
    
def viewAll():
        clear()  
    
        try:
            con = pymysql.connect(host="localhost",user="root",password="abc@123",database="library_management")
            cur = con.cursor()
            
            cur.execute("select * from book_info")
            rows = cur.fetchall()
            
            for row in rows:
                listTree.insert("",tk.END,values=row)
            ch = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
            uid=""
            uid="#"
            for i in range(0,4):
                uid = uid + random.choice(ch)
                random.seed(uid)
            bid.insert(0,uid)
            
        except Exception as es:
            messagebox.showerror("Error" , f"Error Dui to : {str(es)}",parent=root)


def search():
        for item in listTree.get_children():
            listTree.delete(item)     
        
        try:
            con = pymysql.connect(host="localhost",user="root",password="abc@123",database="library_management")
            cur = con.cursor()
            cur1=con.cursor()
            
            cur.execute("select * from book_info where title=%s",(title.get()))
            rows1 = cur.fetchall() 
            cur1.execute("select * from book_info where title=%s",(title.get()))
            rows = cur1.fetchone()
            
            for row in rows1:
                listTree.insert("",tk.END,values=row)
            bid.delete(0,'end')
            bid.insert(0,rows[0])
            author.insert(0,rows[2])
            genre.insert(0,rows[3])
            status.insert(0,rows[4])
            
            
                             
                
        except Exception as es:
            messagebox.showerror("Error" , f"Error Dui to : {str(es)}",parent=root)
            
               


def update():
    a = bid.get() 
    b = title.get()    
    c = author.get()
    d = genre.get()
    e = status.get() 
    
    try:
            con = pymysql.connect(host="localhost",user="root",password="abc@123",database="library_management")
            cur = con.cursor()
            cur1 = con.cursor()
               
            cur.execute("update book_info set title=%s,author=%s,genre=%s,status=%s where bid=%s",(b,c,d,e,a) )
           
            if bid.get==None:
                messagebox.showerror("Error" , "Enter Book ID",parent=root)
            else:
                messagebox.showinfo("Success" , "Successfully Updated",parent=root)
                con.commit()
            
            clear()
            
            cur1.execute("select * from book_info where bid=%s",(bid.get()))
            rows = cur1.fetchall()
            
            for row in rows:
                listTree.insert("",tk.END,values=row)
            ch = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
            uid=""
            uid="#"
            for i in range(0,4):
                uid = uid + random.choice(ch)
                random.seed(uid)
            bid.insert(0,uid)
    except Exception as es:
            messagebox.showerror("Error" , f"Error Dui to : {str(es)}",parent=root) 
			
def dele():
    try:
        con = pymysql.connect(host="localhost",user="root",password="abc@123",database="library_management")
        cur = con.cursor()
        cur.execute("delete from book_info where bid= %s",(bid.get()))	
        
        if bid.get()==None:
            messagebox.showerror("Error" , "Enter the data",parent=root)       
        else:	   
            messagebox.showinfo("Success" , "Successfully Deleted",parent=root )
            clear()
            ch = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
            uid=""
            uid="#"
            for i in range(0,4):
                uid = uid + random.choice(ch)
                random.seed(uid)
            bid.insert(0,uid)
            con.commit()
    except Exception as es:
        messagebox.showerror("Error" , f"Error Dui to : {str(es)}",parent=root)  

       
     

def insert():
     a = bid.get() 
     b = title.get()    
     c = author.get()
     d = genre.get()
     e = status.get() 
     
     if a==None:
         messagebox.showerror("Error","Entert bid or title or status!",parent=root)
     #elif e=="avail" or e=="issued":
     else:
         try:
             con = pymysql.connect(host="localhost",user="root",password="abc@123",database="library_management")
             cur = con.cursor()
        
             cur.execute("insert into book_info values(%s,%s,%s,%s,%s)",(a,b,c,d,e))
             data = (a,b,c,d,e)
             
             
             if data==None:
                     messagebox.showerror("Error" , "Enter all data",parent=root)  
             else: 
                 messagebox.showinfo("Success" , "Successfully Inserted",parent=root )
                 con.commit()
             clear()
             
         except Exception as es:
             messagebox.showerror("Error" , f"Error Due to : {str(es)}",parent=root)
    
    
    
        
                 
       
     
     




def on_enter(e):
    e.widget['background'] = 'white'
    e.widget['foreground'] = 'black'

def on_leave(e):
    e.widget['background'] = 'black'   
    e.widget['foreground'] = 'white'


def book():
    global bid,title,author,qty,status,root,genre,listTree,font1
    root = tk.Tk()
    root.title("Book Details")
    root.attributes('-fullscreen', True)
    root.configure(bg='#006B38')
    
    
    font1 = tkFont.Font(family="Helvetica",size=10,weight="bold")
    
    
    
    headingFrame1 = Frame(root, bg="#ffff99", bd=5)
    headingFrame1.place(relx=0.2, rely=0.04, relwidth=0.6, relheight=0.10)

    headingLabel = Label(headingFrame1, text="Book Info", bg='black', fg='white',
                         font=('Courier', 15))
    headingLabel.place(relx=0, rely=0.01, relwidth=1, relheight=1)
    
    lbl_bid = Label(root,text="Book ID",font=font1)
    lbl_bid.place(relx=0.20, rely=0.2, relwidth=0.09, relheight=0.04)
    bid = Entry(root,bd=3.5,font=font1)
    bid.place(relx=0.30, rely=0.2, relwidth=0.39, relheight=0.035)
    ch = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    uid=""
    uid="#"
    for i in range(0,4):
        uid = uid + random.choice(ch)
        #random.seed(uid)
    bid.insert(0,uid)
     
    
    
    lbl_title = Label(root,text="Book Title",font=font1)
    lbl_title.place(relx=0.20, rely=0.25, relwidth=0.09, relheight=0.04)
    title = Entry(root,bd=3.5,font=font1)
    title.place(relx=0.30, rely=0.25, relwidth=0.39, relheight=0.035)
    title.focus()
    
    lbl_author = Label(root,text="Book Author",font=font1)
    lbl_author.place(relx=0.20, rely=0.30, relwidth=0.09, relheight=0.04)
    author = Entry(root,bd=3.5,font=font1) 
    author.place(relx=0.30, rely=0.30, relwidth=0.39, relheight=0.035)
    
    lbl_genre = Label(root,text="Genre",font=font1)
    lbl_genre.place(relx=0.20, rely=0.35, relwidth=0.09, relheight=0.04)
    genre = Entry(root,bd=3.5,font=font1)
    genre.place(relx=0.30, rely=0.35, relwidth=0.39, relheight=0.035)
   
    
    lbl_status = Label(root,text="Status(avail/issued)",font=font1)
    lbl_status.place(relx=0.20, rely=0.40, relwidth=0.09, relheight=0.04)
    status = Entry(root,bd=3.5,font=font1)
    status.place(relx=0.30, rely=0.40, relwidth=0.39, relheight=0.035)
    
    
    listTree = ttk.Treeview(root,height=14,selectmode = "extended")
    listTree["columns"]=("1","2","3","4","5")
    listTree['show'] = 'headings'
    vsb = ttk.Scrollbar(root,orient="vertical",command=listTree.yview)
    hsb = ttk.Scrollbar(root,orient="horizontal",command=listTree.xview)
    listTree.configure(yscrollcommand=vsb.set,xscrollcommand=hsb.set)
    listTree.heading("1", text='Book ID')
    listTree.column("1", width=70,minwidth=70,anchor='center')
    listTree.heading("2", text='Title')
    listTree.column("2", width=230, minwidth=230,anchor='center')
    listTree.heading("3", text='Author')
    listTree.column("3", width=150, minwidth=150,anchor='center')
    listTree.heading("4", text='Genre')
    listTree.column("4", width=100, minwidth=100,anchor='center')
    listTree.heading("5", text='Status')
    listTree.column("5", width=120, minwidth=120,anchor='center')
    listTree.place(relx=0.20, rely=0.50, relwidth=0.48, relheight=0.35)
    vsb.place(relx=0.68,rely=0.501,relheight=0.349)
    hsb.place(relx=0.201,rely=0.830,relwidth=0.49)
    ttk.Style().configure("Treeview",font=('Times new Roman',15))
    
    
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
    
    clr = Button(root, text="CLEAR", bg='black', fg='white',command=clear)
    clr.place(relx=0.72, rely=0.75, relwidth=0.08, relheight=0.06)   
    clr.bind("<Enter>", on_enter)
    clr.bind("<Leave>", on_leave)
    
    
    
    quitBtn = Button(root, text="X",fg="red", bg='#d1ccc0',command=root.destroy)
    quitBtn.place(relx=1.0, y=0, anchor="ne")
    #root.mainloop()
