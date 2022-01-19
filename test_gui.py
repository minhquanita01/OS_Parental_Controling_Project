from functools import partial
import imp
from tkinter import *
from tkinter import messagebox
import rsa
import math
import random
import os

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

    psw_en = int(rsa.rsa.encryto_withE(input,keypulic,n))

    if (psw_en == psw_p):
        messagebox.showinfo("Thông báo", "Nhập đúng mật khẩu phụ huynh")
    elif (psw_en == psw_c):
        messagebox.showinfo("Thông báo", "Nhập đúng mật khẩu con trẻ")
    else:
        messagebox.showerror("Thông báo", "Nhập sai mật khẩu")

def shutdown():
    if (messagebox.askyesno("Thông báo", "Bạn thật sự muốn tắt máy?")):
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