import random


names = input("Give me everybody's names separated by commas: ").capitalize()
name_list = names.split(", ")
bill_choice = random.choice(name_list)

print(f"The person who's going to pay the bill is: {bill_choice}")
