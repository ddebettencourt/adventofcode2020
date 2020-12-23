
data = open("C:\\Users\\djdeb\\Desktop\\Random Stuff\\Advent of Code 2020\\day3input.txt")
str = data.read()
puzzle_array = str.splitlines()

trees_enc = 0
for i in range(0, len(puzzle_array), 2):
	n = ((i // 2) % 31)
	if puzzle_array[i][n] == "#":
		trees_enc += 1
print(trees_enc)