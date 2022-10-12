import random


def random_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    choices = random.choice(cards)
    return choices


def calculate_score(cards):
    """This takes a list of cards and returns the score generated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw "
    elif computer_score == 0:
        return "You lose, the opponent has a blackjack!"
    elif user_score == 0:
        return "You win with a blackjack!"
    if user_score > 21 and computer_score > 21:
        if user_score > computer_score:
            return "You win"
        elif computer_score > user_score:
            return "Computer wins"

    elif user_score > 21:
        return "You lose, you went over!"
    elif computer_score > 21:
        return "You win, the opponent went over!"


user_cards = []
computer_cards = []
is_game_over = False

for _ in range(2):
    user_cards.append(random_card())
    computer_cards.append(random_card())

while True:

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, your score: {user_score}")
    print(f"Computer's first card {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        break
    else:
        user_should_deal = input(
            "Type 'y' to get another card or type 'n' to pass: ")
        if user_should_deal == 'y':
            user_cards.append(random_card())
        else:
            break

while computer_score != 0 and computer_score < 17:
    computer_cards.append(random_card())
    computer_score = calculate_score(computer_cards)

print(f"Your final hand: {user_cards}, Your score: {user_score}")
print(
    f"Computer's final hand: {computer_cards}, Computer's score: {computer_score}")
print(compare(user_score, computer_score))
