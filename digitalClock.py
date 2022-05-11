
from datetime import *
from tkinter import *

# print(datetime.now())
def date_time():
    time = datetime.now()
    sec = time.strftime('%S')
    min = time.strftime('%M')
    hr = time.strftime('%I')
    am = time.strftime('%p')
    
    lab_sec.config(text=sec)
    lab_min.config(text=min)
    lab_hr.config(text=hr)
    lab_am.config(text=am)
    lab_hr.after(200,date_time)
   
    
    # pm = time.strftime('%p')
    


root = Tk()

root.title("Digital-Clock")
root.geometry("500x500")
root.config(bg='#bdbfdb')
# f1 = Frame(root)
# f1.pack()
# hour
lab_hr = Label(root,text="00",font=('Time New Roman',20,"bold"),bg='black',fg='white')
lab_hr.place(x=40,y=40,height=65,width=50)

# minute
lab_min = Label(root,text="00",font=('Time New Roman',20,"bold"),bg='black',fg='white')
lab_min.place(x=140,y=40,height=65,width=50)

# sec
lab_sec = Label(root,text="00",font=('Time New Roman',20,"bold"),bg='black',fg='white')
lab_sec.place(x=240,y=40,height=65,width=50)

# AM/PM
lab_am = Label(root,text="AM",font=('Time New Roman',25,"bold"),bg='black',fg='white')
lab_am.place(x=340,y=40,height=65,width=100)

l4 = Label(root,text="hr",font=('Time New Roman',20,"bold"),bg='black',fg='white')
l4.place(x=40,y=120,height=35,width=50)

l5 = Label(root,text="min",font=('Time New Roman',20,"bold"),bg='black',fg='white')
l5.place(x=140,y=120,height=35,width=50)

l6 = Label(root,text="sec",font=('Time New Roman',20,"bold"),bg='black',fg='white')
l6.place(x=240,y=120,height=35,width=50)

l7 = Label(root,text="am/pm",font=('Time New Roman',20,"bold"),bg='black',fg='white')
l7.place(x=340,y=120,height=35,width=100)
# l1.pack(x=40,y=40,height=110,width=100)





date_time()
root.mainloop()