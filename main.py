##############################################################
from tkinter import *
from tkinter.ttk import Treeview
from tkinter import ttk
from tkinter import messagebox, filedialog
import ttkthemes as td
import pandas
import pymysql
import time
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

#######################
uname = StringVar()
upass = StringVar()


def login():
    global count, text
    if uname.get() == '' or upass.get() == '':
        messagebox.showerror("Error", "All fields are required!!")
    elif uname.get() == 'rutu' and upass.get() == '1234':
        showinfo('success',f'welcom {uname.get()}')
        window.destroy()
        import sms.py


        def addStudent():
            def submitadd():
                if idval.get() == '' or nameval.get() == '' or emailval.get() == '' or adressval.get() == '' or genderval.get() == '' or phoneval.get() == '' or dobval.get() == '':
                    messagebox.showerror("Error", "All fields are required!!")
                else:
                    id = idval.get()
                    if '0' <= id <= '9':
                        name = nameval.get()
                        email = emailval.get()
                        address = adressval.get()
                        mobile = phoneval.get()
                        if '0' <= mobile <= '9':

                            gender = genderval.get()
                            gender.upper()

                            if gender == 'M' or gender == 'F':
                                dob = dobval.get()
                                addedtime = time.strftime('%H:%M:%S')
                                addeddate = time.strftime('%d/%m/%Y')
                                try:
                                    strr = 'insert into studentdata1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                                    mycursor.execute(strr, (
                                    id, name, mobile, email, address, gender, dob, addeddate, addedtime))
                                    con.commit()
                                    res = messagebox.askyesnocancel("Notifications",
                                                                    'Id {} Name {} Added Successfully..Do want to clean the form?'.format(
                                                                        id, name), parent=addroot)
                                    if res:
                                        idval.set('')
                                        nameval.set('')
                                        emailval.set('')
                                        adressval.set('')
                                        genderval.set('')
                                        phoneval.set('')
                                        dobval.set('')

                                except:
                                    messagebox.showerror("Notification", "Id already exists Try another Id ",
                                                         parent=addroot)
                                strr = 'select * from studentdata1'
                                mycursor.execute(strr)
                                datas = mycursor.fetchall()
                                studentTable.delete(*studentTable.get_children())
                                for i in datas:
                                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                                    studentTable.insert('', END, values=vv)
                            else:
                                messagebox.showerror("Error", "Please Enter 'M or 'F'")

                        else:
                            messagebox.showerror("Error", 'Enter correct Mobile Number')
                    else:
                        messagebox.showerror("Error", 'Id Has To Be A number')

            addroot = Toplevel(dataentryframe)
            addroot.grab_set()
            addroot.geometry("470x470+130+170")
            addroot.title("Student Management System")
            addroot.config(bg='gray20')
            addroot.iconbitmap = ('icon.ico')
            addroot.resizable(0, 0)
            #########################labels##############################
            idlabel = Label(addroot, text="Id :", bg='gray20',fg='white', font=('times', 20, 'bold'), anchor='w')
            idlabel.place(x=10, y=10)

            namelabel = Label(addroot, text="Name :", bg='gray20',fg='white', font=('times', 20, 'bold'))
            namelabel.place(x=10, y=70)

            emaillabel = Label(addroot, text="Email :", bg='gray20',fg='white', font=('times', 20, 'bold'))
            emaillabel.place(x=10, y=190)

            phonelabel = Label(addroot, text="Mobile No :", bg='gray20',fg='white', font=('times', 20, 'bold'))
            phonelabel.place(x=10, y=130)

            addresslabel = Label(addroot, text="Address :", bg='gray20',fg='white', font=('times', 20, 'bold'))
            addresslabel.place(x=10, y=250)

            genderlabel = Label(addroot, text="Gender :", bg='gray20',fg='white', font=('times', 20, 'bold'))
            genderlabel.place(x=10, y=310)

            birthlabel = Label(addroot, text="D.O.B :", bg='gray20',fg='white', font=('times', 20, 'bold'))
            birthlabel.place(x=10, y=370)
            ################################################Entry boxes#######################################################
            idval = StringVar()
            nameval = StringVar()
            emailval = StringVar()
            adressval = StringVar()
            genderval = StringVar()
            phoneval = StringVar()
            dobval = StringVar()

            identry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=idval, width=24)
            identry.place(x=210, y=10)
            nameentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval, width=24)
            nameentry.place(x=210, y=70)
            phoneentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=phoneval, width=24)
            phoneentry.place(x=210, y=130)
            emailentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval, width=24)
            emailentry.place(x=210, y=190)
            addressentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=adressval, width=24)
            addressentry.place(x=210, y=250)
            genderentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval, width=24)
            genderentry.place(x=210, y=310)
            dobentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval, width=24)
            dobentry.place(x=210, y=370)
            ###########################add button #################################################
            submitbtn = Button(addroot, text='SUBMIT', font=('arial', 15, 'bold'), width=15, activebackground='gray20',
                               activeforeground='white', command=submitadd)
            submitbtn.place(x=125, y=422)

            addroot.mainloop()

        def searchStudent():
            def search():
                try:
                    id = idval.get()
                    name = nameval.get()
                    email = emailval.get()
                    address = adressval.get()
                    gender = genderval.get()
                    mobile = phoneval.get()
                    dob = dobval.get()
                    addeddate = time.strftime('%d/%m/%Y')
                    if (id != ''):
                        strr = 'select * from studentdata1 where id=%s'
                        mycursor.execute(strr, (id))
                        datas = mycursor.fetchall()
                        studentTable.delete(*studentTable.get_children())
                        for i in datas:
                            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                            studentTable.insert('', END, values=vv)

                    elif (name != ''):
                        strr = 'select * from studentdata1 where name=%s'
                        mycursor.execute(strr, (name))
                        datas = mycursor.fetchall()
                        studentTable.delete(*studentTable.get_children())
                        for i in datas:
                            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                            studentTable.insert('', END, values=vv)

                    elif (email != ''):
                        strr = 'select * from studentdata1 where email=%s'
                        mycursor.execute(strr, (email))
                        datas = mycursor.fetchall()
                        studentTable.delete(*studentTable.get_children())
                        for i in datas:
                            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                            studentTable.insert('', END, values=vv)

                    elif (mobile != ''):
                        strr = 'select * from studentdata1 where mobile=%s'
                        mycursor.execute(strr, (mobile))
                        datas = mycursor.fetchall()
                        studentTable.delete(*studentTable.get_children())
                        for i in datas:
                            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                            studentTable.insert('', END, values=vv)

                    elif (address != ''):
                        strr = 'select * from studentdata1 where address=%s'
                        mycursor.execute(strr, (address))
                        datas = mycursor.fetchall()
                        studentTable.delete(*studentTable.get_children())
                        for i in datas:
                            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                            studentTable.insert('', END, values=vv)

                    elif (gender != ''):
                        strr = 'select * from studentdata1 where gender=%s'
                        mycursor.execute(strr, (gender))
                        datas = mycursor.fetchall()
                        studentTable.delete(*studentTable.get_children())
                        for i in datas:
                            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                            studentTable.insert('', END, values=vv)


                    elif (addeddate != ''):
                        strr = 'select * from studentdata1 where addeddate=%s'
                        mycursor.execute(strr, (addeddate))
                        datas = mycursor.fetchall()
                        studentTable.delete(*studentTable.get_children())
                        for i in datas:
                            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                            studentTable.insert('', END, values=vv)

                    elif (dob != ''):
                        strr = 'select * from studentdata1 where dob=%s'
                        mycursor.execute(strr, (dob))
                        datas = mycursor.fetchall()
                        studentTable.delete(*studentTable.get_children())
                        for i in datas:
                            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                            studentTable.insert('', END, values=vv)
                except:
                    messagebox.showerror("Oops", 'Please Connect to Database and Fill Entry to be Searched ')

            searchroot = Toplevel(dataentryframe)
            searchroot.grab_set()
            searchroot.geometry("470x540+130+120")
            searchroot.title("Search")
            searchroot.config(bg='gray20')
            searchroot.iconbitmap = ('icon.ico')
            searchroot.resizable(0, 0)
            #########################labels##############################
            idlabel = Label(searchroot, text="Id :", bg='gray20',fg='white', font=('times', 20, 'bold'), anchor='w')
            idlabel.place(x=10, y=10)

            namelabel = Label(searchroot, text="Name :", bg='gray20',fg='white', font=('times', 20, 'bold'))
            namelabel.place(x=10, y=70)

            emaillabel = Label(searchroot, text="Email :", bg='gray20',fg='white', font=('times', 20, 'bold'))
            emaillabel.place(x=10, y=190)

            phonelabel = Label(searchroot, text="Mobile No :", bg='gray20',fg='white', font=('times', 20, 'bold'))
            phonelabel.place(x=10, y=130)

            addresslabel = Label(searchroot, text="Address :", bg='gray20',fg='white', font=('times', 20, 'bold'))
            addresslabel.place(x=10, y=250)

            genderlabel = Label(searchroot, text="Gender :", bg='gray20',fg='white', font=('times', 20, 'bold'))
            genderlabel.place(x=10, y=310)

            birthlabel = Label(searchroot, text="D.O.B :", bg='gray20',fg='white', font=('times', 20, 'bold'))
            birthlabel.place(x=10, y=370)

            datelabel = Label(searchroot, text="Date :", bg='gray20',fg='white', font=('times', 20, 'bold'))
            datelabel.place(x=10, y=430)
            ################################################Entry boxes#######################################################
            idval = StringVar()
            nameval = StringVar()
            emailval = StringVar()
            adressval = StringVar()
            genderval = StringVar()
            phoneval = StringVar()
            dobval = StringVar()
            dateval = StringVar()

            identry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=idval, width=24)
            identry.place(x=210, y=10)
            nameentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval, width=24)
            nameentry.place(x=210, y=70)
            phoneentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=phoneval, width=24)
            phoneentry.place(x=210, y=130)
            emailentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval, width=24)
            emailentry.place(x=210, y=190)
            addressentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=adressval, width=24)
            addressentry.place(x=210, y=250)
            genderentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval, width=24)
            genderentry.place(x=210, y=310)
            dobentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval, width=24)
            dobentry.place(x=210, y=370)
            dateentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=dateval, width=24)
            dateentry.place(x=210, y=430)
            ###########################add button #################################################
            submitbtn = Button(searchroot, text='SUBMIT', font=('arial', 15, 'bold'), width=15, activebackground='gray20',
                               activeforeground='white', command=search)
            submitbtn.place(x=125, y=490)

            searchroot.mainloop()

        def deleteStudent():
            try:
                cc = studentTable.focus()
                content = studentTable.item(cc)
                pp = content['values'][0]
                strr = 'delete from studentdata1 where id=%s'
                mycursor.execute(strr, (pp))
                con.commit()
                messagebox.showinfo("Notification", f'Id {pp} deleted successfully')

                strr = 'select * from studentdata1'
                mycursor.execute(strr)
                datas = mycursor.fetchall()
                studentTable.delete(*studentTable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    studentTable.insert('', END, values=vv)
            except:
                messagebox.showerror("Oops", "There is nothing to Delete")

        def updateStudent():
            def update():
                if idval.get() == '' or nameval.get() == '' or emailval.get() == '' or adressval.get() == '' or genderval.get() == '' or phoneval.get() == '' or dobval.get() == '':
                    messagebox.showerror("Error", "All fields are required!!")
                else:
                    id = idval.get()
                    name = nameval.get()
                    mobile = phoneval.get()
                    email = emailval.get()
                    address = adressval.get()
                    gender = genderval.get()
                    dob = dobval.get()
                    date = dateval.get()
                    time = timeval.get()

                    strr = 'update studentdata1 set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
                    mycursor.execute(strr, (name, mobile, email, address, gender, dob, date, time, id))
                    con.commit()
                    messagebox.showinfo("Notification", f'Id {id} Modified successfully...', parent=updateroot)
                    strr = 'select * from studentdata1'
                    mycursor.execute(strr)
                    datas = mycursor.fetchall()
                    studentTable.delete(*studentTable.get_children())
                    for i in datas:
                        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                        studentTable.insert('', END, values=vv)

            updateroot = Toplevel(dataentryframe)
            updateroot.grab_set()
            updateroot.geometry("470x610+130+80")
            updateroot.title("Update")
            updateroot.config(bg='gray20')
            updateroot.iconbitmap = ('icon.ico')
            updateroot.resizable(0, 0)
            #########################labels##############################
            idlabel = Label(updateroot, text="Update Id ", bg='gray20',fg='white', font=('times', 20, 'bold'), anchor='w')
            idlabel.place(x=10, y=10)

            namelabel = Label(updateroot, text="Update Name ", bg='gray20', fg='white',font=('times', 20, 'bold',), anchor='w')
            namelabel.place(x=10, y=70)

            emaillabel = Label(updateroot, text="Update Email ", bg='gray20', fg='white',font=('times', 20, 'bold',),
                               anchor='w')
            emaillabel.place(x=10, y=190)

            phonelabel = Label(updateroot, text="Update Mobile ", bg='gray20', fg='white',font=('times', 20, 'bold',),
                               anchor='w')
            phonelabel.place(x=10, y=130)

            addresslabel = Label(updateroot, text="Update Address ", bg='gray20',fg='white', font=('times', 20, 'bold',),
                                 anchor='w')
            addresslabel.place(x=10, y=250)

            genderlabel = Label(updateroot, text="Update Gender ", bg='gray20', fg='white',font=('times', 20, 'bold',),
                                anchor='w')
            genderlabel.place(x=10, y=310)

            birthlabel = Label(updateroot, text="Update D.O.B ", bg='gray20',fg='white', font=('times', 20, 'bold',),
                               anchor='w')
            birthlabel.place(x=10, y=370)

            datelabel = Label(updateroot, text="Update Date ", bg='gray20',fg='white', font=('times', 20, 'bold',), anchor='w')
            datelabel.place(x=10, y=430)

            datelabel = Label(updateroot, text="Update Time ", bg='gray20',fg='white', font=('times', 20, 'bold',), anchor='w')
            datelabel.place(x=10, y=490)
            ################################################Entry boxes#######################################################
            idval = StringVar()
            nameval = StringVar()
            emailval = StringVar()
            adressval = StringVar()
            genderval = StringVar()
            phoneval = StringVar()
            dobval = StringVar()
            dateval = StringVar()
            timeval = StringVar()

            identry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=idval, width=24)
            identry.place(x=210, y=10)
            nameentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval, width=24)
            nameentry.place(x=210, y=70)
            phoneentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=phoneval, width=24)
            phoneentry.place(x=210, y=130)
            emailentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval, width=24)
            emailentry.place(x=210, y=190)
            addressentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=adressval, width=24)
            addressentry.place(x=210, y=250)
            genderentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval, width=24)
            genderentry.place(x=210, y=310)
            dobentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval, width=24)
            dobentry.place(x=210, y=370)
            dateentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=dateval, width=24)
            dateentry.place(x=210, y=430)
            timeentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=timeval, width=24)
            timeentry.place(x=210, y=490)
            ###########################add button #################################################
            submitbtn = Button(updateroot, text='SUBMIT',bg='white',fg='black', font=('arial', 15, 'bold'), width=15, activebackground='blue',
                               activeforeground='white', command=update)
            submitbtn.place(x=125, y=555)

            cc = studentTable.focus()
            content = studentTable.item(cc)
            pp = content['values']

            if (len(pp) != 0):
                idval.set(pp[0])
                nameval.set(pp[1])
                phoneval.set(pp[2])
                emailval.set(pp[3])
                adressval.set(pp[4])
                genderval.set(pp[5])

                dobval.set(pp[6])
                dateval.set(pp[7])
                timeval.set(pp[8])

            updateroot.mainloop()

        def showStudent():
            try:

                strr = 'select * from studentdata1'
                mycursor.execute(strr)
                datas = mycursor.fetchall()
                studentTable.delete(*studentTable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    studentTable.insert('', END, values=vv)
            except:
                messagebox.showerror("Oops", "First connect to database")

        def exportStudent():
            ff = filedialog.asksaveasfilename()
            gg = studentTable.get_children()
            id, name, mobile, email, address, gender, dob, addeddate, addedtime = [], [], [], [], [], [], [], [], []
            for i in gg:
                content = studentTable.item(i)
                pp = content['values']
                id.append(pp[0]), name.append(pp[1]), mobile.append(pp[2]), email.append(pp[3]), address.append(
                    pp[4]), gender.append(pp[5]),
                dob.append(pp[6]), addeddate.append(pp[7]), addedtime.append(pp[8])

            dd = ['Id', 'Name', 'Mobile', 'Email', 'Address', 'Gender', 'D.O.B', 'Added Date', 'Added Time']
            df = pandas.DataFrame(list(zip(id, name, mobile, email, address, gender, dob, addeddate, addedtime)),
                                  columns=dd)
            paths = r'{}.csv'.format(ff)
            df.to_csv(paths, index=False)
            messagebox.showinfo("Notification", 'Student Data is Saved {}'.format(paths))

        def exitStudent():
            res = messagebox.askyesnocancel('Notification', "Do you want to exit?")
            if res:
                window.destroy()

        ############################################connect database pe click karne pe window###################################

        def connectDb():
            def submitdb():
                global con, mycursor
                host = hostval.get()
                user = userval.get()
                password = passwordval.get()

                try:
                    con = pymysql.connect(host=host, user=user, password=password)
                    mycursor = con.cursor()
                except:
                    messagebox.showerror("Notifications", "Data is incorrect,please try again")
                    return
                try:
                    strr = 'create database studentmanagementsystem1'
                    mycursor.execute(strr)
                    strr = 'use studentmanagementsystem1'
                    mycursor.execute(strr)
                    strr = 'create table studentdata1(id int,name varchar(20),mobile varchar(12),email varchar(30),address varchar(100),gender varchar(50),dob varchar(50),date varchar(50),time varchar(50))'
                    mycursor.execute(strr)

                    strr = 'alter table studentdata1 modify column id int not null'
                    mycursor.execute(strr)
                    strr = 'alter table studentdata1 modify column id int primary key'
                    mycursor.execute(strr)
                    messagebox.showinfo("Notification", 'Database created and now you are connected to the database...',
                                        parent=dbroot)

                except:
                    strr = 'use studentmanagementsystem1'
                    mycursor.execute(strr)
                    messagebox.showinfo("Notification", 'Now you are connected to the database...', parent=dbroot)
                    dbroot.destroy()

            dbroot = Toplevel()
            dbroot.grab_set()
            dbroot.geometry('470x250+730+230')
            dbroot.config(bg='darkgoldenrod2')
            dbroot.iconbitmap('icon.ico')
            dbroot.resizable(0, 0)
            ####################connect labels###########################################
            idlabel1 = Label(dbroot, text="Host Name :", bg='darkgoldenrod2', fg='white',width=13, font=('arial', 20, 'bold'),
                             )
            idlabel1.place(x=10, y=10)

            namelabel1 = Label(dbroot, text="User Name :", bg='darkgoldenrod2', fg='white', width=13, font=('arial', 20, 'bold'),

                               )
            namelabel1.place(x=10, y=70)

            passwordlabel1 = Label(dbroot, text="Password :", bg='darkgoldenrod2', fg='white', width=13, font=('arial', 20, 'bold'),

                                   )
            passwordlabel1.place(x=10, y=130)
            #################################################################Entrybox
            hostval = StringVar()
            userval = StringVar()
            passwordval = StringVar()
            hostEntry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=hostval)
            hostEntry.place(x=250, y=10)

            userEntry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=userval)
            userEntry.place(x=250, y=70)

            passwordEntry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=passwordval)
            passwordEntry.place(x=250, y=130)

            ############################################################################################
            submitbtn = Button(dbroot, text='SUBMIT', font=('arial', 16, 'bold'), width=10, bd=4,bg='white',fg='black',
                                command=submitdb)
            submitbtn.place(x=150, y=190)

            dbroot.mainloop()

        ########################################################################
        def tick():
            time_string = time.strftime("%H:%M:%S")
            date_string = time.strftime("%d/%m/%Y")
            # print(time_string,date_string)
            clock.config(text='  Date :' + date_string + '\nTime : ' + time_string)
            clock.after(200, tick)

        #############################################################################


        def introLabelTick():
            global count, text
            if (count >= len(ss)):
                count = 0
                text = ''
                sliderLabel.config(text=text)
            else:
                text = text + ss[count]
                sliderLabel.config(text=text)
                count += 1

            sliderLabel.after(500, introLabelTick)

        messagebox.showinfo("Successfull", f"Welcome {uname.get()}")
        bg_label.pack_forget()

        login_frame.place_forget()
        logolbl.grid_remove()
        lbluser.grid_remove()
        lblpassword.grid_remove()
        txtuser.grid_remove()
        txtpassword.grid_remove()
        btn_login.grid_remove()
        window.title("Student Management System created by Faizan Khan")
        window.geometry("1174x700+100+10")
        window.config(bg="whitesmoke")

        window.resizable(0, 0)
        window.iconbitmap("icon.ico")
        dataentryframe = Frame(window, bg='whitesmoke')
        dataentryframe.place(x=10, y=80, width=500, height=600)
        frontlabel = Label(dataentryframe, text='.........WELCOME.........', width=30, font=('arial', 22, 'bold'),
                           bg='whitesmoke')
        frontlabel.pack(side=TOP, expand=True)

        addBtn = ttk.Button(dataentryframe, text='1. Add Student', width=25,

                         command=addStudent)
        addBtn.pack(side=TOP, expand=True)

        searchBtn = ttk.Button(dataentryframe, text='2. Search Student',width=25,

                           command=searchStudent)
        searchBtn.pack(side=TOP, expand=True, )

        deleteBtn = ttk.Button(dataentryframe, text='3. Delete Student', width=25,

                            command=deleteStudent)
        deleteBtn.pack(side=TOP, expand=True)

        updatebtn = ttk.Button(dataentryframe, text='4. Update Student', width=25,

                            command=updateStudent)
        updatebtn.pack(side=TOP, expand=True)

        showBtn = ttk.Button(dataentryframe, text='5. Show All', width=25,

                          command=showStudent)
        showBtn.pack(side=TOP, expand=True)

        exportBtn = ttk.Button(dataentryframe, text='6. Export Data', width=25,

                            command=exportStudent)
        exportBtn.pack(side=TOP, expand=True)

        exitBtn = ttk.Button(dataentryframe, text='7. Exit', width=25,

                          command=exitStudent)
        exitBtn.pack(side=TOP, expand=True)

        showdataframe = Frame(window, bg='white', relief=GROOVE, borderwidth=5)
        showdataframe.place(x=550, y=80, width=620, height=600)

        style = ttk.Style()
        style.configure('Treeview.Heading', font=('chiller', 20, 'bold'), foreground='blue')
        style.configure('Treeview', font=('times', 15, 'bold'), foreground='black', bakground='cyan')
        scroll_x = Scrollbar(showdataframe, orient=HORIZONTAL)
        scroll_y = Scrollbar(showdataframe, orient=VERTICAL)
        studentTable = Treeview(showdataframe, columns=(
            'Id', 'Name', 'Mobile No', 'Email', 'Address', 'Gender', 'D.O.B', 'Added Date', 'Added Time'),
                                yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=studentTable.xview)
        scroll_y.config(command=studentTable.yview)

        studentTable.heading('Id', text='Id')
        studentTable.heading('Name', text='Name')
        studentTable.heading('Mobile No', text='Mobile No')
        studentTable.heading('Email', text='Email')
        studentTable.heading('Address', text='Address')
        studentTable.heading('Gender', text='Gender')
        studentTable.heading('D.O.B', text='D.O.B')
        studentTable.heading('Added Date', text='Added Date')
        studentTable.heading('Added Time', text='Added Time')
        studentTable['show'] = 'headings'
        studentTable.column('Id', width=100)
        studentTable.column('Name', width=200)
        studentTable.column('Mobile No', width=200)
        studentTable.column('Address', width=300)
        studentTable.column('Gender', width=100)
        studentTable.column('D.O.B', width=150)
        studentTable.column('Added Date', width=150)
        studentTable.column('Added Time', width=150)

        studentTable.pack(fill=BOTH, expand=1)

        ################################################################
        ss = "Student Management System"
        count = 0
        text = ''

        #######################slider####################################################

        sliderLabel = Label(window, text=ss, font=("arial", 30, 'italic bold'), relief=RIDGE, borderwidth=4,
                            bg='whitesmoke', width=30)
        sliderLabel.place(x=200, y=0)
        introLabelTick()

        ##################################clock#####################################
        clock = Label(window, font=("times", 14, 'bold'), bg='whitesmoke')
        clock.place(x=0, y=0)
        tick()

        ##############################connect databse button######################################
        databasebtn = ttk.Button(window, text="Connect to Database", width=18,

                              command=connectDb)
        databasebtn.place(x=975, y=0)





    else:
        messagebox.showerror("Error", "Invalid Username or Password")

bg_label = Label(window, image=background)
bg_label.pack()


login_frame = Frame(window, bg='white')
login_frame.place(x=400,y=150)

logoimage=PhotoImage(file='student.png')
logolbl = Label(login_frame, image=logoimage, bg='white', bd=0)
logolbl.grid(row=0, columnspan=2, pady=20)

lbluser = Label(login_frame, text='Username', bg='white', fg='navy', image=usericon, compound=LEFT,
                font=('times new roman', 20, 'bold'))
lbluser.grid(row=1, column=0, padx=20, pady=10)

txtuser = Entry(login_frame, bd=5, textvariable=uname, relief=GROOVE, font=('', 15), bg='white', fg='royalblue')
txtuser.grid(row=1, column=1, padx=20)

lblpassword = Label(login_frame, text='Password', bg='white', fg='navy', image=passwordicon, compound=LEFT,
                    font=('times new roman', 20, 'bold'))
lblpassword.grid(row=2, column=0, padx=20, pady=10)

txtpassword = Entry(login_frame, bd=5, textvariable=upass, relief=GROOVE, font=('', 15), bg='white', fg='royalblue')
txtpassword.grid(row=2, column=1, padx=20)

btn_login = Button(login_frame, text="Login", command=login, width=15, font=('times new roman', 14, 'bold'),
                   bg='cornflowerblue', fg='white',cursor='hand2')
btn_login.grid(row=3, column=1, pady=10)

window.mainloop()

