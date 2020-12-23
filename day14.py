data = open("C:\\Users\\djdeb\\Desktop\\Random Stuff\\Advent of Code 2020\\day14input.txt")
str = data.read()
puzzle_array = str.splitlines()

def part1():
	vals = [0 for i in range(100000)]
	j = 0
	mask = ""
	while j < len(puzzle_array):
		if "mask" in puzzle_array[j]:
			mask = puzzle_array[j][7:]
		else:
			spot = puzzle_array[j][4:].split("]")[0]
			#print(spot)
			val = puzzle_array[j].split()[2]
			bin_val = bin(int(val))
			real_val = 0
			for i in range(36):
				#print(i, len(bin_val), bin_val)
				if len(bin_val) - 2 <= (35 - i) and mask[i] == "X":
					None
				elif mask[i] == "X":
					real_val += (2 ** (35 - i)) * int(bin_val[len(bin_val) - (35-i) - 1])
				elif mask[i] == "1":
					real_val += (2 ** (35 - i))
				elif mask[i] == "0":
					real_val += 0
			vals[int(spot)] = real_val
		j += 1

	print(sum(vals))

def write(spot, vals, val):
	vals[int(spot)] = val

vals = {}
j = 0
while j < len(puzzle_array):
	if "mask" in puzzle_array[j]:
		mask = puzzle_array[j][7:]
	else:
		spot = int(puzzle_array[j][4:].split("]")[0])
		val = int(puzzle_array[j].split()[2])
		bin_val = bin(val)
		arr_36 = [0 for i in range(36)]
		possible_vals = []
		bin_val = bin_val[2:]
		for i in range(36-len(bin_val)):
			bin_val = "0" + bin_val
		#print(bin_val)
		vals_2 = []
		for i in range(36):
			if mask[i] == "X":
				arr_36[i] == 2
				vals_2.append(35 - i)
			elif mask[i] == "1":
				arr_36[i] == 1
			elif mask[i] == "0":
				arr_36[i] == int(bin_val[i])

		#print(arr_36)
		spot_bin = bin(spot)[2:]
		for i in range(36-len(spot_bin)):
			spot_bin = "0" + spot_bin
		possible_vals = [0 for i in range(2 ** len(vals_2))]
		for i in range(36):
			if mask[i] == "1" or mask[i] == "0" and spot_bin[i] == "1":
				for k in range(len(possible_vals)):
					possible_vals[k] += (2 ** (35 - i))

		for i in range(len(possible_vals)):
			bin_i = bin(i)
			bin_i = bin_i[2:]
			for m in range(len(vals_2) - len(bin_i)):
				bin_i = "0" + bin_i
			#print(bin_i)
			for m in range(len(bin_i)):
				if bin_i[m] == "1":
					possible_vals[i] += (2 ** vals_2[m])
		#print(possible_vals, vals_2)
		for v in possible_vals:
			write(v, vals, val)
	j += 1

sum_vals = 0
for val in vals:
	sum_vals += vals[val]

print(sum_vals)

