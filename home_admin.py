import tkinter as tk
from tkinter import Label,Frame,Button
from Book_Info import book
from Stud_Info import stud
from issue_return_book import book_status

def main():
    root = tk.Tk()
    root.title("Admin Library Management")
    root.attributes('-fullscreen', True)
    root.configure(bg='#006B38')

    

    headingFrame1 = Frame(root, bg="#ffff99", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    headingLabel = Label(headingFrame1, text="Library Management System", bg='black', fg='white',
                         font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    book_info = Button(root, text="Book Info", bg='black', fg='white',command=book)
    book_info.place(relx=0.28, rely=0.4, relwidth=0.4, relheight=0.1)

    stud_info = Button(root, text="Student Info", bg='black', fg='white',command=stud)
    stud_info.place(relx=0.28, rely=0.5, relwidth=0.4, relheight=0.1)
    
    issue = Button(root, text="Issue/Return Book", bg='black', fg='white',command=book_status)
    issue.place(relx=0.28, rely=0.6, relwidth=0.4, relheight=0.1)
    
    quitBtn = Button(root, text="X",fg="red", bg='#d1ccc0',command=root.destroy)
    quitBtn.place(relx=1.0, y=0, anchor="ne")



    #root.mainloop()
