from sys import argv
# Read the WYSS section for how to run this
script, first, second, third = argv

forgot = input("What did you forget? ")

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

print("And you almost forgot:", forgot)
