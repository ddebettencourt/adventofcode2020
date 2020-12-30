data = open("C:\\Users\\djdeb\\Desktop\\Random Stuff\\Advent of Code 2020\\day25input.txt")
str1 = data.read()
puzzle_array = str1.splitlines()

card_loop = int(puzzle_array[0])
door_loop = int(puzzle_array[1])



def loop(val, x):
	cur = 1
	for i in range(x):
		cur = val * cur
		cur %= 20201227
		if cur == card_loop:
			print(i, "card loop")
		if cur == door_loop:
			print(i, "door loop")
	return cur

vals = set()
real_x = 0
real_y = 0
for i in range(100):
	x = loop(card_loop, i)
	y = loop(door_loop, i)
	if x not in vals:
		vals.add(x)
	else:
		#print(i, "x", "here")
		real_x = i
	if y not in vals:
		vals.add(y)
	else:
		#print(i, "y", "here")
		real_y = i
	#print(1, x)
	#print(2, y)

print(real_x, real_y)