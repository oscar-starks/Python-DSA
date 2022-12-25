import threading
num = 0

def increment():
    global num
    num += 1
    
def operation():
    for _ in range(10000000):
        increment()
        
t1 = threading.Thread(target=operation, name = 'operation1')
t2 = threading.Thread(target=operation, name = 'operation2')

t1.start()
t2.start()

t1.join()
t2.join()