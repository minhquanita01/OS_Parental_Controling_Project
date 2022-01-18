#from _typeshed import Self
import math
from os import times
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

class Time:
    def __init__(self):
        self._hour = 0
        self._minute = 0

class Using_Time:
    def __init__(self,f,t,d,i,s):
        self._from = f
        self._to = t
        self._duration = d
        self._interrupt = i
        self._sum = s

def data_split(data:str):
    from_ = ""
    to_ = ""
    duration_ = 0
    interrupt_ = 0
    sum_ = 0
    d = data.split()
    for s in d:
        if(s[0] == 'F'): from_ = str(s[1:])
        elif(s[0] == 'T'): to_ = s[1:]
        elif(s[0] == 'D'): duration_ = int(s[1:])
        elif(s[0] == 'I'): interrupt_ = int(s[1:])
        elif(s[0] == 'S'): sum_ = int(s[1:])
    return from_, to_, duration_,interrupt_, sum_

def main():

    parent_pass = "taolabomay"
    p_rs = rsa()
    p_rs.encryto(parent_pass)

    children_pass = "123456"
    c_rs = rsa()
    c_rs.encryto(children_pass)

    time_process = []
    with open("time.txt", encoding = 'utf-8') as f:
        for s_line in f:
            f,t,d,i,s = data_split(s_line)           
            ti = Using_Time(f,t,d,i,s)
            time_process.append(ti)

    pass_input = input("Nhap mat khau: ")

    if (p_rs.isTrue(pass_input)):
        print("Dung mat khau phu huynh")
    else:
        if (c_rs.isTrue(pass_input)):
            print("Dung mat khau con tre")
        else:
            print("Sai mat khau")