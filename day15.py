data = open("C:\\Users\\djdeb\\Desktop\\Random Stuff\\Advent of Code 2020\\day15input.txt")
str = data.read()
puzzle_array = str.splitlines()

ls = [0 for i in range(2020)]

ls[0] = 16
ls[1] = 12
ls[2] = 1
ls[3] = 0
ls[4] = 15
ls[5] = 7
ls[6] = 11
ls[0:6] = [16, 12, 1, 0, 15, 7, 11]

dt = {} 

dt[16] = 0
dt[12] = 1
dt[1] = 2
dt[0] = 3
dt[15] = 4
dt[7] = 5

'''
ls[0] = 1
ls[1] = 2
ls[2] = 3
'''
'''
for i in range(7, 2020):
	ls2 = []
	for j in range(0, i-1):
		if ls[j] == ls[i-1]:
			ls2.append(j)
	if len(ls2) == 0:
		ls[i] = 0
	else:
		ls[i] = (i-1) - max(ls2)

print(ls[2019]) 
'''
last_num = 11
for i in range(7, 30000001):
	if last_num in dt:
		num = (i - 1) - dt[last_num]
		if i % 1000000 == 999999:
			print(i, num)
		
		dt[last_num] = i - 1
		last_num = num
	else:
		num = 0
		dt[last_num] = i - 1
		last_num = 0