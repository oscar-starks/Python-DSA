# Python3 program for demonstrating
# closing a coroutine

def print_name(prefix):
	print("Searching prefix:{}".format(prefix))
	try :
		while True:
				name = (yield)
				if prefix in name:
					print(name)
	except GeneratorExit:
		print("Coutine closed!!")

corou = print_name("Dear")
corou.__next__()
corou.send("Atul")
corou.send("Dear Atul")
corou.close()


def my_coroutine(key):
    print(f"Recieved {key}")
    try :
        while True:
            value = (yield)
            if key in value:
                print("Oh jes!")
            else:
                print("Nope!")
    except GeneratorExit:
        print("Session Closed!")
        
coroutine = my_coroutine("Hello")
coroutine.__next__()
coroutine.send("Atul")
coroutine.send("Hello Atul")
coroutine.send("Hello Damsel")
coroutine.close()