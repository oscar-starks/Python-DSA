import random



def print_rock():
    print("""
    .... _______
    .---'   ____)
            (_____)
            (_____)
            (____)
    ..---.__(___)
    """)



def print_scissors():
    print(""" 
    ..... _______
    ..---'   ____)____
                ______)
    ...... __________)
            (____)
    . ---.__(___)

    """)

def print_paper():
    print("""
          _______
      ---'   ____)____
                ______)
                _______)
               _______)
      ---.__________)


    """)



user_val = 3

while user_val != 22:
    print("0 for Rock, 1 for Paper and 2 for Scissors: ")
    user_val = eval(input())
    comp_list = [0, 1, 2]
    comp_rand = random.choice(comp_list)

    if user_val == 0 and comp_rand == 0:
        print("You chose: ")
        print_rock()
        print("Computer chose: ")
        print_rock()
        print("It's a draw!")
        # print("You choose rock and Computer chose rock, it's a draw!")
        print("Input 22 to exit the game")

    elif  user_val == 0 and comp_rand == 1:
        print("You chose: ")
        print_rock()
        print("Computer chose: ")
        print_paper()
        print("Computer wins!")
        # print("You choose rock and Computer chose paper, computer wins!")
        print("Input 22 to exit the game")

    elif  user_val == 0 and comp_rand == 2:
        print("You chose: ")
        print_rock()
        print("Computer chose: ")
        print_scissors()
        print("You win!")
        print("Input 22 to exit the game")

    elif  user_val == 1 and comp_rand == 0:
        print("You chose: ")
        print_paper()
        print("Computer chose: ")
        print_rock()
        print("You choose paper and Computer chose rock, you win!")
        print("Input 22 to exit the game")

    elif  user_val == 1 and comp_rand == 1:
        print("You chose: ")
        print_paper()
        print("Computer chose: ")
        print_paper()
        print("You choose paper and Computer chose paper, it's a draw!")
        print("Input 22 to exit the game")

    elif  user_val == 1 and comp_rand == 2:
        print("You chose: ")
        print_paper()
        print("Computer chose: ")
        print_scissors()
        print("You choose paper and Computer chose scissors, computer wins!")
        print("Input 22 to exit the game")

    elif  user_val == 2 and comp_rand == 0:
        print("You chose: ")
        print_scissors()
        print("Computer chose: ")
        print_rock()
        print("You choose scissors and Computer chose rock, computer wins!")
        print("Input 22 to exit the game")

    elif  user_val == 2 and comp_rand == 1:
        print("You chose: ")
        print_scissors()
        print("Computer chose: ")
        print_paper()
        print("You choose scissors and Computer chose paper, you win!")
        print("Input 22 to exit the game")

    elif  user_val == 2 and comp_rand == 2:
        print("You chose: ")
        print_scissors()
        print("Computer chose: ")
        print_scissors()
        print("You choose scissord and Computer chose scissors, it's a draw!")
        print("Input 22 to exit the game")
