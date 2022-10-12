print("""            _                               
                    | |                              
 _ __ ___  _   _ ___| |__  _ __ ___   ___  _ __ ___  
| '_ ` _ \| | | / __| '_ \| '__/ _ \ / _ \| '_ ` _ \ 
| | | | | | |_| \__ \ | | | | | (_) | (_) | | | | | |
|_| |_| |_|\__,_|___/_| |_|_|  \___/ \___/|_| |_| |_|
                                                     """)
print("""Welcome to Treasure Island.
Your mission is to find the treasure.""")
user_dir = input(
    "Which way do you wanna go? l for left and r for right: ").lower()

if user_dir == "r":
    print("You fell into a hole. Game Over.")

else:
    stage_res = input(
        "Yo're in the middle of a lake. Do you want to swim or wait? s for swim and w for wait: ")

    if stage_res == "s":
        print("You got eaten by a shark! Game Over.")
    else:
        stage_res = input(
            "You've gotten to the great mushroom door! Which door do you choose? r for red, b for blue and y for yellow: ")
        if stage_res == "r" or stage_res == "b":
            print("Wrong door! Game Over.")
        else:
            print("You win!")
