data = open("C:\\Users\\djdeb\\Desktop\\Random Stuff\\Advent of Code 2020\\day5input.txt")
str = data.read()
puzzle_array = str.splitlines()

highest_ID = 0
IDs = []
for ID in puzzle_array:
	real_ID1 = 0
	real_ID2 = 0
	for i in range(len(ID)):
		#print(len(ID))
		if i < 7:
			if ID[i] == "B":
				real_ID1 += (2 ** (6 - i))
		else:
			if ID[i] == "R":
				real_ID2 += (2 ** (9 - i))
	IDs.append((real_ID1 * 8) + real_ID2)
print(max(IDs)) 
for i in IDs:
	i = int(i)
for i in range(0, 1000):
	if i not in IDs:
		print(i)



