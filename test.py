import collections

letter_positions = collections.defaultdict(list)

for index, letter in enumerate("letters"):
	letter_positions[letter].append(index)
	print(letter_positions)

