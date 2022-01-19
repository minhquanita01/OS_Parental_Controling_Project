from os import times
from datetime import datetime
from datetime import time
import Using_Time as us
import rsa
def data_split(data:str):
    from_ = ""
    to_ = ""
    duration_ = 0
    interrupt_ = 0
    sum_ = 0
    d = data.split()
    for s in d:
        if(s[0] == 'F'): from_ = s[1:] # string "06:00"
        elif(s[0] == 'T'): to_ = s[1:] # string "06:00"
        elif(s[0] == 'D'): duration_ = int(s[1:])
        elif(s[0] == 'I'): interrupt_ = int(s[1:])
        elif(s[0] == 'S'): sum_ = int(s[1:])
    return from_, to_, duration_,interrupt_, sum_

def read_file(file_name):
    time_list = []
    with open(file_name, encoding = 'utf-8') as f:
        for s_line in f:
            f,t,d,i,s = data_split(s_line)           
            ti = us.Using_Time(f,t,d,i,s)
            time_list.append(ti)
    return time_list

def main():
    data = rsa.readFileKey("key.txt")
    print(data)
    print(int(data[0]))
    keypulic = int(data[0])
    n = int(data[1])
    psw_c = int(data[2])
    psw_p = int(data[3])

    print("input password : ")
    psw = input()
    psw_en = rsa.rsa.encryto_withE(psw_e)
    if ():
        print("Dung mat khau phu huynh")
    else:
        if (c_rs.isTrue(pass_input)):
            print("Dung mat khau con tre")
        else:
            print("Sai mat khau")

    print("input password : ")
    psw = input()
    
    pass

main()
