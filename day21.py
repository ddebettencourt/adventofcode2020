data = open("C:\\Users\\djdeb\\Desktop\\Random Stuff\\Advent of Code 2020\\day21input.txt")
str1 = data.read()
puzzle_array = str1.splitlines()

contains_no_allergens = set()
foods_lists = {}
allergy_lists = {}
allergens = ["shellfish", "peanuts", "soy", "nuts", "eggs", "wheat", "sesame", "fish"]
#allergens = ["soy", "dairy", "fish"]

for i in range(len(puzzle_array)):
	foods = puzzle_array[i].split("(")[0]
	foods = foods.split()
	for food in foods:
		if food not in foods_lists:
			foods_lists[food] = [i]
		else:
			foods_lists[food].append(i)
	allergies = [puzzle_array[i].split("(")[1][9:]]
	if "," in allergies[0]:
		allergies = allergies[0].split(",")
	#print(allergies)
	for j in range(len(allergies)):
		if " " in allergies[j]:
			allergies[j] = allergies[j].split()[0]
		if ")" in allergies[j]:
			allergies[j] = allergies[j][:-1]
		if "," in allergies[j]:
			allergies[j] = allergies[j][:-1]
	allergy_lists[i] = allergies

#print(foods_lists, allergy_lists)

no_allergen = {}

for i in range(len(puzzle_array)):
	not_in = []
	for j in range(len(allergens)):
		if allergens[j] not in allergy_lists[i]:
			not_in.append(j)
	no_allergen[i] = not_in

contains_i = {}
for i in range(len(allergens)):
	contains_i[i] = []

for i in range(len(puzzle_array)):
	for j in range(len(allergens)):
		if allergens[j] in allergy_lists[i]:
			contains_i[j].append(i)


count = 0
for food in foods_lists:
	arr = [True for i in range(len(allergens))]
	for i in range(len(allergens)):
		for j in range(len(contains_i[i])):
			if contains_i[i][j] not in foods_lists[food]:
				arr[i] = False
	if not any(arr):
		contains_no_allergens.add(food)
		count += len(foods_lists[food])
	else:
		print(food, arr)

danger = set()
for food in foods_lists:
	if food not in contains_no_allergens:
		danger.add(food)

print(count)






