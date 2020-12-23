data = open("C:\\Users\\djdeb\\Desktop\\Random Stuff\\Advent of Code 2020\\day17input.txt")
str = data.read()
puzzle_array = str.splitlines()

size = 20
grid = [[[[0 for z in range(size)] for y in range(size)] for x in range(size)] for w in range(size)]

for i in range(len(puzzle_array)):
	for j in range(len(puzzle_array[i])):
		if puzzle_array[i][j] == "#":
			grid[i+6][j+6][size // 2][size // 2] = 1

def cycle(grid, size):
	grid_copy = [[[[0 for z in range(size)] for y in range(size)] for x in range(size)] for w in range(size)]
	for x in range(size):
		for y in range(size):
			for z in range(size):
				for w in range(size):
						grid_copy[x][y][z][w] = grid[x][y][z][w]
	neighbors = [1, 0, -1]
	def is_valid(num):
		if num < 0 or num >= size:
			return False
		return True
	for x in range(size):
		for y in range(size):
			for z in range(size):
				for w in range(size):
					active_n = 0
					for i in neighbors:
						for j in neighbors:
							for k in neighbors:
								for m in neighbors:
									if is_valid(x + i) and is_valid(y + j) and is_valid(z + k) and is_valid(w + m) and not (i == 0 and j == 0 and k == 0 and m == 0):
										if grid_copy[x+i][y+j][z+k][w+m] == 1:
											active_n += 1
					if active_n == 3:
						grid[x][y][z][w] = 1
					elif active_n == 2 and grid[x][y][z][w] == 1:
						grid[x][y][z][w] = 1
					else:
						grid[x][y][z][w] = 0

	return None

for i in range(6):
	cycle(grid, 20)
	print("Cycle", i, "complete")


count_active = 0
for i in range(size):
	for j in range(size):
		for k in range(size):
				count_active += sum(grid[i][j][k])

print(count_active)