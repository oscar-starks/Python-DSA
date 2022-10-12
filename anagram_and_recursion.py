# my_symbols = ['~','`','!' ,'@','#','$','%','^','&','*','(',')','_','-','+','=',
#             '{','[','}',']','|','\\',':',';','"',"'","<",",",">",".","?","/",]

# this is a password checker to ensure a user's password contains a certain set of symbols and numbers

# my_input = input("Input a string of your choice: \n")
# count = 0
# acount = 0
# for i in my_input:
#     for mine in my_symbols:
#         if i == mine:
#             count += 1
# for i in my_input:
#     if i.isalpha():
#         if i.isupper():
#             acount += 1
# print(count, "-----------", acount)

# this is how to generate an anagram for a string
# ana = sorted("goat")
# fin = ""
# for i in ana:
#     fin += i
# print(fin)

def recursion(x):
    if type(x) is not int:
      raise TypeError("Only integers are allowed")
    if x >= 1:
        result = x * recursion(x-1)
        print(result)
    else:
        result = 1
    return result
    
def recursion(x):
    if x >= 1:
        result = x * recursion(x-1)
        print(result)
    else:
        result = 1
    return result

def mutability(mystring = "race bear thing care keen trap tweet earth knee heart neek tewt"):
    """ 
        this function takes a string as an argument and returns a dictionary with the individual strings
        as keys and the anagrams of the keys in lists as values
    """
    from itertools import permutations
    mydict = {}
    string_list = mystring.split()
    for val in string_list:
        var = permutations(val)
        list_of_var = list(var)

        my_list = []
        for i in list_of_var:
            char = ""
            for mychar in i:
                char += mychar
            my_list.append(char)
        mydict[val] = my_list
        
    for i in mydict:
        mydict[i].remove(i)

    return mydict

print(mutability())