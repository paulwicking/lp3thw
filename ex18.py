# this one is like scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is pointless, let's do this:
def print_two_again(arg1, arg2):
	print(f"arg1: {arg1}, arg2: {arg2}")

# this takes one argument
def print_one(arg1):
	print(f"arg1: {arg1}")

# this takes NO argument
def print_none():
	print("I got nothin'.")

print_two("Shaw", "Zed")
print_two_again("Shaw", "Zed")
print_one("Shaw")
print_none()
