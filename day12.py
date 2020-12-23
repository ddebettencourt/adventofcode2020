data = open("C:\\Users\\djdeb\\Desktop\\Random Stuff\\Advent of Code 2020\\day12input.txt")
str = data.read()
puzzle_array = str.splitlines()

def part_1():
	east = 0
	north = 0
	direc = 90
	for line in puzzle_array:
		if "N" in line:
			north += int(line[1:])
		elif "S" in line:
			north -= int(line[1:])
		elif "E" in line:
			east += int(line[1:])
		elif "W" in line:
			east -= int(line[1:])
		elif "L" in line:
			direc -= int(line[1:])
		elif "R" in line:
			direc += int(line[1:])
		elif "F" in line:
			if direc == 0:
				north += int(line[1:])
			elif direc == 90:
				east += int(line[1:])
			elif direc == 180:
				north -= int(line[1:])
			elif direc == 270:
				east -= int(line[1:])
		direc = direc % 360

def rotate(deg, a, b):
	deg = deg % 360
	if deg == 90:
		return [b, a * -1]
	elif deg == 180:
		return [a * -1, b * -1]
	elif deg == 270:
		return [b * -1, a]

east = 0
north = 0
w_e = 10
w_n = 1
direc = 90
w_d = 0
for line in puzzle_array:
	if "N" in line:
		w_n += int(line[1:])
	elif "S" in line:
		w_n -= int(line[1:])
	elif "E" in line:
		w_e += int(line[1:])
	elif "W" in line:
		w_e -= int(line[1:])
	elif "L" in line:
		arr = rotate(-1 * int(line[1:]), w_e, w_n)
		w_e = arr[0]
		w_n = arr[1]
	elif "R" in line:
		arr = rotate(1 * int(line[1:]), w_e, w_n)
		w_e = arr[0]
		w_n = arr[1]
	elif "F" in line:
		north += w_n * int(line[1:])
		east += w_e * int(line[1:])
	direc = direc % 360


print(east, north)


