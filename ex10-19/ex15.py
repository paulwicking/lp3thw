# include argv
from sys import argv

# assign argv contents to variables
script, filename = argv

# open file as specified by argv[1]
txt = open(filename)

# print the contents of the file
print(f"Here's your file {filename}:")
print(txt.read())

# provide a prompt and ask user to repeat the filename
print("Type the filename again:")
file_again = input("> ")

# open the file as given. bad input causes script to crash!
txt_again = open(file_again)

# print the contents of the file again
print(txt_again.read())

# close our files
txt.close()
txt_again.close()
