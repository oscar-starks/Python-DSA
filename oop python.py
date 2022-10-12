class animal():
    # def __init__(self):
    #     self.goat = 5

    def breathe(self):
        print("I breathe loudly")

    def move(self):
        print("I move like I don't care")

class goat(animal):
    def __init__(self):
        super(). __init__()
        
        

ani = goat()
ani.breathe()
# ani.move()