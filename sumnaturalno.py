#Python program to calculate the sum of natural numbers up to a given number
n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum =", total)