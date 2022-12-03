import threading
from threading import Thread

""" this is just a simple example of implementing threading using 
    inheritance
"""

class count(Thread):
    def __init__(self, name:str, num:int) -> None:
        super(count, self).__init__()
        self.num  = num
        self.name = name
        
    def start(self) -> None:
        num = self.num
        name = self.name
        print(num, name, threading.current_thread().name)

t1 = count("thread name", 5)

t1.start()