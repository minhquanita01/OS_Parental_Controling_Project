from functools import partial
import time
from tkinter import *
from tkinter import messagebox
import Using_Time as us
import Children as ch
import rsa
import math
import random
import os
from os import times

child = False
parent = False
more = False


def validate_password(password_field):

    input = str(password_field.get())
    
    if (len(input) == 0):
        messagebox.showwarning("Thông báo", "Chưa nhập mật khẩu")
        return

    data = rsa.readFileKey("key.txt")
    keypulic = int(data[1])
    n = int(data[0])
    psw_c = int(data[2])
    psw_p = int(data[3])
    psw_m = int(data[4])

    psw_en = int(rsa.rsa.encryto_withE(input,keypulic,n))

    if (psw_en == psw_p):
        parent = True
        messagebox.showinfo("Thông báo", "Nhập đúng mật khẩu phụ huynh")
    elif (psw_en == psw_c):
        child = True
        messagebox.showinfo("Thông báo", "Nhập đúng mật khẩu con trẻ")
    elif (psw_en == psw_m):
        more = False
        messagebox.showinfo("Thông báo", "Nhập đúng mật khẩu thêm thời gian")    
    else:
        messagebox.showerror("Thông báo", "Nhập sai mật khẩu")

def shutdown():
    if (messagebox.askyesno("Thông báo", "Bạn thật sự muốn tắt máy?")):
        os.system("shutdown -s -t 300")
def forceShutDown():
    os.system("shutdown -s -t 300")
root = Tk()
root.title("Đăng nhập hệ thống")
root.eval("tk::PlaceWindow . center")
root.resizable(0,0)

Input_Label = Label(root, text = "Nhập mật khẩu")
Input_Label.pack()

password = StringVar()
passwordEntry = Entry(root, textvariable=password, width=50, show='*')
passwordEntry.pack()

validate = partial(validate_password, passwordEntry)

Submit_Button = Button(root, text="OK", width=12, command=validate)
Submit_Button.pack()

Shutdown_Button = Button(root, text="Tắt máy", width=12, command=shutdown)
Shutdown_Button.pack()


root.mainloop()

def parentTime(timeList):
    if not parent : return
    root.destroy()
    for t in timeList:
        if int(t.countTimeUsing()) == 1:
            # nhập lại mật khẩu
            root2 = Tk()

            root2.title("Đăng nhập lại hệ thống")
            root2.eval("tk::PlaceWindow . center")
            root2.resizable(0,0)

            Input_Label2 = Label(root, text = "Nhập mật khẩu")
            Input_Label2.pack()

            password2 = StringVar()
            passwordEntry2 = Entry(root, textvariable=password2, width=60, show='*')
            passwordEntry2.pack()

            validate2 = partial(validate_password, passwordEntry2)

            Submit_Button2 = Button(root, text="OK", width=12, command=validate)
            Submit_Button2.pack()

            root2.mainloop()

            print("OK")

            pass

def childTime(timeList):
    if not child : return
    root.destroy()
    for t in timeList:
        if t.isTimeUsing() : 
            # tới thời gian duration
            if int(t.getDuration()) == int(t.countTimeUsing()):
                # deadlock for time sleep
                time.sleep(int(t.getTimeSleep())*60)

        if t.isEnd_UsingTime() :
            forceShutDown()


while(True):
    timeList = ch.read_file("time.txt")
    if child : childTime(timeList)
    while parent : parentTime(timeList)
    break

    



    
        


