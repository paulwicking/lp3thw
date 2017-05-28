from sys import argv

script, filename = argv

print(f"We are going to erase {filename}.")
print("If you do not want that, hit CTRL-C (^C) now.")
print("If you are okay to keep going, hit return.")

input("?")

print("Opening file...")
target = open(filename, 'w')

#print("Truncating file. Bye bye!")
#target.truncate() # file already truncated on open!

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these lines to the file.")

writethis = line1 + "\n" + line2 + "\n" + line3 + "\n"

target.write(writethis)

print("And finally, we close it.")
target.close()
