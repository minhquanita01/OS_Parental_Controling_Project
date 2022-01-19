from functools import partial
from tkinter import *
from tkinter import messagebox
import math
import random

class rsa:
    def __init__(self):
        self.p = 0
        self.q = 0
        self. n = 0
        self.euler =0
        self.e = 0
        self.d = 0
        self.m = ""
    def encryto(self,pri_pass):
        self.p = genPrime(1000,10000)
        self.q = genPrime(1000,10000)
        while self.p == self.q:
            self.q = genPrime(1000,10000)
        self.n = self.p * self.q
        self.euler = (self.p -1)*(self.q - 1)
        self.e =  int(Arbitrary_Int_e(self.euler))
        self.d = int(extend_euclid(self.e,self.euler))
        self.m = self.encryto_withE(pri_pass,self.e,self.n)
        return self.m,self.e,self.d
    
    def encryto_withE(self,private_pass,e,n):
        m =""
        for i in private_pass:
            t = pow(ord(i),e,n)
            m += str(t); 
        return m

    #11.01.2001
    def isTrue(self,psw):
        psw_en = self.encryto_withE(psw,self.e,self.n)
        return psw_en == self.m
    
def Arbitrary_Int_e(phi):
    e = random.randint(1,phi)
    if(int(gcd(e, phi)) == 1):
        return e
    return Arbitrary_Int_e(phi)

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def genPrime(x, y):
    prime = not True
    while not prime:
        n = random.randint(x,y)
        isPrime = True
        for num in range(2, n//2):
            if n % num == 0:
                isPrime = False
        if isPrime:
            break
    return n

def extend_euclid(e, n) :
    xe = 1
    xn = 0
    tn = n

    while (n != 0) :
        q = (e - e % n) / n
        xr = xe - q * xn

        xe = xn
        xn = xr

        r = e % n
        e = n
        n = r

    if (xe < 0):
        xe += tn

    return xe

def validate_password(password_field, p0_rsa, p1_rsa):
    input = password_field.get()

    i_rsa = rsa()
    i_rsa.encryto(input)

    if (p0_rsa.isTrue(i_rsa)):
        messagebox.showinfo("Thông báo", "Nhập đúng mật khẩu phụ huynh")
    elif (p1_rsa.isTrue(i_rsa)):
        messagebox.showinfo("Thông báo", "Nhập đúng mật khẩu con trẻ")
    else:
        messagebox.showerror("Thông báo", "Nhập sai mật khẩu")


root = Tk()
root.title("Đăng nhập hệ thống")
root.eval("tk::PlaceWindow . center")
root.resizable(0,0)

Input_Label = Label(root, text = "Nhập mật khẩu")
Input_Label.pack()

password_parent = "12345"
p_rsa = rsa()
p_rsa.encryto(password_parent)

password_child = "1234"
c_rsa = rsa()
c_rsa.encryto(password_child)

password = StringVar()
passwordEntry = Entry(root, textvariable=password, width=50, show='*')
passwordEntry.pack()

validate = partial(validate_password, passwordEntry, p_rsa, c_rsa)

Submit_Button = Button(root, text="OK", width=12, command=validate)
Submit_Button.pack()


root.mainloop()