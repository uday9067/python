import threading
import time 

x=1
lock = threading.Lock()

def Double():
    global x,lock
    lock.acquire()
    while(x<1024):
        x=x*2
        print(x)
        time.sleep(1)
    print("reached the maximum")
    lock.release()

def half():
    global x,lock
    lock.acquire()
    while(x>1):
        x=x/2
        print(x)
        time.sleep(1)
    print("minimum value riched")
    lock.release()

t1= threading.Thread(target=Double)
t2=threading.Thread(target=half)

t1.start()
t2.start()
