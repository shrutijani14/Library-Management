import tkinter as tk
from tkinter import Button,Frame,Label,Entry,messagebox,ttk
import tkinter.font as tkFont
import pymysql


def clear():
    
    title.delete(0,'end')    
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
                if row[4]=='avail':
                    listTree.insert("",tk.END,values=row) 
            
           
                
            
               
            
            
            
        except Exception as es:
            messagebox.showerror("Error" , f"Error Dui to : {str(es)}",parent=root)

def search_book():
        for item in listTree.get_children():
            listTree.delete(item)     
        
        try:
            con = pymysql.connect(host="localhost",user="root",password="abc@123",database="library_management")
            cur = con.cursor()
            
            
            cur.execute("select * from book_info where title=%s",(title.get()))
            rows1 = cur.fetchall() 
        
            for row in rows1:
                listTree.insert("",tk.END,values=row)
            
            
            
                             
                
        except Exception as es:
            messagebox.showerror("Error" , f"Error Dui to : {str(es)}",parent=root)

def on_enter(e):
    e.widget['background'] = 'white'
    e.widget['foreground'] = 'black'

def on_leave(e):
    e.widget['background'] = 'black'   
    e.widget['foreground'] = 'white'
    

    
def book_info():
    global title,root,con,cur,listTree
    root = tk.Tk()
    root.title("Student Details")
    root.attributes('-fullscreen', True)
    root.configure(bg='#006B38')
    
    
    font1 = tkFont.Font(family="Helvetica",size=10,weight="bold")
    
    
    
    headingFrame1 = Frame(root, bg="#ffff99", bd=5)
    headingFrame1.place(relx=0.2, rely=0.04, relwidth=0.6, relheight=0.10)

    headingLabel = Label(headingFrame1, text="Book Info", bg='black', fg='white',
                         font=('Courier', 15))
    headingLabel.place(relx=0, rely=0.01, relwidth=1, relheight=1)
    
    lbl_rno = Label(root,text="Book Title",font=font1)
    lbl_rno.place(relx=0.25, rely=0.2, relwidth=0.09, relheight=0.04)
    title = Entry(root,bd=3.5,font=font1)
    title.place(relx=0.38, rely=0.2, relwidth=0.39, relheight=0.035)
    title.focus()  
    
    
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
    listTree.place(relx=0.25, rely=0.415, relwidth=0.52, relheight=0.45)
    vsb.place(relx=0.757,rely=0.4161,relheight=0.447)
    hsb.place(relx=0.251,rely=0.838,relwidth=0.515)
    ttk.Style().configure("Treeview",font=('Times new Roman',15))
    
    
    view = Button(root, text="View Avail Books", bg='black', fg='white',command=viewAll)
    view.place(relx=0.30, rely=0.30, relwidth=0.08, relheight=0.06)
    view.bind("<Enter>", on_enter)
    view.bind("<Leave>", on_leave)
    
    
    
    clr = Button(root, text="CLEAR", bg='black', fg='white',command=clear)    
    clr.place(relx=0.466, rely=0.30, relwidth=0.08, relheight=0.06)
    clr.bind("<Enter>", on_enter)
    clr.bind("<Leave>", on_leave)
      
    
    
   
    
    search = Button(root,text="Search",bg = 'black',fg='white',command=search_book)
    search.place(relx=0.63, rely=0.30, relwidth=0.08, relheight=0.06)   
    search.bind("<Enter>", on_enter)
    search.bind("<Leave>", on_leave)
    
    
    
    
    
    
    quitBtn = Button(root, text="X",fg="red", bg='#d1ccc0',command=root.destroy)
    quitBtn.place(relx=1.0, y=0, anchor="ne")
    root.mainloop()
    
    
