import random


for i in range(3):
    randomnums = random.randint(1, 10)
    print("Guess a number \n")
    ans = eval(
        input(f"Hints: {randomnums + 5}, {randomnums + 1}, {randomnums + 3} "))

    if(ans == randomnums):
        print("You won!")
        break

    elif (ans != randomnums and i != 2):
        print("Wrong answer, try again.")
        print(i)

    elif(ans != randomnums and i == 2):
        print("You lose")
