data = open("C:\\Users\\djdeb\\Desktop\\Random Stuff\\Advent of Code 2020\\day13input.txt")
str = data.read()
puzzle_array = str.splitlines()

buses = [17, 37, 907, 19, 23, 29, 653, 41, 13]
offsets = [0, 11, 17, 29, 40, 46, 48, 58, 61]

for bus in buses:
	print((1000186 // bus) * bus + bus)
	print((1000186 // bus) * bus + bus - 1000186)

#bus_list = puzzle_array[1].split(",")
#for i in range(len(bus_list)):
#	print(bus_list[i], i)

# 17, 11 mod 37, 17 mod 907, 10 mod 19, 17 mod 23, 17 mod 29, 48 mod 653, 17 mod 41, 9 mod 13

x = 890
while x % 653 != 605:
	x += 907
print(x)

x = 86148
while x % 17 != 0:
	x += 592271
print(x)

x = 678419
while x % 37 != 26 or x % 19 != 9 or x % 23 != 6:
	x += (592271 * 17)
print(x)

x = 25373568059
while x % 29 != 12 or x % 41 != 24 or x % 13 != 4:
	x += (592271 * 17 * 37 * 19 * 23)
print(x)

for i in buses:
	print(1674202695331513 % i)