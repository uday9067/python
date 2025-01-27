import queue

q=queue.LifoQueue() #its like a stack

number=[10,20,30,40,50,60]

for i in number:
    q.put(i)
print(q.get())
print(q.get())
print(q.get())
print(q.get())