data = open("C:\\Users\\djdeb\\Desktop\\Random Stuff\\Advent of Code 2020\\day11input.txt")
str = data.read()
puzzle_array = str.splitlines()


def part1():
	for i in range(1001):
		new_array = list(puzzle_array)
		for j in range(len(new_array)):
			for k in range(len(new_array[0])):
				total_empty = 0
				total = 0
				if j > 0:
					total += 1
					if puzzle_array[j-1][k] == "L" or puzzle_array[j-1][k] == ".":
						total_empty += 1

				if j < len(new_array)-1:
					total += 1
					if puzzle_array[j+1][k] == "L" or puzzle_array[j+1][k] == ".":
						total_empty += 1

				if k > 0:
					total += 1
					if puzzle_array[j][k-1] == "L" or puzzle_array[j][k-1] == ".":
						total_empty += 1
				if k < len(new_array[0]) - 1:
					total += 1
					if puzzle_array[j][k+1] == "L" or puzzle_array[j][k+1] == ".":
						total_empty += 1
				if j > 0 and k > 0:
					total += 1
					if puzzle_array[j-1][k-1] == "L" or puzzle_array[j-1][k-1] == ".":
						total_empty += 1
				if j > 0 and k < len(new_array[0])-1:
					total += 1
					if puzzle_array[j-1][k+1] == "L" or puzzle_array[j-1][k+1] == ".":
						total_empty += 1
				if k > 0 and j < len(new_array)-1:
					total += 1
					if puzzle_array[j+1][k-1] == "L" or puzzle_array[j+1][k-1] == ".":
						total_empty += 1
				if k < len(new_array[0])-1 and j < len(new_array) - 1:
					total += 1
					if puzzle_array[j+1][k+1] == "L" or puzzle_array[j+1][k+1] == ".":
						total_empty += 1

				if total_empty == total:
					if new_array[j][k] != ".":
						new_array[j] = new_array[j][0:k] + "#" + new_array[j][k+1:]
				if total - total_empty >= 4:
					if new_array[j][k] != ".":
						new_array[j] = new_array[j][0:k] + "L" + new_array[j][k+1:]
		puzzle_array = list(new_array)
		#print(puzzle_array)

	count = 0
	for i in puzzle_array:
		for j in i:
			if j == "#":
				count += 1
	print(count)

for i in range(102):
		new_array = list(puzzle_array)
		for j in range(len(new_array)):
			for k in range(len(new_array[0])):
				total_occupied = 0
				total = 0
				jn = j-1
				kn = k
				while jn >= 0 and (puzzle_array[jn][kn] != "#" and puzzle_array[jn][kn] != "L"):
					jn -= 1
				if jn < 0:
					None
				elif puzzle_array[jn][kn] == "#":
					total_occupied += 1
					total += 1
				elif puzzle_array[jn][kn] == "L":
					total += 1
				jn = j+1
				kn = k
				while jn <= len(new_array)-1 and (puzzle_array[jn][kn] != "#" and puzzle_array[jn][kn] != "L"):
					jn += 1
					#print(jn, len(new_array))
				if jn > len(new_array)-1:
					None
				elif puzzle_array[jn][kn] == "#":
					total_occupied += 1
					total += 1
				elif puzzle_array[jn][kn] == "L":
					total += 1

				jn = j
				kn = k+1
				while kn <= len(new_array[0])-1 and (puzzle_array[jn][kn] != "#" and puzzle_array[jn][kn] != "L"):
					kn += 1
				if kn > len(new_array[0])-1:
					None
				elif puzzle_array[jn][kn] == "#":
					total_occupied += 1
					total += 1
				elif puzzle_array[jn][kn] == "L":
					total += 1

				jn = j
				kn = k-1
				while kn >= 0 and (puzzle_array[jn][kn] != "#" and puzzle_array[jn][kn] != "L"):
					kn -= 1
				if kn < 0:
					None
				elif puzzle_array[jn][kn] == "#":
					total_occupied += 1
					total += 1
				elif puzzle_array[jn][kn] == "L":
					total += 1

				jn = j-1
				kn = k-1
				while jn >= 0 and kn >= 0 and (puzzle_array[jn][kn] != "#" and puzzle_array[jn][kn] != "L"):
					jn -= 1
					kn -= 1
				if jn < 0 or kn < 0:
					None
				elif puzzle_array[jn][kn] == "#":
					total_occupied += 1
					total += 1
				elif puzzle_array[jn][kn] == "L":
					total += 1

				jn = j-1
				kn = k+1
				while jn >= 0 and kn <= len(new_array[0])-1 and (puzzle_array[jn][kn] != "#" and puzzle_array[jn][kn] != "L"):
					jn -= 1
					kn += 1
				if jn < 0 or kn > len(new_array[0])-1:
					None
				elif puzzle_array[jn][kn] == "#":
					total_occupied += 1
					total += 1
				elif puzzle_array[jn][kn] == "L":
					total += 1
				
				jn = j+1
				kn = k-1
				while jn <= len(new_array)-1 and kn >= 0 and (puzzle_array[jn][kn] != "#" and puzzle_array[jn][kn] != "L"):
					jn += 1
					kn -= 1
				if kn < 0 or jn > len(new_array)-1:
					None
				elif puzzle_array[jn][kn] == "#":
					total_occupied += 1
					total += 1
				elif puzzle_array[jn][kn] == "L":
					total += 1

				jn = j+1
				kn = k+1
				while jn <= len(new_array)-1 and kn <= len(new_array[0])-1 and (puzzle_array[jn][kn] != "#" and puzzle_array[jn][kn] != "L"):
					jn += 1
					kn += 1
				if jn > len(new_array)-1 or kn > len(new_array[0])-1:
					None
				elif puzzle_array[jn][kn] == "#":
					total_occupied += 1
					total += 1
				elif puzzle_array[jn][kn] == "L":
					total += 1


				#print(total_occupied, j, k)
				if total_occupied == 0:
					if new_array[j][k] != ".":
						new_array[j] = new_array[j][0:k] + "#" + new_array[j][k+1:]
				if total_occupied >= 5:
					if new_array[j][k] != ".":
						new_array[j] = new_array[j][0:k] + "L" + new_array[j][k+1:]
		puzzle_array = list(new_array)
		#print(puzzle_array)
count = 0
for i in puzzle_array:
	for j in i:
		if j == "#":
			count += 1
print(count)
