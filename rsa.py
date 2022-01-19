import math
import random
from tkinter import E

# mật mã mã hoá mật khẩu rsa
class rsa:
    def __init__(self):
        self.p = 0
        self.q = 0
        self. n = 0
        self.euler =0
        self.e = 0
        self.d = 0
        self.m = ""

    #encryto with no key public
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
        return self.m,self.e,self.n
    
    #encryto with key public
    @staticmethod
    def encryto_withE(private_pass,e,n):
        m =""
        for i in private_pass:
            t = pow(ord(i),e,n)
            m += str(t); 
        return m

    #check_pass with psw
    @staticmethod
    def isTrue(psw1,psw2,keyPublic,n):
        psw_en = rsa.encryto_withE(psw1,keyPublic,n)
        return psw_en == psw2

#find modulo e
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

def writeFileKey(namefile, data):
    file1 = open(namefile, "w")
    file1.writelines(data)
    file1.close()

def readFileKey(namefile):
    file1 = open(namefile, "r")
    d = file1.readlines()
    return d

#delete when run first time
def main():
    c_rs = rsa()
    psw ="1234"
    pswp ="8541"
    psw = "1458"
    psw_c,e,n = c_rs.encryto(psw)
    psw_p = c_rs.encryto_withE(pswp,e,c_rs.n)
    psw_m = c_rs.encryto_withE(pswp,e,c_rs.n)
    a = rsa.encryto_withE(psw,e,n)
    b = rsa.encryto_withE(pswp,e,n)
    print(a)
    print(b)
    print(psw_c)
    print(psw_p)
    L = []
    L.append(str(n) + "\n")
    L.append(str(e) + "\n")
    L.append(psw_c + '\n')
    L.append(psw_p + '\n')
    L.append(psw_m + '\n')
    writeFileKey("key.txt",L)

main()


