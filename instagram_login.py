from tkinter import*
insta=Tk()
insta.title('instagram login')

insta.geometry('400x400')
insta.configure(background='white')

def login():
    username = e1.get()
    password = e2.get()
def on_enter(e):
    e1.delete(0,'end')
def on_leave(e):
    n=e1.get()
    if n=='':
        e1.insert(0,"Phone number, username, email")
def on_enter(e):
    e2.delete(0,'end')
def on_leave(e):
    n1=e2.get()
    if n1=='':
        e2.insert(0,"password")

inst_frame=Frame(insta,width=800,height=900,bg='snow')
inst_frame.pack(pady=20)

lab1=Label(inst_frame,text='Instagram',font=('Helvetica',25),bg='white')
lab1.pack(pady=25)

e1=Entry(inst_frame,fg='black',width=25,font=('Helvetica',16))
e1.pack(pady=25)
e1.insert(0,'Phone number, username, email')
e1.bind('<FocusIn>',on_enter)
e1.bind('<FocusOut>',on_leave)

e2=Entry(inst_frame,fg='black',width=25,font=('Helvetica',16))
e2.pack(pady=0)
e2.insert(0,'Password')
e2.bind('<FocusIn>',on_enter)
e2.bind('<FocusOut>',on_leave)

login_button = Button(inst_frame, text="Log In", font=("Helvetica",10),fg='white',width=38, background='blue', command=login)
login_button.pack(pady=26)

lab2=Label(inst_frame,text=('Log in with Facebook'),fg='blue')
lab2.pack(pady=5)

forgot_password = Label(inst_frame, text="Forgot password?", fg="blue", cursor="hand2")
forgot_password.pack(pady=7)

sign_up =Label(inst_frame, text="Don't have an account? Sign up", fg="blue", cursor="hand2")
sign_up.pack(pady=5)


insta.mainloop()