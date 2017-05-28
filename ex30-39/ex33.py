def print_numbers(limit, step):
	numbers = []

	for x in range (0, limit):
		numbers.append(x)

		x += step
		print("Numbers now: ", numbers)

	print("The numbers: ")

	for num in numbers:
		print(num)

limit = int(input("Limit? "))
step = int(input("Step? "))

print_numbers(limit, step)

