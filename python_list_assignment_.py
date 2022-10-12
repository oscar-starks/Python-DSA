
lists = []
username = str(input("Hello there, please provide a name: \n"))
# this prompts the user to provide his name

print("Thanks " + username.capitalize() + " for providing your name")

counter = eval(input("Input the number of items you want in your list: "))
print("Now input your values accordingly(NB: Must be integers between 1-12) \n ")
# this prompts the user to choose the number of items he/she wants in the list

for i in range(counter):
    user_input = eval(input(f"Value {i + 1}: \n"))
    lists.append(user_input)
# this appends every user input to the end of the lists

for I in lists:
    if I > 10:
     lists[(lists.index(I))] = 10
#this checks if the individual values are greater than 10 and then equates them to 10

    

print(f"Dear {username.capitalize()}, here's yor final list: ")
print(lists)
# this prints the final list
