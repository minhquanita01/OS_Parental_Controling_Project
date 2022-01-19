import math
import random

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
        return self.m,self.e,self.d
    
    #encryto with key public
    def encryto_withE(self,private_pass,e,n):
        m =""
        for i in private_pass:
            t = pow(ord(i),e,n)
            m += str(t); 
        return m

    #check_pass with psw
    def isTrue(self,psw):
        psw_en = self.encryto_withE(psw,self.e,self.n)
        return psw_en == self.m

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


def main():
    rs = rsa()
    psw = "aaaa"
    psw_en,e,d = rs.encryto(psw)
    print(psw_en)
    print(e)
    print(d)
    pass


