
def anagram_check(mystring = "race bear thing care keen trap tweet earth knee heart neek tewt"):
    my_list = mystring.split()
    my_dict = {}

    def checker(inp):
        for val in my_dict.keys():
            if sorted(inp) == sorted(val):
                return True
            
    for keys in my_list:
        if keys in my_dict.keys():
            pass
        elif checker(keys):
            pass
        else:
            my_dict[keys] = []
        
        if keys in my_dict.keys():
            for val in my_list:
                if sorted(val) == sorted(keys) and val not in my_dict.keys() and val != keys:
                    my_dict[keys].append(val)
    return my_dict

print(anagram_check())
        
