import tkinter as tk
from tkinter import Button,Frame,Label,Entry,ttk,messagebox
import tkinter.font as tkFont
import pymysql
import datetime as DT
from datetime import date

def clear():
    bid.delete(0,"end")
    title.delete(0,"end")
    sid.delete(0,"end")
    name.delete(0,"end")
    for item in listTree.get_children():
        listTree.delete(item)

def viewAll():
        for item in listTree.get_children():
            listTree.delete(item)   
    
        try:
            con = pymysql.connect(host="localhost",user="root",password="abc@123",database="library_management")
            cur = con.cursor()
            
            cur.execute("select * from issue_book")
            rows = cur.fetchall()
            
            for row in rows:
                listTree.insert("",tk.END,values=row)
                
        except Exception as es:
            messagebox.showerror("Error" , f"Error Dui to : {str(es)}",parent=root)

def fine_paid():
    try:
        con = pymysql.connect(host="localhost",user="root",password="abc@123",database="library_management")
        cur1 = con.cursor()
        cur = con.cursor()
        cur.execute("select * from issue_book where sid=%s",(sid.get()))
        fine = cur.fetchone()
        if fine[4]==0.0:
            messagebox.showerror("Error","No Fine to pay!!",parent=root)
        elif fine[4]>0.0:
            #messagebox.showinfo("Fine","Fine to be paid is : {}Rs.".format(fine[4]))
            cur1.execute("update issue_book set fine=0 where sid=%s",(sid.get()))
            messagebox.showinfo("Paid","Fine of Rs.{} is paid!!".format(fine[4]),parent=root)
            con.commit()
        else:
            messagebox.showerror("Error","Wrong fine format!!!",parent=root)
    except Exception as es:
            messagebox.showerror("Error" , f"Error Dui to : {str(es)}",parent=root)

def pay_fine():
    try:
        con = pymysql.connect(host="localhost",user="root",password="abc@123",database="library_management")
        cur = con.cursor()
        cur.execute("select * from issue_book where sid=%s",(sid.get()))
        fine = cur.fetchone()
        if fine[4]==0.0:
            messagebox.showerror("Error","No Fine to pay!!",parent=root)
        elif fine[4]>0.0:
            messagebox.showinfo("Fine","Fine to be paid is : {}Rs.".format(fine[4]),parent=root)
        else:
            messagebox.showerror("error","wrong fine format!!",parent=root)
            
    except Exception as es:
            messagebox.showerror("Error" , f"Error Dui to : {str(es)}",parent=root)
        

def search():
        for item in listTree.get_children():
            listTree.delete(item)     
        
        try:
            con = pymysql.connect(host="localhost",user="root",password="abc@123",database="library_management")
            cur = con.cursor()
            
            cur.execute("select * from book_info where title=%s",(title.get()))
            rows = cur.fetchone() 
            if(rows[4] == "avail"):
                    messagebox.showinfo("Available","id = {} \n The book required is AVAILABLE".format(rows[0]),parent=root)
                    bid.insert(0,rows[0])
                    con.commit()
            elif (rows[4] == "issued"):
                    messagebox.showinfo("Unavailable","id = {} \n The book required is NOT AVAILABLE".format(rows[0]),parent=root)
                    title.delete(0,"end")
                    con.commit()
            else:
                   messagebox.showerror("Error","The title mentioned is not in library!!",parent=root)
                   
        
                                               
        except Exception as es:
            messagebox.showerror("Error" , f"Error Dui to : {str(es)}",parent=root)
            

    


def return_book():
    date_today = date.today()
    try:
        con = pymysql.connect(host="localhost",user="root",password="abc@123",database="library_management")
        cur = con.cursor()
        cur1 = con.cursor()
        cur2 = con.cursor()
        cur3 = con.cursor()
        cur4 = con.cursor()
        cur5 = con.cursor()
        cur6 = con.cursor()
        cur.execute("update issue_book set actual_dor=%s where sid=%s",(date_today,sid.get()))
        cur1.execute("select * from issue_book where sid=%s",(sid.get()))
        data = cur1.fetchone()
        date_db = data[3]
        #date_today1 = date_today + DT.timedelta(days=2)
        if(date_today>date_db):
            final = date_today-date_db
            final_count = final.days
                         
            fine = data[4] + (final_count*2.5)
            cur2.execute("update issue_book set fine=%s,dor=%s where sid=%s",(fine,date_today,sid.get()))
            messagebox.showinfo("Updated","Fine updated!!\nPay Fine",parent=root)
            con.commit()
          
        else:    
        #elif (date_today <= date_db):
            cur3.execute("select * from issue_book where sid=%s",(sid.get()))
            fine = cur3.fetchone()
            if fine[4]==0.0:
                cur4.execute("Update issue_book INNER JOIN stud_info on issue_book.sid=stud_info.id set book_issued=%s where issue_book.sid=%s",("NO",sid.get()))
                cur5.execute("Update issue_book INNER JOIN book_info on issue_book.bid=book_info.bid set status=%s where issue_book.bid=%s",("avail",bid.get()))
                cur6.execute("delete from issue_book where sid=%s",(sid.get()))
                messagebox.showinfo("Returned","Book Returned Successfully!!!",parent=root)
                con.commit() 
            else:
                messagebox.showerror("Error","Fine is not paid!!!\nYou have not pay Rs.{}".format(fine[4]),parent=root)
        
        con.commit()
    
    except Exception as es:
        messagebox.showerror("Error" , f"Error Due to : {str(es)}")                
            
            

            






def issue():
    global dor
    for item in listTree.get_children():
        listTree.delete(item)
    try:
        con = pymysql.connect(host="localhost",user="root",password="abc@123",database="library_management")
        cur = con.cursor()
        cur1 = con.cursor()
        cur2 = con.cursor()
        cur3 = con.cursor()
        #cur4 = con.cursor()
        book_id=bid.get()
        mem_id = sid.get()
        doi = date.today()
        dor = doi +  DT.timedelta(days=7)
        fine = 0.0
        cur3.execute("select * from stud_info where id=%s",sid.get())
        row = cur3.fetchone()
        if row[6]=="YES":
            messagebox.showerror("Issued Book","Already issued a book!!",parent=root)
        else:            
            cur1.execute("select * from book_info where title=%s",(title.get()))
            cur2.execute("update stud_info set book_issued='YES' where id=%s",(sid.get()))
            rows = cur1.fetchone() 
            if(rows[4] == "avail"):
                cur.execute("insert into issue_book values (%s,%s,%s,%s,%s,%s)",(book_id,mem_id,doi,dor,fine,dor))
                data=(book_id,mem_id,doi,dor,fine)
                if data==None:
                    messagebox.showerror("Error" , "Enter all data")
                else:
                    cur.execute("update book_info set status = %s where bid = %s",("issued",book_id))
                    messagebox.showinfo("Success" , "Successfully Issued",parent=root )                        
                
      
            elif(rows[4] == "issued"):
                messagebox.showinfo("Unavailable","id = {} \n The book required is NOT AVAILABLE".format(rows[0]),parent=root)
            else:
                messagebox.showerror("Error","The title mentioned is not in library!!",parent=root)
            con.commit()
            
        
    except Exception as es:
        messagebox.showerror("Error" , f"Error Due to : {str(es)}",parent=root)


def on_enter(e):
    e.widget['background'] = 'white'
    e.widget['foreground'] = 'black'

def on_leave(e):
    e.widget['background'] = 'black'   
    e.widget['foreground'] = 'white'


def book_status():
    global bid,title,sid,name,root,listTree,fine
    root = tk.Tk()
    root.title("Issue/Return Book")
    root.attributes('-fullscreen', True)
    root.configure(bg='#006B38')
    fine = 0.0
    
    font1 = tkFont.Font(family="Helvetica",size=10,weight="bold")
    
    
    
    headingFrame1 = Frame(root, bg="#ffff99", bd=5)
    headingFrame1.place(relx=0.2, rely=0.04, relwidth=0.6, relheight=0.10)

    headingLabel = Label(headingFrame1, text="Issue/Return Status", bg='black', fg='white',
                         font=('Courier', 15))
    headingLabel.place(relx=0, rely=0.01, relwidth=1, relheight=1)
    
    lbl_bid = Label(root,text="Book ID",font=font1)
    lbl_bid.place(relx=0.20, rely=0.2, relwidth=0.09, relheight=0.04)
    bid = Entry(root,bd=3.5,font=font1)
    bid.place(relx=0.30, rely=0.2, relwidth=0.39, relheight=0.035)
    bid.focus()  
    
    lbl_title = Label(root,text="Book Title",font=font1)
    lbl_title.place(relx=0.20, rely=0.25, relwidth=0.09, relheight=0.04)
    title = Entry(root,bd=3.5,font=font1)
    title.place(relx=0.30, rely=0.25, relwidth=0.39, relheight=0.035)
    
    lbl_sid = Label(root,text="Student ID",font=font1)
    lbl_sid.place(relx=0.20, rely=0.30, relwidth=0.09, relheight=0.04)
    sid = Entry(root,bd=3.5,font=font1) 
    sid.place(relx=0.30, rely=0.30, relwidth=0.39, relheight=0.035)
    
    #lbl_name = Label(root,text="Name",font=font1)
    #lbl_name.place(relx=0.20, rely=0.35, relwidth=0.09, relheight=0.04)
    #name = Entry(root,bd=3.5,font=font1)
    #name.place(relx=0.30, rely=0.35, relwidth=0.39, relheight=0.035)
    
   
    
    
    listTree = ttk.Treeview(root,height=14,selectmode = "extended")
    listTree["columns"]=("1","2","3","4","5")
    listTree['show'] = 'headings'
    vsb = ttk.Scrollbar(root,orient="vertical",command=listTree.yview)
    hsb = ttk.Scrollbar(root,orient="horizontal",command=listTree.xview)
    listTree.configure(yscrollcommand=vsb.set,xscrollcommand=hsb.set)
    listTree.heading("1", text='Book ID')
    listTree.column("1", width=100,minwidth=100,anchor='center')
    listTree.heading("2", text='Stud ID')
    listTree.column("2", width=100, minwidth=100,anchor='center')
    listTree.heading("3", text='Date of Issue')
    listTree.column("3", width=150, minwidth=150,anchor='center')
    listTree.heading("4", text='Date of Return')
    listTree.column("4", width=150, minwidth=150,anchor='center')
    listTree.heading("5", text='Fine')
    listTree.column("5", width=125, minwidth=125,anchor='center')
    listTree.place(relx=0.20, rely=0.40, relwidth=0.49, relheight=0.45)
    vsb.place(relx=0.68,rely=0.401,relheight=0.448)
    hsb.place(relx=0.2008,rely=0.830,relwidth=0.491)
    ttk.Style().configure("Treeview",font=('Times new Roman',15))
    
    
    search1 = Button(root, text="SEARCH BOOK", bg='black', fg='white',command=search)
    search1.place(relx=0.72, rely=0.19, relwidth=0.08, relheight=0.06)
    search1.bind("<Enter>", on_enter)
    search1.bind("<Leave>", on_leave)
    
    
    issue1 = Button(root, text="ISSUE", bg='black', fg='white',command=issue)
    issue1.place(relx=0.72, rely=0.29, relwidth=0.08, relheight=0.06)
    issue1.bind("<Enter>", on_enter)
    issue1.bind("<Leave>", on_leave)
    
    return1 = Button(root, text="RETURN", bg='black', fg='white',command=return_book)
    return1.place(relx=0.72, rely=0.39, relwidth=0.08, relheight=0.06)
    return1.bind("<Enter>", on_enter)
    return1.bind("<Leave>", on_leave)
    
    pay = Button(root, text="PAY FINE", bg='black', fg='white',command=pay_fine)
    pay.place(relx=0.72, rely=0.49, relwidth=0.08, relheight=0.06)
    pay.bind("<Enter>", on_enter)
    pay.bind("<Leave>", on_leave)
    
    pay1 = Button(root, text="FINE PAID", bg='black', fg='white',command=fine_paid)
    pay1.place(relx=0.72, rely=0.59, relwidth=0.08, relheight=0.06)
    pay1.bind("<Enter>", on_enter)
    pay1.bind("<Leave>", on_leave)
    
    view = Button(root, text="VIEW ALL", bg='black', fg='white',command=viewAll)
    view.place(relx=0.72, rely=0.69, relwidth=0.08, relheight=0.06)
    view.bind("<Enter>", on_enter)
    view.bind("<Leave>", on_leave)

    
    clr = Button(root, text="CLEAR", bg='black', fg='white',command=clear)
    clr.place(relx=0.72, rely=0.79, relwidth=0.08, relheight=0.06)   
    clr.bind("<Enter>", on_enter)
    clr.bind("<Leave>", on_leave)
    
    
    
    
    
    quitBtn = Button(root, text="X",fg="red", bg='#d1ccc0',command=root.destroy)
    quitBtn.place(relx=1.0, y=0, anchor="ne")
    root.mainloop()
    
    
#book_status()




   