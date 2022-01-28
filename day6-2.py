with open("20input-6-1.txt") as f:
	groups = [ group.strip().split('\n') for group in f.read().split('\n\n') ]

print(groups)

count = 0
for i in range(len(groups)):
	totalYeses = set()
	for j in range(len(groups[i])):
		for k in range(len(groups[i][j])):
			totalYeses.add(groups[i][j][k])
	for j in range(len(groups[i])):
		stringsplit = set()
		for k in range(len(groups[i][j])):
			stringsplit.add(groups[i][j][k])
		for x in totalYeses.copy():
			if x not in stringsplit:
				totalYeses.remove(x)
	count += len(totalYeses)

print(f"Your count is {count}.")
print(f"Sanity check: there are {len(groups)} groups.")
