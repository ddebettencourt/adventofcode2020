data = open("C:\\Users\\djdeb\\Desktop\\Random Stuff\\Advent of Code 2020\\day22input.txt")
str1 = data.read()
puzzle_array = str1.splitlines()

p1_deck = puzzle_array[1:26]
p2_deck = puzzle_array[28:]

#p1_deck = puzzle_array[1:6]
#p2_deck = puzzle_array[8:]
print(p1_deck, p2_deck)

def mash_string(p1, p2):
	s = ""
	for p in p1:
		s = s + str(p)
		s = s + ","
	for p in p2:
		s = s + str(p)
		s = s + ","
	return s

def play_game(p1_deck, p2_deck):
	count_rounds = 0
	round_set = set()
	def play_round(p1, p2):
		#print(p1, p2)
		#print(round_dict, mash_string(p1, p2))
		if len(p1) > int(p1[0]) and len(p2) > int(p2[0]):
			result = play_game(p1[1:1+int(p1[0])], p2[1:1+int(p2[0])])
			return result
		elif int(p1[0]) > int(p2[0]):
			return 0
		else:
			return 1	

	while len(p1_deck) > 0 and len(p2_deck) > 0:
		count_rounds += 1
		if count_rounds % 100 == 0 and len(p1_deck) + len(p2_deck) > 39:
			print(count_rounds, len(p1_deck) + len(p2_deck))
		if mash_string(p1_deck, p2_deck) in round_set:
			return 0
		else:
			round_set.add(mash_string(p1_deck, p2_deck))
		round_champ = play_round(p1_deck, p2_deck)
		if round_champ == 0:
			p1_deck.append(p1_deck[0])
			p1_deck.append(p2_deck[0])
			p1_deck.pop(0)
			p2_deck.pop(0)
		elif round_champ == 1:
			p2_deck.append(p2_deck[0])
			p2_deck.append(p1_deck[0])
			p2_deck.pop(0)
			p1_deck.pop(0)
		else:
			#print("here")
			return 0
	if len(p1_deck) == 0:
		print(mult_arr(p2_deck))
		return 1
	else:
		print(mult_arr(p1_deck))
		return 0
		#print(len(p1_deck), len(p2_deck))


def mult_arr(arr):
	count = 0
	for i in range(len(arr)):
		count += (len(arr) - i) * int(arr[i])
		print(count)
	print(count)

a = [43, 19]
b = [2, 29, 14]

