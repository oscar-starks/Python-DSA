def decorator(function):
    def inner(*args):
        print("hello")
        returned_val = function(*args)
        return returned_val
    
    return inner

@decorator
def sum(a, b):
    return a+b

print(sum(2,4))
# print(sum("min"))

# def myFun(arg1, arg2, arg3):
#     print("arg1:", arg1)
#     print("arg2:", arg2)
#     print("arg3:", arg3)
 
 
# # Now we can use *args or **kwargs to
# # pass arguments to this function :
# args = ("Geeks", "for", "Geeks")
# myFun(*args)
 
# kwargs = { "arg2": "for", "arg1": "Geeks", "arg3": "Geeks"}
# myFun(**kwargs)