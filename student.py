from tkinter import *
from tkinter import messagebox
import ttkthemes as td
from PIL import ImageTk

window = td.ThemedTk()
window.get_themes()
window.set_theme('radiance')
window.title("Login to Student Management System")
window.geometry("1280x700+20+10")
window.resizable(0, 0)
##############################Images#######################

background = ImageTk.PhotoImage(file='bg.jpg')
usericon = PhotoImage(file='usericon.png')
passwordicon = PhotoImage(file='password1.png')
logoicon = PhotoImage(file='student.png')


def login():
    global count, text
    if txtuser.get() == '' or txtpassword.get() == '':
        messagebox.showerror("Error", "All fields are required!!")
    elif txtuser.get() == 'rutu' and txtpassword.get() == '1234':
        messagebox.showinfo('success',f'welcom {txtuser.get()}')
        window.destroy()
        import sms

    else:
        messagebox.showerror("Error", "Invalid Username or Password")


bg_label = Label(window, image=background)
bg_label.pack()

login_frame = Frame(window, bg='white')
login_frame.place(x=400, y=150)

logoimage = PhotoImage(file='student.png')
logolbl = Label(login_frame, image=logoimage, bg='white', bd=0)
logolbl.grid(row=0, columnspan=2, pady=20)

lbluser = Label(login_frame, text='Username', bg='white', fg='navy', image=usericon, compound=LEFT,
                font=('times new roman', 20, 'bold'))
lbluser.grid(row=1, column=0, padx=20, pady=10)

txtuser = Entry(login_frame, bd=5, relief=GROOVE, font=('', 15), bg='white', fg='royalblue')
txtuser.grid(row=1, column=1, padx=20)

lblpassword = Label(login_frame, text='Password', bg='white', fg='navy', image=passwordicon, compound=LEFT,
                    font=('times new roman', 20, 'bold'))
lblpassword.grid(row=2, column=0, padx=20, pady=10)

txtpassword = Entry(login_frame, bd=5, relief=GROOVE, font=('', 15), bg='white', fg='royalblue')
txtpassword.grid(row=2, column=1, padx=20)

btn_login = Button(login_frame, text="Login", command=login, width=15, font=('times new roman', 14, 'bold'),
                   bg='cornflowerblue', fg='white',cursor='hand2')
btn_login.grid(row=3, column=1, pady=10)

window.mainloop()








