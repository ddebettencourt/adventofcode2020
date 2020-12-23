data = open("C:\\Users\\djdeb\\Desktop\\Random Stuff\\Advent of Code 2020\\day16input.txt")
str = data.read()
puzzle_array = str.splitlines()

valid_nums = set()

for i in range(10):
	ar1 = puzzle_array[i].split()[2]
	ar2 = puzzle_array[i].split()[4]
	for j in range(int(ar1.split("-")[0]), int(ar1.split("-")[1]) + 1):
		valid_nums.add(j)
	for j in range(int(ar2.split("-")[0]), int(ar2.split("-")[1]) + 1):
		valid_nums.add(j)
for i in range(10, 20):
	ar1 = puzzle_array[i].split()[1]
	ar2 = puzzle_array[i].split()[3]
	for j in range(int(ar1.split("-")[0]), int(ar1.split("-")[1]) + 1):
		valid_nums.add(j)
	for j in range(int(ar2.split("-")[0]), int(ar2.split("-")[1]) + 1):
		valid_nums.add(j)

invalid_tickets = []
invalid_vals = []
for i in range(25, len(puzzle_array)):
	ar1 = puzzle_array[i].split(",")
	invalid = False
	for j in range(len(ar1)):
		if int(ar1[j]) not in valid_nums:
			invalid = True
			invalid_vals.append(int(ar1[j]))
	if invalid:
		invalid_tickets.append(i)

valid_ticket_list = []
for i in range(25, len(puzzle_array)):
	if i not in invalid_tickets:
		ar1 = puzzle_array[i].split(",")
		for j in range(len(ar1)):
			ar1[j] = int(ar1[j])
		valid_ticket_list.append(ar1)

lo_hi = [0 for i in range(20)]
hi_lo = [0 for i in range(20)]

for i in range(10):
	ar1 = puzzle_array[i].split()[2]
	ar2 = puzzle_array[i].split()[4]
	lo_hi[i] = int(ar1.split("-")[1])
	hi_lo[i] = int(ar2.split("-")[0])
for i in range(10, 20):
	ar1 = puzzle_array[i].split()[1]
	ar2 = puzzle_array[i].split()[3]
	lo_hi[i] = int(ar1.split("-")[1])
	hi_lo[i] = int(ar2.split("-")[0])


min_and_max = [0 for i in range(20)]
has_x = [[True for i in range(20)] for j in range(20)]
for i in range(20):
	ar = [el[i] for el in valid_ticket_list]
	min_and_max[i] = [min(ar), max(ar)]
	for k in range(20):
		for j in range(lo_hi[k] + 1, hi_lo[k]):
			if j in ar:
				has_x[k][i] = False


for i in range(693, 715):
	ar = [el[12] for el in valid_ticket_list]
	if i in ar:
		print("False")




