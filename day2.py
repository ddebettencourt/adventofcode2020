
data = open("C:\\Users\\djdeb\\Desktop\\Random Stuff\\Advent of Code 2020\\day2input.txt")
str = data.read()
puzzle_array = str.splitlines()

valid_passwords = 0
for line in puzzle_array:
	split = line.split()
	split2 = split[0].split("-")
	min_letter = split2[0]
	max_letter = split2[1]
	letter = split[1][0]
	password = split[2]
	count = 0
	for i in range(len(password)):
		if password[i] == letter:
			count += 1
	if count >= int(min_letter) and count <= int(max_letter):
		valid_passwords += 1
print(valid_passwords)

valid_passwords = 0
for line in puzzle_array:
	split = line.split()
	split2 = split[0].split("-")
	min_letter = split2[0]
	max_letter = split2[1]
	letter = split[1][0]
	password = split[2]
	count = 0
	#print(password, min_letter, max_letter, len(password))
	if password[int(min_letter) - 1] == letter:
		count += 1
	if password[int(max_letter) - 1] == letter:
		count += 1 
	if count == 1:
		valid_passwords += 1
print(valid_passwords)

