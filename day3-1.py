with open("20input-3-1.txt") as f:
	lines=[ line.strip() for line in f.readlines() ]

xpos=0
treeCount=0
i = 0
patternWidth=len(lines[0])
while i in range(len(lines)):
	if lines[i][xpos%patternWidth]=='#':
		treeCount+=1
	xpos+=3
	i += 1 

print(f"{treeCount} trees.")
