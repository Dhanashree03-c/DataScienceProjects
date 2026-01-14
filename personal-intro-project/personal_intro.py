#Bio Data
print("-----Your Bio Data-----")
name = input("What is your name? ")
age = input("How old are you? ")
hobby = input("What is your favourite hobby? ")
city = input("Where do you live? ")

print(f"\U0001F389 Welcome {name}!\U0001F389")
print(f"Your are {age} years old and love {hobby}.")
print(f"You live in {city}.")

foods = ["Burger", "Pasta", "Ramen", "Sushi", "Pizza"]
print("Here is a list of foods:")
for food in foods:
    print(f"~ {food}")
print(f"Your favourite food is {foods[3]}.")

#Arithmetic operations
print("\nTo perform arithemtic operations,")
a = input("Enter one number:")
b = input("Enter another number: ")

print(f"\nAddition: {int(a) + int(b)}")
print(f"Subtraction: {int(a) - int(b)}")
print(f"Multiplication: {int(a) * int(b)}")
print(f"Division: {int(a) / int(b)}")