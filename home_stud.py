import tkinter as tk
from tkinter import Label,Frame,Button
from View_Profile import stud_info
from stud_view_book import book_info






def main1():
    root = tk.Tk()
    root.title("Library_Student_Portal")
    #root.minsize(width=400, height=400)
    #root.geometry("600x500")
    root.attributes('-fullscreen', True)
    root.configure(bg='#006B38')

    

    headingFrame1 = Frame(root, bg="#ffff99", bd=5)
    headingFrame1.place(relx=0.2, rely=0.05, relwidth=0.6, relheight=0.16)

    headingLabel = Label(headingFrame1, text="Library Management System", bg='black', fg='white',
                         font=('Courier', 15))
    headingLabel.place(relx=0, rely=0.01, relwidth=1, relheight=1)
    
    

    view = Button(root, text="View Profile", bg='black', fg='white',command=stud_info)
    view.place(relx=0.28, rely=0.4, relwidth=0.4, relheight=0.1)
    
    bookInfo = Button(root, text="Book Info", bg='black', fg='white',command=book_info)
    bookInfo.place(relx=0.28, rely=0.5, relwidth=0.4, relheight=0.1)
    
   
    
    quitBtn = Button(root, text="X",fg="red", bg='#d1ccc0',command=root.destroy)
    quitBtn.place(relx=1.0, y=0, anchor="ne")



