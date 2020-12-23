data = open("C:\\Users\\djdeb\\Desktop\\Random Stuff\\Advent of Code 2020\\day4input.txt")
str = data.read()
puzzle_array = str.splitlines()

valid = 0
end = True
categories = 0
has_cid = False
byr_valid = False
iyr_valid = False
eyr_valid = False
hgt_valid = False
hcl_valid = False
ecl_valid = False
pid_valid = False

for i in range(len(puzzle_array)):
	if puzzle_array[i] == "":
		end = True
		if categories >= 8 or (categories == 7 and not has_cid):
			if byr_valid and iyr_valid and eyr_valid and hgt_valid and hcl_valid and ecl_valid and pid_valid:
				valid += 1
		print(byr_valid, iyr_valid, eyr_valid, hgt_valid, hcl_valid, ecl_valid, pid_valid)
		has_cid = False
		byr_valid = False
		iyr_valid = False
		eyr_valid = False
		hgt_valid = False
		hcl_valid = False
		ecl_valid = False
		pid_valid = False
		categories = 0
	else:
		end = False
	categories += len(puzzle_array[i].split())
	
	if "cid" in puzzle_array[i]:
		has_cid = True
	for value in puzzle_array[i].split():
		if "byr" in value:
			if int(value[4:]) <= 2002 and int(value[4:]) >= 1920:
				byr_valid = True
		if "iyr" in value:
			if int(value[4:]) <= 2020 and int(value[4:]) >= 2010:
				iyr_valid = True
		if "eyr" in value:
			if int(value[4:]) <= 2030 and int(value[4:]) >= 2020:
				eyr_valid = True
		if "hgt" in value:
			try:
				if "cm" in value:
					if int(value[4:7]) >= 150 and int(value[4:7]) <= 193:
						hgt_valid = True
				if "in" in value:
					if int(value[4:6]) >= 59 and int(value[4:6]) <= 76:
						hgt_valid = True
			except ValueError:
				None
		if "hcl" in value:
			if "#" == value[4]:
				out_of_6 = 0
				valid_vals = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
				for i in range(5, 11):
					if value[i] in valid_vals:
						out_of_6 += 1
				if out_of_6 == 6:
					hcl_valid = True
		if "ecl" in value:
			eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
			if value[4:7] in eye_colors:
				ecl_valid = True
		if "pid" in value:
			if len(value) == 13:
				pid_valid = True
	end = False
print(valid)


