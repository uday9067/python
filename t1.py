import threading
def f1():
    for i in range(100):
        print("f1")
def f2():
    for i in range(100):
        print("f2")
t1 = threading.Thread(target=f1)
t2 = threading.Thread(target=f2)
t1.start()
t2.start()