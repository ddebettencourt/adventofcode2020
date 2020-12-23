data = open("C:\\Users\\djdeb\\Desktop\\Random Stuff\\Advent of Code 2020\\day8input.txt")
str = data.read()
puzzle_array = str.splitlines()

def try_term():
	current_pos = 0
	done_twice = False
	acc = 0
	inst_set = {0}
	while not done_twice:
		#print(puzzle_array)
		if "nop" in puzzle_array[current_pos]:
			current_pos += 1
		elif "acc" in puzzle_array[current_pos]:
			if "-" in puzzle_array[current_pos]:
				acc += int(puzzle_array[current_pos][4:])
				current_pos += 1
			else:
				acc += int(puzzle_array[current_pos][5:])
				current_pos += 1
		else:
			if "-" in puzzle_array[current_pos]:
				current_pos += int(puzzle_array[current_pos][4:])
			else:
				current_pos += int(puzzle_array[current_pos][5:])
		if current_pos in inst_set and current_pos != 0:
			done_twice = True
		else:
			inst_set.add(current_pos)
		print(current_pos)
		if current_pos == 623:
			print(acc)
			print("FOUND IT")
	#print(acc)

for i in range(len(puzzle_array)):
	if "nop" in puzzle_array[i]:
		puzzle_array[i] = "jmp" + puzzle_array[i][3:]
	elif "jmp" in puzzle_array[i]:
		puzzle_array[i] = "nop" + puzzle_array[i][3:]
	print(puzzle_array[i])
	try_term()
	if "nop" in puzzle_array[i]:
		puzzle_array[i] = "jmp" + puzzle_array[i][3:]
	elif "jmp" in puzzle_array[i]:
		puzzle_array[i] = "nop" + puzzle_array[i][3:]



