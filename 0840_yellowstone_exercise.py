"""Opgave "Yellowstone"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

--------

Denne øvelse er en valgfri udfordring for de fremragende programmører blandt jer.
Du behøver absolut ikke at løse denne øvelse for at fortsætte med succes.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.


Skriv en funktion som beregner Yellowstone-følgen. For at nå det, løs de følgende delopgaver:

Del 1:
    Se de første 4 minutter og 16 sekunder af denne video:
    https://www.youtube.com/watch?v=DUaqiM1bGX4

    Hvis du hellere vil have reglerne på skrift:
    Definer en række positive heltal ved hjælp af reglerne, at
        a(1) = 1, a(2) = 2, a(3) = 3,
        og for n ≥ 4 er a(n) det mindste tal, der ikke allerede er i rækken,
        som har en fælles faktor med a(n - 2), men som er relativt primtal i forhold til a(n - 1).
Del 2:
    Skriv en funktion prime_list(n), der returnerer de første n primtal som en list.

Del 3:
    Skriv en funktion prime_factorization(number), der returnerer
    en list over primfaktorerne for number.

    Prime factorization eller integer factorization af et tal er at nedbryde et
    tal til et sæt af primtal, som ganges sammen for at resultere i det oprindelige tal.
    Dette er også kendt som prime decomposition.
    Eksempel: 2, 2, 5 er primfaktoriseringen af 20.

Del 4:
    Skriv en funktion greatest_common_divisor(number1, number2), der returnerer den største fælles divisor for de to tal.
    Eksempel: Den største fælles divisor for 20 og 70 er 10 (fordi 20 og 70 har de fælles primfaktorer 2 og 5).

Del 5:
    Skriv en funktion relative_prime(number1, number2), der returnerer True, hvis de to tal er relative primtal
    til hinanden, ellers False.
    Relativt primtal betyder, at den største fælles divisor for de to tal er 1.

Del 6:
    Skriv en funktion yellowstone(n), der returnerer de første n elementer af Yellowstone-følgen som en list.
    Brug denne liste til at kontrollere din løsning: https://oeis.org/A098550/b098550.txt

--------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""


def get_factors(number, exclude_first=False):
	factors = []
	for i in range(1 if not exclude_first else 2, number + 1):
		if number % i < 1:
			factors.append(i)
	return factors

def prime_factorization(number):
	primes = []
	factors = get_factors(number, True)
	current_factor = 0
	while True:
		if current_factor >= len(factors):
			break
		if number % factors[current_factor] > 0:
			current_factor += 1
			continue
		primes.append(factors[current_factor])
		number //= factors[current_factor]
	return primes

def relative_prime(number1, number2):
	return not greatest_common_divisor(number1, number2) > 1

def greatest_common_divisor(number1, number2):
	while number2 != 0:
		number1, number2 = number2, number1 % number2
	return number1

def prime_list(number):
	primes = []
	test_number = 2
	while len(primes) < number:
		if len(get_factors(test_number)) < 3:
			primes.append(test_number)
		test_number += 1
	return primes

def yellowstone(number):  # Versionen nedenunder er før jeg spurgte ChatGPT om hjælp, den duer stadig, men tog måske 6-8 minutter om at regne de første 1000 tal ud, dog ikke længere efter den primære performance fejl var med min GCD. Lad os bare sige jeg overkomplicerede det... Som altid.
	numbers = [1, 2, 3]
	used = set(numbers)
	while len(numbers) < number:
		start = 1
		while True:
			if start not in used:
				if greatest_common_divisor(start, numbers[-1]) == 1 and greatest_common_divisor(start, numbers[-2]) > 1:
					numbers.append(start)
					used.add(start)
					break
			start += 1
	return numbers[:number]
# def yellowstone(number):  # Kan klart mærke og sikkert også se at det her kunne være lavet en del mere effektivt... men havde problemer nok med bare at få det til at du.
# 	numbers = [1, 2, 3]
# 	while len(numbers) < number:
# 		relative = numbers[len(numbers) - 1]
# 		legal_factors = get_factors(numbers[len(numbers) - 2], True)
# 		multiplier = 1
# 		smallest = None
# 		while True:
# 			for factors in legal_factors:
# 				if relative_prime(factors * multiplier, relative):
# 					if factors * multiplier not in numbers:
# 						if smallest is None:
# 							smallest = factors * multiplier
# 						elif factors * multiplier < smallest:
# 							smallest = factors * multiplier
# 			if smallest is not None:
# 				new_smallest = None
# 				for factors in legal_factors:
# 					special_multiplier = 1
# 					while True:
# 						if relative_prime(factors * special_multiplier, relative):
# 							if factors * special_multiplier not in numbers:
# 								if new_smallest is None:
# 									new_smallest = factors * special_multiplier
# 								elif factors * special_multiplier < new_smallest:
# 									new_smallest = factors * special_multiplier
# 						special_multiplier += 1
# 						if factors * special_multiplier >= smallest:
# 							break
# 				if new_smallest is not None and new_smallest < smallest:
# 					smallest = new_smallest
# 				numbers.append(smallest)
# 				break
# 			multiplier += 1
# 	return numbers[:number]


for a, b in enumerate(yellowstone(15)):
	print(a + 1, b)
