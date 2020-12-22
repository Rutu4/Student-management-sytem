from tkinter import*
import ttkthemes
from tkinter import ttk
import time
import pymysql
from tkinter import messagebox, filedialog
from tkinter.ttk import Treeview
import pandas


################################fun
def export():
    url=filedialog.asksaveasfilename()
    indexing=studentTable.get_children()
    id,name,mobile,email,address,gender,bod,addeddate,addedtime=[],[],[],[],[],[],[],[],[]

    for i in indexing:
        content=studentTable.item(i)
        listdata=content['values']
        id.append(listdata[0]),name.append(listdata[1]),mobile.append(listdata[2]),email.append(listdata[3])
        address.append(listdata[4]),gender.append(listdata[5]),bod.append(listdata[6]),addeddate.append(listdata[7]),addedtime.append(listdata[8])

    columnheading=['id','name','mobile','email','address','gender','bod','addeddate','addedtime']

    pandas_data=pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,bod,addeddate,addedtime)),columns=columnheading)
    paths=r'{}.csv'.format(url)
    pandas_data.to_csv(paths,index=False)

    messagebox.showinfo('information',f'student data saved {paths}')



def updatestd():
    def update():
        if identry.get() == '' or nameentry.get() == '' or emailentry.get() == '' or addressentry.get() == '' or \
           bodentry.get() == '' or genderentry.get() == '' or\
                phoneentry == ''or dateentry.get()=='' or timeentry.get()=='':
            messagebox.showerror('error','all fields are required')
        else:
            strr='update student set name=%s,mobile =%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
            mycurser.execute(strr,(nameentry.get(),phoneentry.get(),emailentry.get(),addressentry.get(),genderentry.get(),bodentry.get(),dateentry.get(),timeentry.get(),identry.get()))

            con.commit()
            messagebox.showinfo('information',f'Id {identry.get()} has updated successfully')
            updateroot.destroy()

            strr='select * from student'
            mycurser.execute(strr)

            data = mycurser.fetchall()  # it stores data in tuple format
            studentTable.delete(*studentTable.get_children())
            for i in data:
                listdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]  #########3onverting to list
                studentTable.insert('', END, values=listdata)

    updateroot=Toplevel()
    updateroot.grab_set()
    updateroot.geometry('470x600+100+70')
    updateroot.title('Update Student')
    updateroot.resizable(0,0)

    idlable=Label(updateroot,text='Id',font=('times new roman',20) ,fg='red4')
    idlable.grid(pady=10,padx=40,sticky=W)

    namelable=Label(updateroot,text='Name',font=('times new roman',20) ,fg='red4')
    namelable.grid(row=1,pady=10,padx=25,sticky=W)

    phonelable=Label(updateroot,text='Phone No',font=('times new roman',20) ,fg='red4')
    phonelable.grid(row=2,pady=10,padx=25,sticky=W)

    emaillable=Label(updateroot,text='Email',font=('times new roman',20) ,fg='red4')
    emaillable.grid(row=3,pady=10,padx=25,sticky=W)

    addresslable=Label(updateroot,text='Address',font=('times new roman',20) ,fg='red4')
    addresslable.grid(row=4,pady=10,padx=25,sticky=W)

    genderlable=Label(updateroot,text='Gender',font=('times new roman',20) ,fg='red4')
    genderlable.grid(row=5,pady=10,padx=25,sticky=W)

    bodlable=Label(updateroot,text='B.O.D',font=('times new roman',20) ,fg='red4')
    bodlable.grid(row=6,pady=10,padx=25,sticky=W)
    datelable=Label(updateroot,text='Date',font=('times new roman',20) ,fg='red4')
    datelable.grid(row=7,pady=10,padx=25,sticky=W)
    timelable=Label(updateroot,text='Time',font=('times new roman',20) ,fg='red4')
    timelable.grid(row=8,pady=10,padx=25,sticky=W)

    identry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, width=24)
    identry.grid(row=0,column=1)

    nameentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, width=24)
    nameentry.grid(row=1,column=1)
    phoneentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, width=24)
    phoneentry.grid(row=2,column=1)
    emailentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, width=24)
    emailentry.grid(row=3,column=1)
    addressentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, width=24)
    addressentry.grid(row=4,column=1)
    genderentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, width=24)
    genderentry.grid(row=5,column=1)
    bodentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, width=24)
    bodentry.grid(row=6,column=1)
    dateentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, width=24)
    dateentry.grid(row=7,column=1)
    timeentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, width=24)
    timeentry.grid(row=8,column=1)

    updatebutton=Button(updateroot,text="UPDATE" ,command=update)
    updatebutton.grid(row=9,column=1,pady=5,padx=25)

    indexing=studentTable.focus()
    content=studentTable.item(indexing)
    listdata=content['values']
    if len(listdata)!=0:
        identry.insert(END,listdata[0])
        nameentry.insert(END,listdata[1])
        phoneentry.insert(END,listdata[2])
        emailentry.insert(END,listdata[3])
        addressentry.insert(END,listdata[4])
        genderentry.insert(END,listdata[5])
        bodentry.insert(END,listdata[6])
        dateentry.insert(END,listdata[7])
        timeentry.insert(END,listdata[8])








def delete():
    try:

         indexing=studentTable.focus()
         content=studentTable.item(indexing)######### gives dict

         gotid=content['values'][0]

         strr='delete from student where id=%s'
         mycurser.execute(strr,gotid)
         con.commit()
         messagebox.showinfo('Information',f'Id {gotid} deleted successfully')
         strr='select * from student'
         mycurser.execute(strr)
         data = mycurser.fetchall()  # it stores data in tuple format
         studentTable.delete(*studentTable.get_children())
         for i in data:
              listdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]  #########3onverting to list
              studentTable.insert('', END, values=listdata)
    except:
         messagebox.showerror('error','Selet row of student to delete')


def searstd():

    def sear_data():
        if identry.get()!='':
           strr='select * from student where id=%s'
           mycurser.execute(strr,(identry.get()))

           data = mycurser.fetchall()  # it stores data in tuple format
           studentTable.delete(*studentTable.get_children())
           for i in data:
               listdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]  #########3onverting to list
               studentTable.insert('', END,values= listdata)


        if nameentry.get()!='':
           strr='select * from student where name=%s'
           mycurser.execute(strr,(nameentry.get()))

           data = mycurser.fetchall()  # it stores data in tuple format
           studentTable.delete(*studentTable.get_children())
           for i in data:
               listdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]  #########3onverting to list
               studentTable.insert('', END,values= listdata)


        if phoneentry.get()!='':
           strr='select * from student where mobile number=%s'
           mycurser.execute(strr,(phoneentry.get()))

           data = mycurser.fetchall()  # it stores data in tuple format
           studentTable.delete(*studentTable.get_children())
           for i in data:
               listdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]  #########3onverting to list
               studentTable.insert('', END,values= listdata)

        if emailentry.get()!='':
           strr='select * from student where email=%s'
           mycurser.execute(strr,(emailentry.get()))

           data = mycurser.fetchall()  # it stores data in tuple format
           studentTable.delete(*studentTable.get_children())
           for i in data:
               listdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]  #########3onverting to list
               studentTable.insert('', END,values= listdata)


        if addressentry.get()!='':
           strr='select * from student where address=%s'
           mycurser.execute(strr,(addressentry.get()))

           data = mycurser.fetchall()  # it stores data in tuple format
           studentTable.delete(*studentTable.get_children())
           for i in data:
               listdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]  #########3onverting to list
               studentTable.insert('', END,values= listdata)


        if bodentry.get()!='':
           strr='select * from student where bod=%s'
           mycurser.execute(strr,(bodentry.get()))

           data = mycurser.fetchall()  # it stores data in tuple format
           studentTable.delete(*studentTable.get_children())
           for i in data:
               listdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]  #########3onverting to list
               studentTable.insert('', END,values= listdata)

        if genderentry.get()!='':
           strr='select * from student where gender=%s'
           mycurser.execute(strr,(genderentry.get()))

           data = mycurser.fetchall()  # it stores data in tuple format
           studentTable.delete(*studentTable.get_children())
           for i in data:
               listdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]  #########3onverting to list
               studentTable.insert('', END,values= listdata)



    searroot=Toplevel()
    searroot.grab_set()
    searroot.geometry('470x520+130+130')
    searroot.title('Search Student')
    searroot.resizable(0,0)

    idlable=Label(searroot,text='Id',font=('times new roman',20) ,fg='red4')
    idlable.grid(pady=15,padx=25,sticky=W)

    namelable=Label(searroot,text='Name',font=('times new roman',20) ,fg='red4')
    namelable.grid(row=1,pady=15,padx=25,sticky=W)

    phonelable=Label(searroot,text='Phone No',font=('times new roman',20) ,fg='red4')
    phonelable.grid(row=2,pady=15,padx=25,sticky=W)

    emaillable=Label(searroot,text='Email',font=('times new roman',20) ,fg='red4')
    emaillable.grid(row=3,pady=15,padx=25,sticky=W)

    addresslable=Label(searroot,text='Address',font=('times new roman',20) ,fg='red4')
    addresslable.grid(row=4,pady=15,padx=25,sticky=W)

    genderlable=Label(searroot,text='Gender',font=('times new roman',20) ,fg='red4')
    genderlable.grid(row=5,pady=15,padx=25,sticky=W)

    bodlable=Label(searroot,text='B.O.D',font=('times new roman',20) ,fg='red4')
    bodlable.grid(row=6,pady=15,padx=25,sticky=W)

    identry = Entry(searroot, font=('roman', 15, 'bold'), bd=5, width=24)
    identry.grid(row=0,column=1)

    nameentry = Entry(searroot, font=('roman', 15, 'bold'), bd=5, width=24)
    nameentry.grid(row=1,column=1)
    phoneentry = Entry(searroot, font=('roman', 15, 'bold'), bd=5, width=24)
    phoneentry.grid(row=2,column=1)
    emailentry = Entry(searroot, font=('roman', 15, 'bold'), bd=5, width=24)
    emailentry.grid(row=3,column=1)
    addressentry = Entry(searroot, font=('roman', 15, 'bold'), bd=5, width=24)
    addressentry.grid(row=4,column=1)
    genderentry = Entry(searroot, font=('roman', 15, 'bold'), bd=5, width=24)
    genderentry.grid(row=5,column=1)
    bodentry = Entry(searroot, font=('roman', 15, 'bold'), bd=5, width=24)
    bodentry.grid(row=6,column=1)

    searbutton=Button(searroot,text="Search" ,command=sear_data)
    searbutton.grid(row=7,column=1,pady=5,padx=10)




def iexit():
    res=messagebox.askyesno('confirm','Do You Want To Exit')
    if res==True:
        root.destroy()
    else:
        pass

def showstd():
    strr='select * from student'
    mycurser.execute(strr)

    data = mycurser.fetchall()  # it stores data in tuple format
    studentTable.delete(*studentTable.get_children())
    for i in data:
        listdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]  #########3onverting to list
        studentTable.insert('', END,values= listdata)


def addstd():


    def adddata():
        if identry.get()==''or nameentry.get()==''or emailentry.get()==''or addressentry.get()==''or \
                bodentry.get()=='' or genderentry.get()==''or phoneentry=='':

            messagebox.showerror('Error','All Fields are Required',parent=addroot)

        else:
            addeddate=time.strftime('%d/%m/%Y')

            addedtime=time.strftime('%H:%M:%S')


            try:
                strr='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycurser.execute(strr,(identry.get(),nameentry.get(),phoneentry.get(),emailentry.get(),addressentry.get(),genderentry.get(),bodentry.get(),addeddate,addedtime))

                con.commit()

                res=messagebox.askyesno('Question',f'Id{identry.get()} Added Suessfully.'
                            f'Do you want to clear form?',parent=addroot)

                if res==True:
                     identry.delete(0,END)
                     nameentry.delete(0,END)
                     addressentry.delete(0,END)
                     bodentry.delete(0,END)
                     genderentry.delete(0,END)
                     phoneentry.delete(0,END)
                     bodentry.delete(0,END)
                     emailentry.delete(0,END)



            except:
                messagebox.showerror('error','Id alredy exit')

            strr='select * from student'

            mycurser.execute(strr)

            fetched_data=mycurser.fetchall()#it stores data in tuple format
            studentTable.delete(*studentTable.get_children())
            for i in fetched_data:
                    listdata=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]#########3onverting to list
                    studentTable.insert('',END,values=listdata)



    addroot=Toplevel()
    addroot.grab_set()
    addroot.geometry('470x520+130+130')
    addroot.title('Add Student')
    addroot.resizable(0,0)

    idlable=Label(addroot,text='Id',font=('times new roman',20) ,fg='red4')
    idlable.grid(pady=15,padx=25,sticky=W)

    namelable=Label(addroot,text='Name',font=('times new roman',20) ,fg='red4')
    namelable.grid(row=1,pady=15,padx=25,sticky=W)

    phonelable=Label(addroot,text='Phone No',font=('times new roman',20) ,fg='red4')
    phonelable.grid(row=2,pady=15,padx=25,sticky=W)

    emaillable=Label(addroot,text='Email',font=('times new roman',20) ,fg='red4')
    emaillable.grid(row=3,pady=15,padx=25,sticky=W)

    addresslable=Label(addroot,text='Address',font=('times new roman',20) ,fg='red4')
    addresslable.grid(row=4,pady=15,padx=25,sticky=W)

    genderlable=Label(addroot,text='Gender',font=('times new roman',20) ,fg='red4')
    genderlable.grid(row=5,pady=15,padx=25,sticky=W)

    bodlable=Label(addroot,text='B.O.D',font=('times new roman',20) ,fg='red4')
    bodlable.grid(row=6,pady=15,padx=25,sticky=W)

    identry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, width=24)
    identry.grid(row=0,column=1)

    nameentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, width=24)
    nameentry.grid(row=1,column=1)
    phoneentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, width=24)
    phoneentry.grid(row=2,column=1)
    emailentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, width=24)
    emailentry.grid(row=3,column=1)
    addressentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, width=24)
    addressentry.grid(row=4,column=1)
    genderentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, width=24)
    genderentry.grid(row=5,column=1)
    bodentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, width=24)
    bodentry.grid(row=6,column=1)

    submitbutton=Button(addroot,text="SUBMIT",command=adddata)
    submitbutton.grid(row=7,column=1,pady=5,padx=10)















def connetDB():

    def connect():
        global mycurser, con

        try:
            con=pymysql.connect(host='localhost',user='root',password='rutu@1997')
            mycurser=con.cursor()

        except:
            messagebox.showerror('Error','Invalid Details',parent=root1)
            return

        try:
            strr='create database studentdata5'
            mycurser.execute(strr)

            strr='use studentdata5'
            mycurser.execute(strr)

            strr='create table student(id int,name varchar(30),mobile varchar(10),email varchar(30),address varchar(100),gender varchar(10),dob varchar(50),date varchar(50),time varchar(50))'

            mycurser.execute(strr)
            strr='alter table student modify column id int not null'
            mycurser.execute(strr)
            strr='alter table student modify column id int primary key'
            mycurser.execute(strr)

            messagebox.showinfo('Informtion','You are conneted to database',parent=root1)
        except:
             strr='use studentdata5'
             mycurser.execute(strr)


             messagebox.showinfo('Informtion', 'You are conneted to database', parent=root1)
             addBtn.config(state=NORMAL)
             showBtn.config(state=NORMAL)
             updateBtn.config(state=NORMAL)
             exportBtn.config(state=NORMAL)
             searchBtn.config(state=NORMAL)
             deleteBtn.config(state=NORMAL)




        root1.destroy()

    root1=Toplevel()
    root1.geometry('470x250+730+230')
    root1.title('Database connetion')
    root1.resizable(0,0)

    hostnamelable=Label(root1,text='Host Name:',font=('arial',20,'bold'),fg='red4')
    hostnamelable.place(x=10,y=10)
    usernamelable=Label(root1,text='User Name:',font=('arial',20,'bold'),fg='red4')
    usernamelable.place(x=10,y=70)
    passwordlable=Label(root1,text='Password:',font=('arial',20,'bold'),fg='red4')
    passwordlable.place(x=10,y=130)

    hostentry=Entry(root1,font=('roman',15,'bold'),bd=2)
    hostentry.place(x=250,y=10)
    userentry=Entry(root1,font=('roman',15,'bold'),bd=2)
    userentry.place(x=250,y=70)
    passwordentry=Entry(root1,font=('roman',15,'bold'),bd=2)
    passwordentry.place(x=250,y=130)

    connectbtn=ttk.Button(root1,text='connect',width=15,command=connect)
    connectbtn.place(x=250,y=190)





def clock():
    date = time.strftime("%H:%M:%S")
    currenttime= time.strftime("%d/%m/%Y")
            # print(time_string,date_string)
    clocklable.config(text=f'  Date : { date}\nTime :  {currenttime} ')


def slider():
    global count,text

    if count>=len(s):
        count=0
        text=''
        sliderLabel.config(text=text)

    else:
        text=text+s[count]
        sliderLabel.config(text=text)
        count+=1
    sliderLabel.after(300,slider)







root=ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')
root.geometry('1174x700+100+10')
root.title('Student Managment System')
root.resizable(0,0)
root.iconbitmap('icon.ico')

leftframe=Frame(root,bg='whitesmoke')
leftframe.place(x=10,y=80,width=500,height=600,)
frontlabel = Label(leftframe, text='.........WELCOME.........', width=30, font=('arial', 22, 'bold'),
                   bg='whitesmoke',fg='red4')
frontlabel.grid(row=0,column=0,pady=20)

addBtn = ttk.Button(leftframe, text='1. Add Student', width=25,state=DISABLED ,command=addstd)
addBtn.grid(row=1,column=0,pady=20)

searchBtn = ttk.Button(leftframe, text='2. Search Student', width=25,state=DISABLED,command=searstd )
searchBtn.grid(row=2,column=0,pady=20)

deleteBtn = ttk.Button(leftframe, text='3. Delete Student', width=25,state=DISABLED,command=delete )
deleteBtn.grid(row=3,column=0,pady=20)

updateBtn = ttk.Button(leftframe, text='4. Update Student', width=25,state=DISABLED,command=updatestd )
updateBtn.grid(row=4,column=0,pady=20)

showBtn = ttk.Button(leftframe, text='5. Show All', width=25,state=DISABLED,command=showstd)
showBtn.grid(row=5,column=0,pady=20)

exportBtn = ttk.Button(leftframe, text='6. Export Data', width=25,state=DISABLED,command=export)
exportBtn.grid(row=6,column=0,pady=20)

exitBtn = ttk.Button(leftframe, text='7. Exit', width=25,command=iexit )
exitBtn.grid(row=7,column=0,pady=20)

clocklable= Label(root, font=("times", 14, 'bold'), bg='whitesmoke')
clocklable.place(x=0, y=0)
clock()

databasebtn = ttk.Button(root, text="Connect to Database", width=18, command=connetDB)
databasebtn.place(x=975, y=0)

s='STUDENT MANAGMENT SYSTEM'
count=0
text=''

sliderLabel = Label(root, text=s, font=("arial", 30, 'italic bold'), relief=RIDGE, borderwidth=4,fg='red4',
                    bg='whitesmoke', width=30)
sliderLabel.place(x=200, y=0)
slider()

rightframe=Frame(root,bg='whitesmoke')
rightframe.place(x=550,y=80,width=620,height=600,)

style=ttk.Style()
style.configure('Treeview.Heading', font=('casteller', 20, 'bold'), foreground='red4')
style.configure('Treeview', font=('times new roman', 15, 'bold'), foreground='black', bakground='red4')

scroll_x = Scrollbar(rightframe, orient=HORIZONTAL)
scroll_y = Scrollbar(rightframe, orient=VERTICAL)

studentTable = Treeview(rightframe, columns=(
    'Id', 'Name', 'Mobile No', 'Email', 'Address', 'Gender', 'D.O.B', 'Added Date', 'Added Time'),
                        yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
studentTable.pack(fill=BOTH,expand=1)

scroll_x.config(command=studentTable.xview)
scroll_y.config(command=studentTable.yview)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.pack(side=BOTTOM, fill=X)



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
studentTable.column('Email', width=200)

studentTable.column('Address', width=300)
studentTable.column('Gender', width=100)
studentTable.column('D.O.B', width=150)
studentTable.column('Added Date', width=200)
studentTable.column('Added Time', width=200)

root.mainloop()