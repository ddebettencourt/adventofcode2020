data = open("C:\\Users\\djdeb\\Desktop\\Random Stuff\\Advent of Code 2020\\day10input.txt")
str = data.read()
puzzle_array = str.splitlines()

for i in range(len(puzzle_array)):
	puzzle_array[i] = int(puzzle_array[i])

puzzle_array.sort()
count1 = 0
count3 = 0
gap_arr = [1]
for i in range(len(puzzle_array) - 1):
	if puzzle_array[i+1] - puzzle_array[i] == 1:
		count1 += 1
		gap_arr.append(1)
	elif puzzle_array[i+1] - puzzle_array[i] == 3:
		count3 += 1
		gap_arr.append(3)
gap_arr.append(3)
print(count1, count3)
print(gap_arr)