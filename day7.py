data = open("C:\\Users\\djdeb\\Desktop\\Random Stuff\\Advent of Code 2020\\day7input.txt")
str = data.read()
puzzle_array = str.splitlines()

bag_types = {}
contain_shiny = 0
for line in puzzle_array:
	bags = line.split("contain")
	bags_to_contain = bags[1].split(",")
	bag_types[bags[0]] = bags_to_contain

def has_shiny(bag, bag_types):
	for bag2 in bag_types[bag]:
		if "shiny gold" in bag2:
			return True
		elif (bag2.split()[1] + " " + bag2.split()[2] + " bags ") in bag_types and has_shiny(bag2.split()[1] + " " + bag2.split()[2] + " bags ", bag_types):
			return True
	return False

for bag in bag_types:
	if has_shiny(bag, bag_types):
		#print(bag)
		contain_shiny += 1

def count_inside(bag, bag_types):
	sum_bags = 0
	for bag2 in bag_types[bag]:
		if not (bag2.split()[0] == "no") and (bag2.split()[1] + " " + bag2.split()[2] + " bags ") in bag_types:
			sum_bags += int(bag2.split()[0]) + int(bag2.split()[0]) * int(count_inside(bag2.split()[1] + " " + bag2.split()[2] + " bags ", bag_types))
	return sum_bags

print(count_inside("shiny gold bags ", bag_types))
#print(contain_shiny)


