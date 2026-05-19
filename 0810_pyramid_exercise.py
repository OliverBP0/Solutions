"""Opgave "Number pyramid"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

--------

Denne øvelse er en valgfri udfordring for de fremragende programmører blandt jer.
Du behøver absolut ikke at løse denne øvelse for at fortsætte med succes.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Del 1:
    Se de første 93 sekunder af denne video: https://www.youtube.com/watch?v=NsjsLwYRW8o

Del 2:
    Skriv en funktion "pyramid", der producerer de tal, der er vist i videoen.
    Funktionen har en parameter "lines", der definerer, hvor mange talrækker der skal produceres.
    Funktionen udskriver tallene i hver række og også deres sum.

Del 3:
    I hovedprogrammet kalder du funktionen med fx 7 som argument.

Del 4:
    Tilføj en mere generel funktion pyramid2.
    Denne funktion har som andet parameter "firstline" en liste med pyramidens øverste rækkens tallene.

Del 5:
    I hovedprogrammet kalder du pyramid2 med fx 10 som det første argument
    og en liste med tal efter eget valg som andet argument.
    Afprøv forskellige lister som andet argument.

Hvis du ikke aner, hvordan du skal begynde, kan du åbne 0812_pyramid_help.py og starte derfra

--------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""


def list_builder(number_list, index, number):
	new_list = []
	index = 0
	:
		if list_index == index:
			new_list.append(number)
			continue
		new_list.append(number_list[index])
	return new_list
def pyramid(lines):
	numbers = [1, 1]
	next_list = []
	current = 2
	for _ in range(lines):
		for index in range(len(numbers)):
			print(f"{numbers[index]}", end=" ")
			if index + 1 >= len(numbers):
				break
			if numbers[index] + numbers[index + 1] == current:
				next_list = list_builder(numbers, index + 1, current)
		print()
		numbers = next_list
		current += 1


pyramid(3)
