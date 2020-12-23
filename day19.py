data = open("C:\\Users\\djdeb\\Desktop\\Random Stuff\\Advent of Code 2020\\day19input.txt")
str1 = data.read()
puzzle_array = str1.splitlines()


rules = {}
'''
def eval_rules(rules, num):
	num = int(num)
	string_poss = []
	if rules[num][0] == "a" or rules[num][0] == "b":
		return [rules[num][0]]
	elif num == 113:
		string_poss.append("b")
		string_poss.append("a")
	elif num == 8:
		rule1 = eval_rules(rules, rules[num][0][0])
		for i in rule1:
			string_poss.append(i)
	elif num == 11:
		None
	else:
		rule1 = eval_rules(rules, rules[num][0][0])
		rule2 = eval_rules(rules, rules[num][0][1])
		for i in rule1:
			for j in rule2:
				if len(i + j) > 96:
					break
				else:
					string_poss.append(i + j)
		if len(rules[num]) > 1:
			rule1 = eval_rules(rules, rules[num][1][0])
			rule2 = eval_rules(rules, rules[num][1][1])
			for i in rule1:
				for j in rule2:
					if len(i + j) > 96:
						break
					else:
						string_poss.append(i + j)
	return string_poss

for i in range(138):
	rule = puzzle_array[i].split()
	num = int(rule[0].split(":")[0])
	if "|" in rule and num != 11 and num != 8:
		if num == 113:
			rules[num] = [[rule[1]], [rule[3]]]
		else:
			rules[num] = [[rule[1], rule[2]], [rule[4], rule[5]]]
	elif len(rule) == 3:
		rules[num] = [[rule[1], rule[2]]]
	elif num == 8:
		rules[num] = [[42], [42, 42], [42, 42, 42], [42, 42, 42, 42], [42, 42, 42, 42, 42], [42, 42, 42, 42, 42, 42], [42, 42, 42, 42, 42, 42, 42], [42, 42, 42, 42, 42, 42, 42, 42], [42, 42, 42, 42, 42, 42, 42, 42, 42]
		, [42, 42, 42, 42, 42, 42, 42, 42, 42, 42], [42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42], [42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42]]
	elif num == 11:
		print(rule)
		rules[num] = [[42, 31], [42, 42, 31, 31], [42, 42, 42, 31, 31, 31], [42, 42, 42, 42, 31, 31, 31, 31], [42, 42, 42, 42, 42, 31, 31, 31, 31, 31], [42, 42, 42, 42, 42, 42, 31, 31, 31, 31, 31, 31]]
	else:
		if "a" in rule[1]:
			rules[num] = ["a"]
		else:
			rules[num] = ["b"]
'''
#for i in [42, 31]:
#	print(i, len(eval_rules(rules, i)), eval_rules(rules, i))

rule_42 = ['abbabaaa', 'ababaaaa', 'abaabaaa', 'aabbaaaa', 'aababaaa', 'aaabbaaa', 'aaabaaaa', 'aaaaaaaa', 'ababbbaa', 'abaabbaa', 'aaabbbaa', 'aababbaa', 'aaaabbaa', 'abbaabaa', 'aabbabaa', 'aaababaa', 'aabbbbba', 'aabaabba', 'aaaabbba', 'aaaaabba', 'aaaaaaba', 'aabbbaba', 'aabababa', 'abaaaaba', 'ababbbba', 'abababba', 'abaaabba', 'abbbbaba', 'abbbaaba', 'abbababa', 'abbaaaba', 'abbabbba', 'abbbabba', 'abbaabba', 'bbbabbaa', 'bbbbbbaa', 'bbabbbaa', 'babbbbaa', 'baabbbaa', 'bbbaabaa', 'babbabaa', 'bbbbabaa', 'bbababaa', 'bbabbaaa', 'bbaabaaa', 'bbbaaaaa', 'babbbaaa', 'bababaaa', 'babbaaaa', 'baaaaaaa', 'bbabbaba', 'bbaaaaba', 'bbabbbba', 'bbababba', 'bbaabbba', 'bbaaabba', 'bbbababa', 'bbbbbbba', 'bbbbabba', 'babbabba', 'babaabba', 'babbbbba', 'babbbaba', 'babbaaba', 'babaaaba', 'baaababa', 'baabaaba', 'baaaaaba', 'babaabab', 'bababaab', 'babaaaab', 'babbbbab', 'baabbbab', 'baabbaab', 'baaabbab', 'baaaabab', 'babbaabb', 'babaaabb', 'baababbb', 'babbbbbb', 'babbabbb', 'bbabbbab', 'bbabaaab', 'bbaabbab', 'bbaabaab', 'bbbaabab', 'bbbbbabb', 'bbbbaabb', 'bbbabbbb', 'bbbbabbb', 'bbbaabbb', 'bbabbbbb', 'bbabaabb', 'bbaabbbb', 'bbaababb', 'aabbabbb', 'aabaabbb', 'aaaaabbb', 'aabbbbbb', 'aababbbb', 'abbaabbb', 'abbbbbbb', 'aabaaabb', 'abbbaabb', 'ababaabb', 'aabbaabb', 'aaabaabb', 'abbababb', 'aabababb', 'aaaababb', 'abbbbaab', 'abbaaaab', 'ababbaab', 'ababaaab', 'abababab', 'abbaabab', 'abaaabab', 'abbbbbab', 'abbabbab', 'abaabbab', 'aababaab', 'aabaaaab', 'aabaabab', 'aaaabaab', 'aaaaabab', 'aaababab', 'aaabbbab', 'aaabbaab']
rule_31 = ['abbabbbb', 'abaabbbb', 'aaaabbbb', 'ababbbbb', 'aaabbbbb', 'baabbbbb', 'bababbbb', 'baaabbbb', 'bbbbbbbb', 'babaabbb', 'baaaabbb', 'bbababbb', 'bbaaabbb', 'abbbabbb', 'abababbb', 'aaababbb', 'abaaabbb', 'bbbaaabb', 'bbaaaabb', 'baaaaabb', 'abbaaabb', 'abaaaabb', 'aaaaaabb', 'baabaabb', 'abaababb', 'bbbababb', 'babababb', 'baaababb', 'bbabbabb', 'baabbabb', 'ababbabb', 'aaabbabb', 'abbbbabb', 'babbbabb', 'aabbbabb', 'babbabab', 'baababab', 'bababbab', 'bbbabbab', 'bbbbbbab', 'bbbbabab', 'bbababab', 'bbaaabab', 'ababbbab', 'aabbbbab', 'aababbab', 'aaaabbab', 'abbbabab', 'aabbabab', 'aabbbaab', 'abbabaab', 'abaabaab', 'abbbaaab', 'abaaaaab', 'aabbaaab', 'aaabaaab', 'aaaaaaab', 'babbaaab', 'baabaaab', 'baaaaaab', 'bbbbaaab', 'bbbaaaab', 'bbaaaaab', 'bbabbaab', 'bbbbbaab', 'bbbabaab', 'babbbaab', 'baaabaab', 'baabbbba', 'abbbbbba', 'aaabbbba', 'bbbabbba', 'bababbba', 'aababbba', 'baaabbba', 'abaabbba', 'baababba', 'aaababba', 'aabbabba', 'baaaabba', 'bbbaabba', 'ababbaba', 'abaababa', 'aaabbaba', 'aaaababa', 'bbaababa', 'babababa', 'bbbbbaba', 'baabbaba', 'bbbaaaba', 'bbbbaaba', 'bbabaaba', 'aabbaaba', 'ababaaba', 'aaabaaba', 'aabaaaba', 'aaaabaaa', 'aaaaabaa', 'aabbbbaa', 'aabbbaaa', 'aabaabaa', 'aabaaaaa', 'abbbbaaa', 'ababbaaa', 'abbbaaaa', 'abbaaaaa', 'abaaaaaa', 'abbabbaa', 'abbbbbaa', 'abbbabaa', 'abababaa', 'abaaabaa', 'bbaaabaa', 'bbaabbaa', 'bababbaa', 'babaabaa', 'baaabbaa', 'baababaa', 'baaaabaa', 'bbbbaaaa', 'bbabaaaa', 'baabaaaa', 'bbaaaaaa', 'babaaaaa', 'bbbbbaaa', 'bbbabaaa', 'baabbaaa', 'baaabaaa']
#rule_0 = eval_rules(rules, 0)
count = 0

for i in range(138, len(puzzle_array)):
	line = puzzle_array[i]
	if len(line) % 8 == 0:
		eight_block = 0
		forty_twos = 0
		thirty_ones = 0
		no_count = False
		rep = ""
		while eight_block * 8 < len(line):
			if line[(eight_block * 8):(eight_block * 8 + 8)] in rule_42:
				if thirty_ones > 0:
					no_count = True
				forty_twos += 1
				rep = rep + "1"
			elif line[(eight_block * 8):(eight_block * 8 + 8)] in rule_31:
				thirty_ones += 1
				rep = rep + "0"
			else:
				no_count = True
			eight_block += 1
		if not no_count and thirty_ones < forty_twos:
			count += 1
			print(forty_twos, thirty_ones, rep)



print(count)

