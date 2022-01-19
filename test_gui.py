from functools import partial
from tkinter import *
from tkinter import messagebox
import rsa
import math
import random


def validate_password(password_field):
    data = rsa.readFileKey("key.txt")
    print(data)
    print(int(data[0]))
    keypulic = int(data[1])
    n = int(data[0])
    psw_c = int(data[2])
    psw_p = int(data[3])

    input = str(password_field.get())
    print(input)
    psw_en = int(rsa.rsa.encryto_withE(input,keypulic,n))
    print(psw_en)

    if (psw_en == psw_p):
        messagebox.showinfo("Thông báo", "Nhập đúng mật khẩu phụ huynh")
    elif (psw_en == psw_c):
        messagebox.showinfo("Thông báo", "Nhập đúng mật khẩu con trẻ")
    else:
        messagebox.showerror("Thông báo", "Nhập sai mật khẩu")


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


root.mainloop()