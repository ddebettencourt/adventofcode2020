data = open("C:\\Users\\djdeb\\Desktop\\Random Stuff\\Advent of Code 2020\\day6input.txt")
str = data.read()
puzzle_array = str.splitlines()
#print(puzzle_array)
alphabet = [0 for i in range(26)]
total_count = 0
num = 0
for line in puzzle_array:
	if line == "":
		print(alphabet)
		total_count += sum([a for a in alphabet if a == num])//num
		alphabet = [0 for i in range(26)]
		num = 0
	else:
		num += 1
		for char in line:
			alphabet[ord(char) - 97] += 1
			if alphabet[ord(char) - 97] == 0:
				alphabet[ord(char) - 97] = 1
#total_count += sum(alphabet)
print(total_count)

