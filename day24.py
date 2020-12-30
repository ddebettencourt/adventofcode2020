data = open("C:\\Users\\djdeb\\Desktop\\Random Stuff\\Advent of Code 2020\\day24input.txt")
str1 = data.read()
puzzle_array = str1.splitlines()

neighbors = [[-1, 0], [-0.5, 0.75], [0.5, 0.75], [1, 0], [0.5, -0.75], [-0.5, -0.75]]
tile_dict = {}

def flip_tile(tile):
	dis_e = 0
	dis_n = 0
	line = tile
	j = 0
	while j < len(line):
		if line[j] == "e":
			dis_e += 1
			j += 1
		elif line[j] == "w":
			dis_e -= 1
			j += 1
		elif line[j] == "n" and line[j+1] == "e":
			dis_e += 0.5
			dis_n += 0.75
			j += 2
		elif line[j] == "n" and line[j+1] == "w":
			dis_e -= 0.5
			dis_n += 0.75
			j += 2
		elif line[j] == "s" and line[j+1] == "e":
			dis_e += 0.5
			dis_n -= 0.75
			j += 2
		elif line[j] == "s" and line[j+1] == "w":
			dis_e -= 0.5
			dis_n -= 0.75
			j += 2
	print("flipped", dis_e, dis_n)
	if (dis_e * 10000) + dis_n in tile_dict:
		tile_dict[(dis_e * 10000) + dis_n] = not tile_dict[(dis_e * 10000) + dis_n]
		print("flipped again")
	else:
		tile_dict[(dis_e * 10000) + dis_n] = True

def flip_tile_loc(dis_e, dis_n):
	if (dis_e * 10000) + dis_n in tile_dict:
		tile_dict[(dis_e * 10000) + dis_n] = not tile_dict[(dis_e * 10000) + dis_n]
		print("flipped again")
	else:
		tile_dict[(dis_e * 10000) + dis_n] = True

def do_day(tile_dict):
	tile_dict2 = dict(tile_dict)
	for tile in tile_dict2:
		count_n = 0
		for i in range(6):
			if tile + (10000 * neighbors[i][0]) + neighbors[i][1] in tile_dict2 and tile_dict2[tile + (10000 * neighbors[i][0]) + neighbors[i][1]] == True:
				count_n += 1
				#print("found neighbor")
		if (count_n == 0 or count_n > 2) and tile_dict2[tile]:
			tile_dict[tile] = not tile_dict[tile]
		elif count_n == 2 and not tile_dict2[tile]:
			tile_dict[tile] = not tile_dict[tile]

def do_days(tile_dict, num):
	for i in range(num):
		do_day(tile_dict)
		print("day", i)
		count()

def initialize():
	for i in range(-400, 400):
		for j in range(-400, 400):
			if (5000 * i + j * 0.75) not in tile_dict:
				tile_dict[5000 * i + j * 0.75] = False

for i in range(len(puzzle_array)):
	flip_tile(puzzle_array[i])

def count():
	count = 0
	for tile in tile_dict:
		if tile_dict[tile]:
			count += 1
	print(count)


