from datetime import time 
from datetime import datetime
import math
def subtractTimeString(s1,s2):
    FMT = '%H:%M'
    return (datetime.strptime(s1, FMT) - datetime.strptime(s2, FMT)).total_seconds()/60

def getTimeNow():
    FMT = '%H:%M'
    current_time = datetime.now()
    crt = current_time.strftime(FMT)
    return crt

class Using_Time:
    def __init__(self,f,t,d = math.inf,i = 0, s = math.inf):
        self._from = f
        self._to = t
        self._duration = d
        self._interrupt = i
        self._sum = s
        self._FMT = '%H:%M'
        self._time_start = ""

    def isTimeUsing(self):
        crt = getTimeNow()
        if crt >= self._from and crt <= self._to :
            return True
        return False

    def setNow_isUsing(self):
        crt = getTimeNow()
        self._time_start = crt

    def countTimeUsing(self):
        crt = getTimeNow()
        return subtractTimeString(crt,self._time_start)

    # function for debug
    def countTimeUsing2(self,time):
        crt = getTimeNow()
        return subtractTimeString(crt,time)

    def isEnd_UsingTime(self):
        if self.isTimeUsing():
            if int(self.countTimeUsing()) >= self._sum :
                return True
            return False
        return True

    def getDuration(self):
        return self._duration
    
    def getTimeSleep(self):
        return self._interrupt

    def getSum(self):
        return self._sum

a = Using_Time("06:00","06:45")
a.setNow_isUsing()
c = a.countTimeUsing()
print(c)