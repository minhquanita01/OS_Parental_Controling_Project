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
        if(s[0] == 'F'): from_ = s[1:]
        elif(s[0] == 'T'): to_ = s[1:]
        elif(s[0] == 'D'): duration_ = int(s[1:])
        elif(s[0] == 'I'): interrupt_ = int(s[1:])
        elif(s[0] == 'S'): sum_ = int(s[1:])
    return from_, to_, duration_,interrupt_, sum_

def main():
    # parent_pass = "taolabomay"
    # p_rs = rsa.rsa()
    # p_rs.encryto(parent_pass)

    # children_pass = "123456"
    # c_rs = rsa.rsa()
    # c_rs.encryto(children_pass)
    # pass_input = input("Nhap mat khau: ")

    # if (p_rs.isTrue(pass_input)):
    #     print("Dung mat khau phu huynh")
    # else:
    #     if (c_rs.isTrue(pass_input)):
    #         print("Dung mat khau con tre")
    #     else:
            # print("Sai mat khau")
    
    time_process:us.Using_Time = []
    with open("time.txt", encoding = 'utf-8') as f:
        for s_line in f:
            f,t,d,i,s = data_split(s_line)           
            ti = us.Using_Time(f,t,d,i,s)
            time_process.append(ti)

    if time_process[0].isTimeUsing() : print("oke")
    

main()
