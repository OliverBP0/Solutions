"""Opgave "Lunar arithmetic"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

--------

Denne øvelse er en valgfri udfordring for de fremragende programmører blandt jer.
Du behøver absolut ikke at løse denne øvelse for at fortsætte med succes.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Del 1:
    Se denne video fra 0:00 til 2:41:
    https://www.youtube.com/watch?v=cZkGeR9CWbk

Del 2:
    Skriv en klasse Lunar_int(), med metoder, der gør, at du kan anvende operatorerne + og * på
    objekter af denne klasse, og at resultaterne svarer til de regler, der forklares i videoen.

Del 3:
    Se resten af videoen.

Del 4:
    Skriv en funktion calc_lunar_primes(n), som retunerer en liste med de første n lunar primes.

--------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""


class Lunar_int(int):

	def __init__(self, number):
		self._number = number

	def __add__(self, other):  # Forstod godt Lunar arithmetic efter at se videoen med lyd, men havde svært ved at regne __add__ ud, så fik noget hjælp fra ChatGPT, læste dog godt igennem hvad alt gjorde.
		a = str(self)
		b = str(other)
		max_length = max(len(a), len(b))

		a = a.zfill(max_length)
		b = b.zfill(max_length)

		result = "".join(str(max(int(x), int(y))) for x, y in zip(a, b))
		return int(result)

	def __mul__(self, other):  # __mul__ blev lidt af et rod med loops... Det var så hvad jeg kom op med uden ChatGPT, har dog godt spurgt ChatGPT om hvordan en bedre version ville se ud. Det føltes en smule cheap at bruge ChatGPT til __add__, også selvom jeg nu forstår hvad det hele gør, så selvom jeg har set hvordan en bedre version af __mul__ ser ud, valgte jeg ikke at bruge den.
		a = str(self)
		b = list(reversed(str(other)))

		numbers = []
		for i in range(len(b)):
			numbers.append("".join(str(min(int(x), int(b[i]))) for x in a) + "0" * i)
		for i in range(len(numbers) - 1):
			numbers[i] = numbers[i].zfill(len(numbers[len(numbers) - 1]))
		result = ""
		for i in range(len(numbers[len(numbers) - 1])):
			current = 0
			for i2 in range(len(numbers)):
				current = max(current, int(numbers[i2][i]))
			result += str(current)
		return int(result)

def calc_lunar_primes(n):  # Jeg er helt stumped på hvordan i alverden lunar prime tallene fungerede... så siden jeg ikke rigtig kunne komme op med noget, valgte jeg bare at prøve næsten hver eneste mulighed... ikke ligefrem særlig effektivt.
	primes = []
	current = 19
	try_out = current
	continue_loop = False
	while len(primes) < n:
		if "9" not in str(current):
			current += 1
			try_out = current
			continue_loop = False
		if try_out == 9:
			try_out -= 1
			continue
		for current_primes in primes:
			if Lunar_int(current_primes) * Lunar_int(try_out) == current:
				current += 1
				try_out = current
				continue_loop = True
				break
		if continue_loop:
			continue_loop = False
			continue
		if Lunar_int(current) * Lunar_int(try_out) == current:
			current += 1
			try_out = current
			continue
		try_out -= 1
		if try_out < 1:
			primes.append(current)
			current += 1
			try_out = current
	return primes


print(Lunar_int(43) + Lunar_int(16))  # Burde være 46
print(Lunar_int(8738) * Lunar_int(63265))  # Burde være 66366565
print(calc_lunar_primes(30))
