
data = open("C:\\Users\\djdeb\\Desktop\\Random Stuff\\Advent of Code 2020\\day1input.txt")
str = data.read()
puzzle_array = str.splitlines()

def part_1():
	hashset = set()
	for val in puzzle_array:
		if (2020 - int(val)) in hashset:
			print((2020 - int(val)) * int(val))
		else:
			hashset.add(int(val))

def part_2():
	hashset = set()
	for val in puzzle_array:
		hashset.add(int(val))
	for val in puzzle_array:
		for val2 in puzzle_array:
			if (2020 - int(val) - int(val2)) in hashset:
				print((2020 - int(val) - int(val2)) * int(val) * int(val2))
