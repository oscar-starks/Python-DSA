from threading import Thread, current_thread
import time

def calcsqr(num : int) -> int:
    for i in num:
        time.sleep(0.2)
        print(current_thread().getName())
        print(f"the square of {i} is {i**2}\n")
        
def calccube(num : int) -> int:
    for i in num:
        time.sleep(0.2)
        print(current_thread().getName())
        print(f"the cube of {i} is {i**3}\n")
        
def daemon() -> None:
    while True:
        time.sleep(0.2)
        print("this is a daemon thread!")

nums = [3,4,6,7]
time1 = time.time()        
f1 = Thread(target=calcsqr, name = "1st thread", args=(nums,))
f2 = Thread(target=calccube, name = "2nd thread", args=(nums,))
f3 = Thread(target=daemon, name = "3rd thread", daemon= True)

f1.start()
f2.start()
f3.start()

# f1.join()
# f2.join()
# f3.join()
print("total time taken", time.time() - time1)

# The command "Tasklist" can be used on our cmd to list out the number of cpu processes that are active on our computer