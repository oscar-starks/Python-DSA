import random

word_choice = ['goat', 'chicken', 'baboon', 'hippopotamus', 'aadvark']

random_choice = random.choice(word_choice)

user_answer = []
for dashes in range(len(random_choice)):
    user_answer.append("_")


chances = 0

print("""\n         Welcome to my word guessing game.
         You are to guess the letters in the hidden word till it is completed
         Also know that you have only 5 chances to input the wrong answers if which exceeded, you lose
         Good luck in the game!""")

while True:

    final = ""

    for letters in user_answer:
        final += letters

    if chances == 5:
        print("You've exhausted your chances, you lose!")
        print(f"The correct word is {random_choice}")
        break

    print(final)
    if final == random_choice:
        print(f"The final word is {final}! Congratulations, you won")
        break

    # print(user_answer, final)
    
    
    user_input = input("Guess the letters in the random word: ")
    n = 0

    if user_input in random_choice:
        print("Your letter is in the hidden word.")

        for char in random_choice:
            
            if user_input == char:
                #print('True', n )
                user_answer[n] = user_input
                # for letters in user_answer:
                #     final += letters
                #print(user_answer)
                n += 1
                # print(final)
            else:
                n += 1
    else:
            #print("False", n)
            #print(user_answer)
        print(f"The characters are not in the random word, you have {4-chances} chances left.")
        chances += 1
            

    