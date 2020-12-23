data = open("C:\\Users\\djdeb\\Desktop\\Random Stuff\\Advent of Code 2020\\day20input.txt")
str1 = data.read()
puzzle_array = str1.splitlines()

tiles = {}
i = 0
while i < len(puzzle_array):
	if "Tile" in puzzle_array[i]:
		num = int(puzzle_array[i].split()[1].split(":")[0])
		tiles[num] = []
		for j in range(10):
			tiles[num].append(puzzle_array[i+j+1])
		i += 10
	i += 1

tile_sides = {}

for key in tiles.keys():
	#print(key)
	ls = []
	tile_sides[key] = ls
	tile_sides[key].append(tiles[key][0])
	tile_sides[key].append(tiles[key][0][::-1])
	tile_sides[key].append(tiles[key][9])
	tile_sides[key].append(tiles[key][9][::-1])
	arr = [s[0] for s in tiles[key]]
	str2 = ""
	for char in arr:
		str2 = str2 + char
	tile_sides[key].append(str2)
	tile_sides[key].append(str2[::-1])
	arr = [s[9] for s in tiles[key]]
	str2 = ""
	for char in arr:
		str2 = str2 + char
	tile_sides[key].append(str2)
	tile_sides[key].append(str2[::-1])

count_tiles = {}
all_sides = []
for tile in tile_sides.values():
	for str1 in tile:
		all_sides.append(str1)

for tile in all_sides:
	if tile not in count_tiles.keys():
		count_tiles[tile] = 1
	else:
		count_tiles[tile] += 1

ls_ones = []
for tile in count_tiles:
	if count_tiles[tile] == 1:
		ls_ones.append(tile)

for num in tile_sides:
	count = 0
	for i in range(8):
		if tile_sides[num][i] in ls_ones:
			count += 1
	if count == 4:
		print(num)

instructions = []
for side in all_sides:
	instruct = []
	for num in tile_sides:
		for i in range(8):
			if tile_sides[num][i] == side:
				instruct.append(num)
				instruct.append(i)
	instructions.append(instruct)

corners = [1693, 2111, 2207, 2339]

connected = {}
for i in range(len(instructions)):
	if len(instructions[i]) > 2:
		if instructions[i][0] not in connected:
			connected[instructions[i][0]] = [instructions[i][2]]
		else:
			if instructions[i][2] not in connected[instructions[i][0]]:
				connected[instructions[i][0]].append(instructions[i][2])
		if instructions[i][2] not in connected:
			connected[instructions[i][2]] = [instructions[i][0]]
		else:
			if instructions[i][0] not in connected[instructions[i][2]]:
				connected[instructions[i][2]].append(instructions[i][0])

attempt_array = [[0 for i in range(12)] for j in range(12)]
attempt_array[0][0] = 1693
edges = [3041, 3637, 1039, 1171, 3119, 2473, 2659, 2383, 1693, 1783, 2803, 2579, 1361, 1123, 3433, 2207, 2083, 1499, 1291, 2111, 1129, 1481, 1609, 2237, 3121, 3049, 1063, 1663, 1163, 1973, 2879, 2371, 3343, 3539, 2267, 2339, 1571, 3023, 3067, 3329, 2011, 1399, 3659, 1907]

edge_n = {}
for edge in edges:
	con = connected[edge]
	for c in con:
		if c in edges and edge not in corners:
			if edge not in edge_n:
				edge_n[edge] = []
			if c not in edge_n:
				edge_n[c] = []
			edge_n[edge].append(c)
			edge_n[c].append(edge)

def in_both(num1, num2):
	d = []
	for c in connected[num1]:
		if c in connected[num2]:
			d.append(c)
	return d

sol = [[1693,2803,3023,3067,1171,1163,1973,2879,1907,1609,1481,2207],
[1783,3559,2251,1709,3673,1613,1087,1439,1933,1091,2749,1123],
[1663,1987,3821,3191,2311,2791,3259,2843,1429,2837,3931,3433],
[1063,1187,1451,1847,2137,2377,2297,1997,1319,2423,2963,3049],
[3121,2069,1913,1019,2657,1511,1031,2801,1733,1307,3089,2237],
[1571,3623,1559,1567,2477,3347,1097,3271,2239,2663,3793,1039],
[2383,1747,3467,2999,1459,1193,1871,2027,3331,1093,1721,3041],
[2371,1999,2551,2707,3253,1201,2677,3061,1471,3407,3109,3637],
[3343,3739,3733,3769,2539,3929,3469,2903,1823,3671,2531,3329],
[1399,1249,2789,2521,2591,2753,1277,3499,3779,2767,3001,2011],
[2579,1223,3593,2819,1051,1951,3863,3697,2927,3557,1619,3539],
[2111,1361,1129,3659,2473,3119,2659,1499,2083,1291,2267,2339]]

def rotate_r90(arr):
	arr2 = ["" for j in range(10)]
	for i in range(10):
		for j in range(10):
			arr2[j] = arr[i][j] + arr2[j]
	return arr2

def flip(arr):
	arr2 = ["" for j in range(10)]
	for i in range(10):
		arr2[i] = arr[i][::-1]
	return arr2

def rotate_r90_sz(arr, sz):
	arr2 = ["" for j in range(sz)]
	for i in range(sz):
		for j in range(sz):
			arr2[j] = arr[i][j] + arr2[j]
	return arr2

def flip_sz(arr, sz):
	arr2 = ["" for j in range(sz)]
	for i in range(sz):
		arr2[i] = arr[i][::-1]
	return arr2

arr_border = [[["" for i in range(10)] for j in range(12)] for k in range(12)]
for i in range(12):
	for j in range(12):
		arr_border[i][j] = tiles[sol[i][j]]

def show_diagram(arr):
	for k in range(12):
		for i in range(10):
			row = ""
			for j in range(12):
				row = row + arr[k][j][i]
			print(row)

arr_border = [[['...####.#.', '#....#.#.#', '#..#.....#', '#.#....#..', '..........', '...#.....#', '#....#....', '.....#....', '#.....#.##', '..####...#'], ['.##..####.', '#.....#.#.', '##....####', '......#...', '.......#.#', '##........', '.....#...#', '.......#..', '#.........', '###...##..'], ['....#.##..', '...#....#.', '#......#..', '......#...', '#.........', '..........', '#.##.....#', '....#.####', '......#.#.', '.....##..#'], ['.##.....##', '..........', '..#.....#.', '.#...#..##', '..#....#.#', '.........#', '#...#.....', '##.#.....#', '.....#...#', '###..##..#'], ['###.##....', '.....#...#', '.#...#....', '#.....##..', '#..##..#.#', '#.##..#..#', '......#..#', '#..#..#..#', '#.....#...', '##..#####.'], ['..#.#....#', '#.........', '.....#...#', '.#.......#', '#...#..###', '#.......##', '#..#..###.', '#...#....#', '.........#', '.#.#.#....'], ['##..###.#.', '....#....#', '#.#.###..#', '#.#.##..##', '##....##..', '#......#.#', '..#.#.....', '#.....#...', '#....##..#', '.#.#..####'], ['.###...###', '#.....#...', '#........#', '#..#..#...', '....##...#', '#......#..', '.#.#......', '...#...#.#', '##..#..#.#', '#..#.#####'], ['###..#.##.', '.....##..#', '#......#..', '.#.......#', '#.#...#...', '........#.', '..#.....#.', '#..#....##', '###.#..#..', '##...#.#.#'], ['..#..###.#', '#..#......', '.....#....', '#....#.##.', '..........', '.....#...#', '.#..#.....', '#......#.#', '..#...#...', '##..###.##'], ['####.##.#.', '..........', '...#......', '..#.#.....', '.#..#....#', '#.#.......', '.#.#.#....', '#....#....', '..........', '#.#.##.#..'], ['.#.#.#.##.', '...#......', '..........', '.......#.#', '#.........', '........#.', '.#.#......', '....#....#', '..#...#...', '.#.#.#.#..']], [['..####...#', '#.#......#', '#.........', '#...#....#', '..........', '...##.....', '#.....#...', '#..#......', '.........#', '#.##..#.##'], ['###...##..', '#....#....', '.......#..', '##.....###', '..........', '..........', '........#.', '...#....#.', '#.#...#...', '#####.#.##'], ['.....##..#', '.....#....', '...#...#..', '#.#.####.#', '.....##...', '...#....#.', '.....#...#', '..#..#....', '....##..#.', '#.....###.'], ['###..##..#', '.#.......#', '..#..#..#.', '#.###...##', '......####', '.#..#..#.#', '#........#', '.....#....', '..#.#.....', '.#..##..##'], ['##..#####.', '#.......#.', '...#..#.#.', '###....#..', '#.........', '#.....##..', '#..#.#....', '.#........', '..##...#.#', '##..##....'], ['.#.#.#....', '........#.', '......#...', '..........', '....##....', '.....#..#.', '...##....#', '....##..##', '#...#..#.#', '.#....####'], ['.#.#..####', '..#...#..#', '...###.#.#', '.##.#....#', '...#.....#', '...#.#....', '##..#.....', '##.###..#.', '#.####.#.#', '##.....#..'], ['#..#.#####', '##..#..##.', '#.##....#.', '#...#..#..', '#.#.....##', '.#....#...', '..........', '.#.##.##.#', '###....##.', '..##....##'], ['##...#.#.#', '..#..#...#', '.##...##.#', '..#.......', '##.......#', '.#.......#', '..#.......', '##..#....#', '..#..#....', '#.#.####.#'], ['##..###.##', '#.....#..#', '#.##.....#', '..........', '#........#', '#..#......', '.........#', '#...#..#..', '.###....#.', '#...#.#..#'], ['#.#.##.#..', '#.....#...', '#.#.......', '.......#.#', '#.........', '..........', '#.........', '..#..#.###', '.##...##.#', '#....#.###'], ['.#.#.#.#..', '.......#.#', '..#...#..#', '#...#.....', '.#.#..#..#', '.........#', '....#...##', '#..#.....#', '#...#.#..#', '####.#...#']], [['#.##..#.##', '#.#......#', '#.........', '#......#.#', '.##..#....', '.......###', '#...#..#.#', '....#.....', '##..##...#', '###.#.####'], ['#####.#.##', '#.........', '.........#', '#..#.....#', '.#.#..#...', '##.###....', '#...#....#', '...#......', '#...#.....', '##.#.....#'], ['#.....###.', '..........', '#......#..', '##..#.....', '.##.#..###', '..##...###', '#...#....#', '...#.#....', '.....#....', '#.#.###.#.'], ['.#..##..##', '......#.##', '..#..##...', '.#...#...#', '#.#.##..##', '##.#..#..#', '#.........', '...#......', '......#..#', '.#...#....'], ['##..##....', '#.......##', '....#...#.', '#.........', '#......#.#', '#.........', '....#.#..#', '..#.....##', '##......##', '..##..#..#'], ['.#....####', '#.........', '...#......', '...##....#', '#.......##', '...#....##', '#.....#..#', '#........#', '#.#..#....', '##.###.#.#'], ['##.....#..', '...##...#.', '.#......#.', '##..#..#.#', '#.....#...', '##.....#.#', '#..#.....#', '#........#', '.........#', '#####.##.#'], ['..##....##', '.#.#..#...', '..#.#..#.#', '#.........', '....#.....', '#...#...##', '#.#.....#.', '#........#', '#...#...#.', '#.####....'], ['#.#.####.#', '.........#', '#...#....#', '..........', '...#.#....', '#.......#.', '.....###..', '##.#.##..#', '..##..##.#', '.#.###.#..'], ['#...#.#..#', '#.#.......', '##........', '.........#', '.#..#..#..', '..##.##.#.', '....##.#..', '#.........', '#...##...#', '....#.#.##'], ['#....#.###', '......#...', '......#..#', '#..###...#', '....#...#.', '.#.###.#..', '..##....#.', '....#....#', '#........#', '#..##...##'], ['####.#...#', '.....##..#', '#....#.###', '#..#...#.#', '......#...', '..#...#.#.', '...#.#....', '#..#..#..#', '#.#.##...#', '#.#....#..']], [['###.#.####', '#.....#..#', '.....#..##', '#..#.....#', '##..#.#...', '#.......#.', '#..#..#..#', '#...#.#.#.', '..........', '.#.#.#..#.'], ['##.#.....#', '#....#...#', '#.#..#....', '#.###.....', '.......#..', '...#......', '##........', '..........', '..........', '.#########'], ['#.#.###.#.', '#...#....#', '....#.....', '.........#', '....#..#..', '..........', '.#........', '........##', '.........#', '#...##..#.'], ['.#...#....', '#..##.....', '........#.', '#.......#.', '.#........', '..#......#', '...##.#..#', '####...##.', '##........', '..###...#.'], ['..##..#..#', '.#..#.....', '....#.....', '...###....', '...#...#.#', '#.#.#.....', '##..######', '...#.##..#', '..#.......', '....###.#.'], ['##.###.#.#', '...#.#.#.#', '......#.##', '....#...#.', '##.....#..', '.....#...#', '#.#...#.##', '##.#......', '....#..#.#', '..#.#.....'], ['#####.##.#', '##.#.....#', '#.........', '.......###', '.....#..##', '###.####..', '##........', '.......#.#', '#.##......', '..#.#.##..'], ['#.####....', '#..##.....', '.##..#.##.', '##....##..', '#.....#...', '..........', '.........#', '#..##.#..#', '....##...#', '.....#.##.'], ['.#.###.#..', '...#......', '...##.#...', '.##.##.#.#', '.#.......#', '.....#...#', '#.##......', '#......#..', '##.......#', '....###.##'], ['....#.#.##', '..........', '.#........', '#.#...#..#', '##..#....#', '#.......#.', '..##.....#', '..........', '#........#', '##.#..#..#'], ['#..##...##', '..........', '...#.#....', '#........#', '#.#....#..', '..#..#...#', '#....#...#', '......#..#', '#.......#.', '#.#.#.#..#'], ['#.#....#..', '.....#.###', '.......#.#', '#....#....', '.#..#.....', '#.........', '#.#..#...#', '##.#.#...#', '....#.....', '#..#...#..']], [['.#.#.#..#.', '...#..##..', '#........#', '.#...#..##', '#.#.......', '.....#....', '..#.#....#', '#.....#..#', '#..###...#', '.#####....'], ['.#########', '.#.......#', '#.#......#', '#........#', '..#.#....#', '.........#', '#........#', '#......##.', '#.#..##..#', '.....####.'], ['#...##..#.', '#.........', '#........#', '###.#.....', '#.#......#', '###.......', '#.#.......', '....#....#', '##...#....', '.#....#...'], ['..###...#.', '.......#.#', '#.........', '..#...#..#', '##..#..#..', '.###....##', '..#.......', '#.#.......', '.##.......', '..#####..#'], ['....###.#.', '#..#..#..#', '......#...', '#...#.....', '.##..#..##', '##....##..', '.#....#...', '.##..#...#', '.........#', '##..#....#'], ['..#.#.....', '#........#', '.##...#.##', '..........', '#..#.#..##', '.##.#...##', '.#.......#', '##.#..#...', '#........#', '#.##..#.#.'], ['..#.#.##..', '#.#.#....#', '#.......##', '......#..#', '##...#...#', '#....#....', '#..#......', '..##.#....', '#........#', '..#....###'], ['.....#.##.', '#.........', '#........#', '#..#.#...#', '#..#...##.', '.....#.#..', '.........#', '...#..##.#', '#...#.....', '#.#.##...#'], ['....###.##', '......#.#.', '#..#......', '#.#.......', '.......#..', '...#.....#', '###.......', '#...#..##.', '.......###', '#.#.###...'], ['##.#..#..#', '...##.....', '........##', '.......#..', '.#...#..#.', '#....#...#', '........#.', '.##..#..#.', '##..####.#', '.#...###.#'], ['#.#.#.#..#', '.........#', '#.........', '..........', '........#.', '#.....#..#', '......#...', '...#.##..#', '#...##....', '##........'], ['#..#...#..', '#..#.#....', '....##...#', '..#.......', '...#..#..#', '#.....#..#', '....#....#', '##...##..#', '..#.....#.', '.#....#.##']], [['.#####....', '#........#', '#.....#..#', '#..###...#', '#.#.#.#..#', '#....###..', '#.........', '##..#.....', '..........', '##..####.#'], ['.....####.', '#...#.#...', '##..#.##..', '#.##....#.', '#.#..#.#.#', '.#.......#', '.....#...#', '.....#...#', '.........#', '##.###...#'], ['.#....#...', '.........#', '..#.###...', '.#....##.#', '#.#....#..', '##..#.#.##', '#........#', '#.#.....##', '#....#...#', '#..#.##.#.'], ['..#####..#', '#..##.....', '..........', '#.....##.#', '.#..#.##.#', '##..#.#...', '###...#...', '#.#.#.##..', '#....#....', '.#.#.#.#.#'], ['##..#....#', '........#.', '.........#', '#.....###.', '##....##..', '.#........', '.#..#.....', '....#.....', '...#......', '##.#######'], ['#.##..#.#.', '.#.#.#...#', '##..#..#..', '.....##..#', '.....#...#', '....#.....', '.......#..', '..........', '..#...#...', '##..##.#.#'], ['..#....###', '#..#.#....', '..#..#..#.', '#..####.#.', '#........#', '.......#..', '...#.....#', '..#.#.#..#', '..........', '##...#.###'], ['#.#.##...#', '..###.....', '.......##.', '.###...#.#', '#...#....#', '.......#..', '##...#...#', '#.........', '..........', '##.#.#.#.#'], ['#.#.###...', '...#....##', '......#.##', '#........#', '#.....#..#', '..........', '##.#.#....', '........##', '.#........', '#.#####.#.'], ['.#...###.#', '#.........', '#...#.....', '#....#...#', '#..#...#.#', '.....#....', '......#...', '#..#.....#', '..........', '..#.##....'], ['##........', '...#.#...#', '..........', '#.#......#', '#......###', '..#...#..#', '..........', '#.#.#...#.', '.#.##...##', '...##..##.'], ['.#....#.##', '#....#....', '..........', '#.#...#..#', '#........#', '#.....#..#', '.###..#..#', '.........#', '#.......##', '..#.####..']], [['##..####.#', '#.....#...', '####...#.#', '#.....#..#', '#.........', '.......#..', '...#......', '#........#', '..........', '###...#..#'], ['##.###...#', '.#........', '#....##...', '#..###....', '.#..#.#.##', '........#.', '..#.......', '#....##.#.', '..###...#.', '##..#.#..#'], ['#..#.##.#.', '....##...#', '.#.##..#.#', '..##...###', '#.#..#.#.#', '....#.....', '..........', '..##..#...', '.##....###', '#.#..####.'], ['.#.#.#.#.#', '#...#.#..#', '#.#..#...#', '##.#..#...', '#.#..#....', '.#.......#', '.......#.#', '.#..##....', '#....#....', '.#...##.#.'], ['##.#######', '#.#...##..', '##.....#.#', '..##.#..#.', '.....#.#..', '##..#..#.#', '####.#..#.', '..##.#...#', '......#..#', '...#.##..#'], ['##..##.#.#', '...#..#.##', '#...#.#..#', '........##', '.......##.', '###..#..#.', '.#....##..', '#.#...#..#', '#......###', '##.#.#..##'], ['##...#.###', '#......#.#', '#...#.#.##', '#........#', '.#.......#', '...#...#.#', '....#.....', '#.........', '#.........', '####.##..#'], ['##.#.#.#.#', '#...#.##.#', '####....##', '#.#......#', '#..#...#..', '#.........', '.....#.##.', '........##', '......#.#.', '#####..###'], ['#.#####.#.', '#.#..#.###', '##....###.', '#.........', '.........#', '..#..#..##', '.#....##.#', '#...#....#', '..........', '##..##.###'], ['..#.##....', '#..#.#####', '..#.##.#..', '........##', '#...#.....', '##.##.#...', '##..##....', '#.....#..#', '.........#', '#...##..##'], ['...##..##.', '#....#....', '..#.#.#...', '#..#...#..', '..........', '.##...#..#', '..##.#.#..', '#.....##.#', '#..#...#.#', '###.#.#.##'], ['..#.####..', '........##', '..#.###..#', '........#.', '.........#', '#..#.#....', '....#..#.#', '#..#.#...#', '#...#.#..#', '##...#...#']], [['###...#..#', '#.#..#....', '..........', '#..##.....', '#...#....#', '#.....#..#', '......#.#.', '#...#....#', '#.#......#', '.##.#....#'], ['##..#.#..#', '...##.#..#', '..#......#', '.........#', '#......#..', '#....#.#..', '......#..#', '#...#....#', '#.........', '#...#..#..'], ['#.#..####.', '##.##.#..#', '##.##.#...', '#...#.....', '....#.#..#', '....#..##.', '#....###..', '##.......#', '.###......', '...#......'], ['.#...##.#.', '#..#.....#', '..#.......', '.#....#.##', '##........', '.#.......#', '.#..##...#', '#..#.....#', '...#...#.#', '.##...##.#'], ['...#.##..#', '###.......', '........#.', '#........#', '..........', '##....#...', '#.......##', '#.......##', '#......#.#', '#.########'], ['##.#.#..##', '..##.....#', '.#....#...', '#..#...#.#', '.....#.#..', '..##..#..#', '###...###.', '##...#....', '##.#.....#', '###.......'], ['####.##..#', '##.#.....#', '..#......#', '#.....#.##', '...##.....', '##..#..#..', '.#..###...', '..........', '#.#.#....#', '...#....##'], ['#####..###', '#..#....#.', '##.#......', '#....#...#', '.....#...#', '..#...#...', '.#.##.....', '..#......#', '#..#......', '##....##.#'], ['##..##.###', '......#...', '......#...', '#.##.##..#', '#...#..##.', '...#.#..##', '.........#', '#.........', '..#.#..#..', '#.###.....'], ['#...##..##', '....#..##.', '........##', '#.#....#..', '.....#.#.#', '##.......#', '#.......#.', '...#....#.', '.#.......#', '..####.##.'], ['###.#.#.##', '.......###', '#.....#..#', '.........#', '##.......#', '#....#...#', '...#......', '......##..', '##....#..#', '..#..##...'], ['##...#...#', '#.##.....#', '#........#', '##........', '#.#.......', '##....#..#', '....##...#', '.#.....#.#', '#.........', '.#.......#']], [['.##.#....#', '#.........', '#..#.....#', '.#.......#', '#........#', '#.........', '..#.#.....', '.......##.', '...#.....#', '..###....#'], ['#...#..#..', '....#..#.#', '##....##.#', '#..#..##..', '#.#.......', '....#.#...', '...###..##', '...#......', '#..#....##', '###..#.###'], ['...#......', '#.........', '#..#......', '...#...#.#', '.##.....#.', '.........#', '#.......##', '...#......', '#........#', '##..###..#'], ['.##...##.#', '.#...#...#', '.........#', '#........#', '......#..#', '#.#.#.#...', '#...#...#.', '.........#', '#...#.....', '#...#.#...'], ['#.########', '#......###', '#......#.#', '#...###..#', '#....#..#.', '.#.....###', '.#...#....', '###.......', '.........#', '.####.####'], ['###.......', '#.........', '#.#..#..#.', '#..###....', '..........', '#.#.......', '.........#', '..#..#....', '#........#', '###..#..##'], ['...#....##', '...##..#..', '...#..#...', '.##....#.#', '.........#', '.........#', '#...#.....', '.......#..', '#...#.....', '##.######.'], ['##....##.#', '.#.......#', '.#..#.....', '#...#.###.', '#..#.#.##.', '#.........', '......#...', '.#.....#.#', '.....#...#', '.#......##'], ['#.###.....', '#...##....', '.#..#..#..', '.....#####', '.#.......#', '..........', '.#.##.....', '#.#.......', '###.#..#.#', '##..#..#..'], ['..####.##.', '...#....#.', '..#..####.', '#..####...', '#.#.#....#', '.....#.#..', '..#.#.....', '...#.....#', '#.##.#..##', '.....#.#.#'], ['..#..##...', '..#..#...#', '.....#....', '.#..#..#.#', '#..#..#.#.', '........##', '.......#.#', '###.....##', '#..##.#...', '##...#####'], ['.#.......#', '#.###....#', '...#.....#', '#........#', '.#........', '#........#', '#.#......#', '#....#..##', '....#.....', '#.####...#']], [['..###....#', '.##.....#.', '...#.....#', '..........', '##..#....#', '.#.#....#.', '#.#.#....#', '...#.....#', '...##.....', '#.##.###.#'], ['###..#.###', '..........', '##..##...#', '.#.......#', '#...##.#.#', '.###.....#', '#.....#...', '#..#.....#', '.#....####', '#..###...#'], ['##..###..#', '.......#.#', '#.....#...', '#.....#...', '#..#...##.', '#....###.#', '.#....#...', '#...#..#..', '#.....#.##', '#.#.#..##.'], ['#...#.#...', '##.......#', '..##..#...', '..#.......', '...#.##..#', '#...##.#.#', '.#........', '..#......#', '#.......#.', '.#.....#..'], ['.####.####', '##......#.', '...#.....#', '..........', '###.#..#.#', '#.###...#.', '.........#', '#...#....#', '.........#', '...#...#.#'], ['###..#..##', '...#...#.#', '#....#....', '.......###', '#.##......', '....#.....', '#...##....', '#........#', '#..#.#.#..', '##.#.#...#'], ['##.######.', '#..#......', '..........', '#.........', '..#..#...#', '..#.......', '.#.#.....#', '##.......#', '....#....#', '#...###.#.'], ['.#......##', '...#......', '.........#', '.........#', '#......#..', '......#..#', '####.#..#.', '#...#.....', '#......###', '....#.####'], ['##..#..#..', '...####..#', '#..#.##...', '#.........', '.....#....', '#...#...#.', '.#.##.....', '.#..##...#', '#....#.#.#', '#.#...#..#'], ['.....#.#.#', '#..##..#.#', '.....#...#', '...#......', '..........', '..#.#.....', '....#.##..', '#...#.....', '#......#..', '#.##.##..#'], ['##...#####', '###.#..#.#', '#.....#...', '....#....#', '..#.....##', '.#.....##.', '....#..#.#', '.#...#....', '.........#', '#.##.#.#..'], ['#.####...#', '##....##.#', '..#.......', '#...#....#', '#......#.#', '........##', '#......#.#', '.#.#..#...', '#.......##', '..#.#####.']], [['#.##.###.#', '#.#.#....#', '#.........', '##........', '#........#', '#.........', '.##.......', '..#.......', '#.....#..#', '##.#..##..'], ['#..###...#', '##...#...#', '.........#', '.........#', '#...##..##', '....#.#..#', '..##...#..', '...##.##.#', '#...##...#', '..########'], ['#.#.#..##.', '#......#.#', '#......#..', '#.........', '##........', '#.#...#..#', '.#.......#', '#.#.....#.', '#..##.....', '#..###.#.#'], ['.#.....#..', '#.........', '..#.......', '........#.', '....##...#', '#.........', '##........', '...#...#..', '.........#', '#####....#'], ['...#...#.#', '..........', '.........#', '..#....#.#', '#.#####.#.', '...#.#...#', '..##...#.#', '......#.#.', '#........#', '##..##.##.'], ['##.#.#...#', '..........', '#.##.....#', '#.#..##.#.', '...##...#.', '#....#...#', '#.......#.', '....#....#', '#...##..#.', '....##.#.#'], ['#...###.#.', '......#...', '#..#..#.#.', '..##..#..#', '.##..#.#..', '##.#......', '.....#..##', '#.#......#', '.........#', '##.##.....'], ['....#.####', '.#.....##.', '....#....#', '#..#.#....', '...#.....#', '.#......##', '##.......#', '#......#.#', '#........#', '..#...##.#'], ['#.#...#..#', '...#..#..#', '#...#.##..', '...###...#', '#.#.#...##', '#..#......', '#.........', '##....##..', '#......#..', '#######..#'], ['#.##.##..#', '#..##.#...', '.#..#..##.', '#####.#.#.', '##.....###', '....#..#.#', '....#.#...', '..#......#', '..#..##.#.', '###.#.#...'], ['#.##.#.#..', '....#.....', '..#.##..##', '.#..###..#', '##..#.#..#', '#......#..', '........#.', '##.....##.', '...##.#...', '.##..###..'], ['..#.#####.', '....##..##', '#.........', '#.#.......', '#.........', '.#..#.....', '.#.#..#.##', '.#.....#.#', '.#....#...', '.#...#...#']], [['##.#..##..', '.#...#...#', '.......#.#', '#.........', '.....#...#', '#.........', '#..#...#.#', '...#.....#', '###.#....#', '###.#...#.'], ['..########', '#.....#...', '#....#....', '.........#', '#....#..#.', '...#.....#', '##....#...', '#.........', '##..#....#', '..##.##...'], ['#..###.#.#', '....#..#..', '......#..#', '#.##.....#', '....##....', '###.......', '......#.#.', '....#...#.', '#.#...#...', '..####..##'], ['#####....#', '..#.......', '#.......##', '#...#....#', '.....#....', '.........#', '....#..#..', '.......#.#', '....#...##', '#.....#..#'], ['##..##.##.', '..#......#', '#........#', '#.#.#..#.#', '...#..#..#', '#........#', '......##..', '#....#.#..', '##.#......', '##.#.###.#'], ['....##.#.#', '#........#', '#.....#...', '#..#..##.#', '#..#...###', '#.#.###...', '..#......#', '...#.#.#.#', '..#..#...#', '##...#..##'], ['##.##.....', '#....#...#', '.......#.#', '#...#.#..#', '##..#.#...', '.....##..#', '#.#......#', '##........', '#..#...#..', '###.###.##'], ['..#...##.#', '#.......#.', '#........#', '##.......#', '.......#..', '#..#.....#', '#......#..', '.#......#.', '..........', '#.#..#..#.'], ['#######..#', '.##....##.', '#....#.###', '#.......#.', '..........', '#..##.##.#', '.#.....###', '...##...#.', '....#.....', '..####....'], ['###.#.#...', '.#....####', '##.......#', '.##.#.####', '......#...', '#.........', '##........', '.......#..', '.......###', '..###.##.#'], ['.##..###..', '##..##....', '#..#.##..#', '##..#.....', '.##.....#.', '.#.......#', '..#..#...#', '..#...####', '#..#.##...', '##.##..##.'], ['.#...#...#', '..#.#....#', '##......##', '...##.....', '..........', '#.....#...', '#.#.###..#', '#.#.....#.', '.........#', '.......#.#']]]

def fix(arr_border, i, j):
	if arr_border[i][j][0] == arr_border[i-1][j][9]:
		return None
	else:
		#try rotating
		for k in range(4):
			arr_border[i][j] = rotate_r90(arr_border[i][j])
			if arr_border[i][j][0] == arr_border[i-1][j][9]:
				return None 
		#try flip rotate
		arr_border[i][j] = flip(arr_border[i][j])
		for k in range(4):
			arr_border[i][j] = rotate_r90(arr_border[i][j])
			if arr_border[i][j][0] == arr_border[i-1][j][9]:
				return None 
		arr_border[i][j] = flip(arr_border[i][j])
		print("failed")
		return None

def fix_two(arr_border, i, j):
	if arr_border[i][j][9] == arr_border[i+1][j][0]:
		return None
	else:
		#try rotating
		for k in range(4):
			arr_border[i][j] = rotate_r90(arr_border[i][j])
			for m in range(4):
				arr_border[i+1][j] = rotate_r90(arr_border[i+1][j])
				if arr_border[i][j][9] == arr_border[i+1][j][0]:
					return None 

		#try flip rotate
		arr_border[i][j] = flip(arr_border[i][j])
		for k in range(4):
			arr_border[i][j] = rotate_r90(arr_border[i][j])
			for m in range(4):
				arr_border[i+1][j] = rotate_r90(arr_border[i+1][j])
				if arr_border[i][j][9] == arr_border[i+1][j][0]:
					return None 
		arr_border[i][j] = flip(arr_border[i][j])
		print("failed")
		return None

def fix_col(arr_border, j):
	for i in range(1, 12):
		fix(arr_border, i, j)

def flip_col(arr_border, j):
	for i in range(0, 12):
		arr_border[i][j] = flip(arr_border[i][j])

arr_no_border = [[["" for i in range(8)] for j in range(12)] for k in range(12)]

for i in range(12):
	for j in range(12):
		for k in range(1, 9):
			arr_no_border[i][j][k-1] = arr_border[i][j][k][1:9]

complete_arr = []

for i in range(12):
	for j in range(8):
		str1 = ""
		for k in range(12):
			str1 = str1 + arr_no_border[i][k][j]
		complete_arr.append(str1)

def calc_roughness(arr):
	monsters = 0
	for i in range(len(arr) - 3):
		for j in range(len(arr[0]) - 20):
			i_vals = [0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]
			j_vals = [18, 0, 5, 6, 11, 12, 17, 18, 19, 1, 4, 7, 10, 13, 16]
			hashtags = 0
			for k in range(len(i_vals)):
				if arr[i + i_vals[k]][j + j_vals[k]] == "#":
					is_hashtag = True
					hashtags += 1
				else:
					is_hashtag = False
				
			print(i, j, hashtags)
			if hashtags == 15:
				monsters += 1
	print("monsters:", monsters)
	count_hashtag = 0
	for i in range(len(arr)):
		for j in range(len(arr[0])):
			if arr[i][j] == "#":
				count_hashtag += 1

	print("roughness: ", count_hashtag - (15 * monsters))






#print(tiles)
