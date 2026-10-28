#Python program to repeatedly ask the user for a number until they enter zero

num = int(input("Enter a number: "))

while num != 0:
    num = int(input("Enter a number: "))

print("You entered zero. Program stopped.")