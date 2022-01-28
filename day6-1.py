with open("20input-6-1.txt") as f:
	groups = [ group.strip() for group in f.read().split('\n\n') ]

count = 0
for i in range(len(groups)):
	yeses = set()
	for j in range(len(groups[i])):
		if groups[i][j]!='\n':
			yeses.add(groups[i][j])
	count += len(yeses)

print(f"The sum is {count}.")
