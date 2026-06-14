def inventory(lines):
	numbers = {}
	for i in range(lines):
		current = 0
		while True:
			if current not in numbers:
				numbers[current] = 0
			amount_of = numbers[current]
			print(f"{amount_of}", end=" ")
			if amount_of not in numbers:
				numbers[amount_of] = 1
			else:
				numbers[amount_of] += 1
			if amount_of == 0:
				break
			current += 1
		print()


inventory(20)
