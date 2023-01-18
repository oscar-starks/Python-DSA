my_list = [2,3,4,5,6,7,7,8,89,91,1]
list_2 = []

while len(my_list) >= 2:
    list_2.append(str(my_list[-2]) + "," + str(my_list[-1]))
    del my_list[-2]
    del my_list[-1]  

if len(my_list) == 1:
    list_2.append(str(my_list[-1]))
    del my_list[-1]
    

print(list_2)
            