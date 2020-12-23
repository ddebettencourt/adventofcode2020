data = open("C:\\Users\\djdeb\\Desktop\\Random Stuff\\Advent of Code 2020\\day9input.txt")
str = data.read()
puzzle_array = str.splitlines()

for i in range(len(puzzle_array)):
	puzzle_array[i] = int(puzzle_array[i])
last25 = puzzle_array[0:25]
print(last25)
for i in range(25, len(puzzle_array)):
	found = False
	for j in range(25):
		for k in range(25):
			if int(last25[j]) + int(last25[k]) == int(puzzle_array[i]):
				found = True
				#print(last25[j], last25[k])
	if not found:
		None
		print(puzzle_array[i])
		print(i)
	for m in range(24):
		last25[m] = last25[m + 1]
	last25[24] = puzzle_array[i]

for i in range(508):
	for j in range(508):
		if sum(puzzle_array[i:j+1]) == 31161678:
			print(puzzle_array[i]+puzzle_array[j])
			print(puzzle_array[i:j+1])
			print(min(puzzle_array[i:j+1]) + max(puzzle_array[i:j+1]))
