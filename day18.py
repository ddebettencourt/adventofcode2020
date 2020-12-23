data = open("C:\\Users\\djdeb\\Desktop\\Random Stuff\\Advent of Code 2020\\day18input.txt")
str1 = data.read()
puzzle_array = str1.splitlines()

def num_eval(string):
	arr = string.split()
	print(arr)
	cur_val = int(arr[0])
	i = 1
	while i < len(arr):
		if arr[i] == "+":
			arr[i] = int(arr[i-1]) + int(arr[i+1])
			arr.pop(i+1)
			arr.pop(i-1)
			i -= 1
		#elif arr[i] == "*":
		#	cur_val *= int(arr[i+1])
		i += 1
	cur_val = int(arr[0])
	i = 1
	while i < len(arr):
		if arr[i] == "*":
			cur_val *= int(arr[i+1]) 
		i += 2

	print(cur_val)
	return cur_val

def eval_array(puzzle_array):
	for i in range(len(puzzle_array)):
		parens = 0
		paren_locs = []
		for k in range(4):
			for j in range(len(puzzle_array[i])):
				if puzzle_array[i][j] == "(":
					paren_locs.append(j)
				elif puzzle_array[i][j] == ")":
					first_paren = max(paren_locs)
					num = num_eval(puzzle_array[i][first_paren+1:j])
					prev_len = len(puzzle_array[i])
					extra_spaces = (j - first_paren) - len(str(num)) + 2
					puzzle_array[i] = puzzle_array[i][0:first_paren] + str(num) + (" " * extra_spaces) + puzzle_array[i][j+1:]
					for p in paren_locs:
						if p == first_paren:
							paren_locs.remove(p)
				print(paren_locs, i,j, puzzle_array[i])
		puzzle_array[i] = num_eval(puzzle_array[i])
	return puzzle_array

eval_array(puzzle_array)
print(puzzle_array)






