dicts = {}
# this declares an empty dictionary
item = ""
# this is used to store the names of the items in the dictionary
user_key = 0
# this is used to store the names of the items in the second dictionary

name = str(input("Hello there and welcome to this brief demonstration but before that, may I quickly know your name? ")).capitalize()
# this prompts the user to provide his/her name

print(f"Thank you {name} for providing your name!\n")
# this prints the name of the user back in response to the input provided

print("NB: While in this demo, if you want to terminate the process at any point, simply input '00' \n")
# further instructions given to the user on what to do

while item != "00":
    # this bar now states that while the user has not given a value of "00", the codes below are going to be executed

    item = str(input("Please provide the name of an item you wish to store: "))
    # this now prompts the user to provide the name of the item he wants to store

    if item == "00":
        print("All entries have been properly stored!\n")
        break
    # this line breaks out of the loop whenever the user inputs an item of value "00"

    else:
        print("Name saved!\n")

    value = int(input("Now input the price for the item: "))
    print("Enter 00 when done.\n")
    # this prompts the user to to provide the price for the items earlier mentioned

    dicts.update({item: value})
    # this then stores all the information about the item into the "dicts" dictionary

while user_key != "00":
    user_key = str(input("Input the name of an item to access its price: "))
    keys = dicts.keys()

    if user_key in keys:
        print(f"The price for {user_key} is {dicts[user_key]} unit")
        print("Input 00 when done\n")
        print("Input '11' if you want to add a new item\n")

    elif user_key == "11":
        user_res = str(
            input("Do you wish to add a new item? '11'= 'yes' and '00' = 'no "))

        if user_res == "00":
            print("Okay! Back to the demo.\n")

        elif user_res == "11":
            user_val = str(input("Now provide an item name: "))
            user_price = str(input("Now provide a price tag: "))
            dicts.update({user_val: user_price})
            print("Added!\n")

        else:
            pass

    elif user_key not in keys and user_key != "00":
        print("That is not part of your items\n")

print(f"Thank you {name} for testing this demo.")
