
print("Welcome to Python Pizza deliveries.")
pizza_size = input(
    "What size of pizza do you want? 's' for small, 'm' for medium, 'l' for large: ").lower()
add_pepperoni = input("Do you want pepperoni? y for yes and n for no: ")
extra_cheese = input("Do you want extra cheese? y for yes and n for no: ")

if pizza_size == "s":
    price = 15

elif pizza_size == "m":
    price = 20

else:
    price = 25

if add_pepperoni == "y":
    if pizza_size == "s":
        price += 2
    else:
        price += 3

if extra_cheese == "y":
    price += 1

else:
    price

print(f"Your final bill is {price}$")
