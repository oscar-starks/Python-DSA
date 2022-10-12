import random
i = 0

username = str(input(
    "Hello user and welcome to my game! But before we start, may I know your name? ")).capitalize()

print(f"""
Thank you {username} for providing your name. Now please follow the instructions:
(1.) You are expected to guess random numbers and hints will be provided.
(2.) You have only three chances after which if you fail to provide the correct number, you lose.
(3.) Good luck and have fun!

""")

while i < 3:
    randomnums = random.randint(1, 10)
    print(f"Hints: {randomnums + 5}, {randomnums + 1}, {randomnums + 3} ")
    ans = eval(input("Guess a number: "))

    if (ans == randomnums):
        i += 1
        if i == 1:
            print(f"Congratulations {username}! You won in {i} attempt!")
            break

        else:
            print(f"Congratulations {username}! You won in {i} attempts!")
            break

    elif (ans != randomnums and i != 2):
        i += 1
        print("Wrong answer, try again. ")

    else:
        print("You lose!")
        break
