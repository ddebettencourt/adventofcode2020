data = open("C:\\Users\\djdeb\\Desktop\\Random Stuff\\Advent of Code 2020\\day23input.txt")
str1 = data.read()
puzzle_array = str1.splitlines()


def part1():
	pa = [6, 5, 3, 4, 2, 7, 9, 1, 8]
	#pa = [3, 8, 9, 1, 2, 5, 4, 6, 7]
	pos = 0

	for i in range(100):
		pickup = [(pos + 1) % 9, (pos + 2) % 9, (pos + 3) % 9]
		pickup2 = [pa[pickup[0]], pa[pickup[1]], pa[pickup[2]]]
		found = False
		x = 2
		dist = 0
		while found == False:
			for j in range(len(pa)):
				if pa[j] == ((pa[pos] - x) % 9) + 1:
					dest = j
					if pa[j] not in pickup2:
						found = True
						dist = (j - pos) % 9
			x += 1
		for j in range(dist - 3):
			temp = pa[(j+pos+4) % 9]
			pa[(j+pos+4) % 9] = pa[(j+pos+3) % 9]
			pa[(j+pos+3) % 9] = pa[(j+pos+2) % 9]
			pa[(j+pos+2) % 9] = pa[(j+pos+1) % 9]
			pa[(j+pos+1) % 9] = temp
			
		pos += 1
		pos = pos % 9
		print(i, pa)

	print(pa)

class Node:
	empty = {}
	def __init__(self, value, prev=empty, rest=empty):
		self.value = value
		self.prev = prev
		self.rest = rest

dt = {}
pa = [6, 5, 3, 4, 2, 7, 9, 1, 8]
#pa = [3, 8, 9, 1, 2, 5, 4, 6, 7]
first = Node(pa[0])
dt[pa[0]] = first
for i in range(1,9):
	first.rest = Node(pa[i], prev=first)
	first = first.rest
	dt[pa[i]] = first

for i in range(10, 1000001):
	first.rest = Node(i, prev=first)
	first = first.rest
	dt[i] = first

dt[1000000].rest = dt[pa[0]]
cur_pos = dt[pa[0]]
for i in range(10000000):
	if i % 100000 == 0:
		print(i)
	cup1 = cur_pos.rest
	cup2 = cur_pos.rest.rest
	cup3 = cur_pos.rest.rest.rest
	cup4 = cur_pos.rest.rest.rest.rest

	num = (cur_pos.value - 2) % 1000000 + 1
	found = False
	while found == False:
		if cup1.value != num and cup2.value != num and cup3.value != num:
			found = True
		else:
			num -= 1
			if num == 0:
				num = 1000000
	dest = dt[num]
	cur_pos.rest = cup4
	temp = dest.rest
	dest.rest = cup1
	cup3.rest = temp
	cur_pos = cur_pos.rest

print(dt[1].rest.value, dt[1].rest.rest.value)









