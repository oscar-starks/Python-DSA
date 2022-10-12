
def highest_bidder(dictionary={}):
    bidder = ""
    highest_bid = 0
    for bids in dictionary:
        bid_counter = int(dictionary[bids])
        if bid_counter > highest_bid:
            bidder = bids
            highest_bid = bid_counter

    #print(highest_bid, bidder)
    print(
        f"The highest bidder is {bidder.capitalize()} with a bid of ${highest_bid}")


bid_dict = {}

while True:
    name = input("What is your name: ")
    bid = eval(input("What is your bid: $"))
    bid_dict.update({name: bid})
    choice = input("Is there another bidder? ").lower()

    if choice == "yes":
        for n in range(15):
            print("\n")
    else:
        print(bid_dict)
        highest_bidder(bid_dict)
        break
