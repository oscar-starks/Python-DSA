user_name = str(
    input("Hello there, please may I know your name? ")).capitalize()
user_height = eval(input(f"Okay {user_name}, now input your height in cm: "))

if user_height >= 120:
    user_age = eval(input("Now input your age: "))

    if user_age <= 12:
        user_choice = input(
            "Do you want pictures on your ticker? 'y' for yes and 'n' for no ").lower()

        if user_choice == "y":
            print("Your ticket is 8$ ")

        elif user_choice == "n":
            print("Your ticket is 5$")

        else:
            print("Invalid option")

    elif user_age <= 18:
        user_choice = input(
            "Do you want pictures on your ticker? 'y' for yes and 'n' for no ").lower()

        if user_choice == "y":
            print("Your ticket is 10$ ")

        elif user_choice == "n":
            print("Your ticket is 7$")

        else:
            print("Invalid option")

    elif user_age > 18:
        if user_age >= 45 and user_age <= 50:
            print("Congrats, you won a free ticket!")

        else:
            user_choice = input(
                "Do you want pictures on your ticker? 'y' for yes and 'n' for no ").lower()

            if user_choice == "y":
                print("Your ticket is 15$ ")

            elif user_choice == "n":
                print("Your ticket is 12$")

            else:
                print("Invalid option")

            #print(f"Dear {user_name}, your ticket costs 12$")

else:
    print("You are not eligible to go for the roller coaster ride.")
