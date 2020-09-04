import tkinter as tk
from tkinter import *
import webbrowser

#create window
app = Tk()

#classlink
app.title('Classlink')

#links(functions)

def ds_as():
    webbrowser.open('https://meet.google.com/ktk-uitn-tow')

def dslab_as():
    webbrowser.open('https://meet.google.com/ktk-uitn-tow')

def mp_gk():
    webbrowser.open('https://meet.google.com/fok-pphe-pon')

def oopllab_sa():
    webbrowser.open('https://meet.google.com/ibd-reza-rxd')

def oopllab_as():
    webbrowser.open('https://meet.google.com/ksz-adin-vxp')

def oopl_as():
    webbrowser.open('https://meet.google.com/ksz-adin-vxp')

def math_yg():
    webbrowser.open('https://meet.google.com/owv-svay-szh')

def math_drp():
    webbrowser.open('https://meet.google.com/hhe-qqvo-dzc')

def math_drp1():
    webbrowser.open('https://meet.google.com/eoz-kcso-ofo')


def stat_bpss():
    webbrowser.open('https://meet.google.com/jwc-fudc-vis')

def mp_gk1():
    webbrowser.open('https://meet.google.com/pyg-hzmk-ube')

def project_as():
    webbrowser.open('https://meet.google.com/bdi-vffg-yrf')
def mplab_gk():
    webbrowser.open('https://meet.google.com/htx-uzpq-kdf')


#time
time_a = Label(app,text='6:40-7:30',width=20,relief='raised')
time_a.grid(row=0,column=0,sticky=W)

time_b = Label(app,text='7:30-8:20',width=20,relief='raised')
time_b.grid(row=0,column=1,sticky=W)

time_c = Label(app,text='8:20-9:10',width=20,relief='raised')
time_c.grid(row=0,column=2,sticky=W)

time_d = Label(app,text='9:40-10:30',width=20,relief='raised')
time_d.grid(row=0,column=3,sticky=W)

time_e = Label(app,text='10:30-11:20',width=20,relief='raised')
time_e.grid(row=0,column=4,sticky=W)

time_f = Label(app,text='11:20-12:30',width=20,relief='raised')
time_f.grid(row=0,column=5,sticky=E)

time_ab = Label(app,text='6:40-7:30',width=20,relief='raised')
time_ab.grid(row=5,column=0,sticky=W)

time_bb = Label(app,text='7:30-8:20',width=20,relief='raised')
time_bb.grid(row=5,column=1,sticky=W)

time_cb = Label(app,text='8:20-10:00',width=20,relief='raised')
time_cb.grid(row=5,column=2,sticky=W)

time_db = Label(app,text='10:30-11:20',width=20,relief='raised')
time_db.grid(row=5,column=3,sticky=W)

time_eb = Label(app,text='11:20-12:30',width=20,relief='raised')
time_eb.grid(row=5,column=4,sticky=W)

#time_fb = Label(app,text='11:20-12:10',width=20,relief='raised')
#time_fb.grid(row=5,column=5,sticky=E)






#subject

#monday
subject_1 = Button(app,text='DS/AS',width=40,command=ds_as)
subject_1.grid(row=1,column=0,sticky=W,columnspan=2)

subject_2 = Button(app,text='OOPL LAB/SA',width=20,command=oopllab_sa)
subject_2.grid(row=1,column=2)

subject_3 = Button(app,text='MP/GK',width=40,command=mp_gk)
subject_3.grid(row=1,column=3,columnspan=2,sticky=W)

subject_4 = Button(app,text='Maths II/YG',width=20,command=math_yg)
subject_4.grid(row=1,column=5)

#tuesday
subject_11 = Button(app,text='STAT/BP/SS',width=40,command=stat_bpss)
subject_11.grid(row=2,column=0,sticky=W,columnspan=2)

subject_21 = Button(app,text='PROJECT/AS',width=20,command=project_as)
subject_21.grid(row=2,column=2)

subject_31 = Button(app,text='MP/GK',width=20,command=mp_gk1)
subject_31.grid(row=2,column=3,sticky=W)

subject_41 = Button(app,text='OOPL/AS',width=40,command=oopl_as)
subject_41.grid(row=2,column=4,columnspan=2,sticky=W)


#wednesday
subject_12 = Button(app,text='DS/AS',width=40,command=ds_as)
subject_12.grid(row=3,column=0,sticky=W,columnspan=2)

subject_22 = Button(app,text='OOPL LAB/SA',width=20,command=oopllab_sa)
subject_22.grid(row=3,column=2)

subject_32 = Button(app,text='MP/GK',width=40,command=mp_gk)
subject_32.grid(row=3,column=3,columnspan=2,sticky=W)

#thrusday
subject_13 = Button(app,text='STAT/BP/SS',width=40,command=stat_bpss)
subject_13.grid(row=4,column=0,sticky=W,columnspan=2)

subject_23 = Button(app,text='PROJECT/AS',width=20,command=project_as)
subject_23.grid(row=4,column=2)

subject_33 = Button(app,text='MP/GK',width=20,command=mp_gk1)
subject_33.grid(row=4,column=3,sticky=W)

subject_43 = Button(app,text='OOPL/AS',width=20,command=oopl_as)
subject_43.grid(row=4,column=4,sticky=W)

subject_53 = Button(app,text='OOPL LAB/AS',width=20,command=oopllab_as)
subject_53.grid(row=4,column=5,sticky=W)

#friday
subject_14 = Button(app,text='STAT/BP/SS',width=40,command=stat_bpss)
subject_14.grid(row=6,column=0,sticky=W,columnspan=2)

subject_24 = Button(app,text='MATHS II/DRP',width=20,command=math_drp)
subject_24.grid(row=6,column=2)

subject_34 = Button(app,text='MATHS II/YG',width=40,command=math_yg)
subject_34.grid(row=6,column=3,columnspan=2,sticky=W)


#SATURDAY
subject_15 = Button(app,text='DS LAB/AS ',width=40,command=dslab_as)
subject_15.grid(row=7,column=0,sticky=W,columnspan=2)

subject_25 = Button(app,text='MATHS II/DRP',width=20,command=math_drp1)
subject_25.grid(row=7,column=2)

subject_35 = Button(app,text='MP LAB /GK ',width=20,command=mplab_gk)
subject_35.grid(row=7,column=3,sticky=W)

subject_45 = Button(app,text='MATHS II /YG ',width=20,command=math_yg)
subject_45.grid(row=7,column=4,sticky=W)


#frame
app.geometry('1000x400')
#frame = tk.Frame(app,bg="black")
#frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

#icon
app.iconbitmap('C:/Users/LENOVO/Desktop/classlink/logo.ico')

#mainloop
app.mainloop()



