with open("20input-3-2.txt") as f:
	lines = [ line.strip() for line in f.readlines() ]

treeCounts = {}

def treeCount(x,y):
	treeCount=0	
	xpos=0
	i = 0
	patternWidth=len(lines[0])
	while i in range(len(lines)):
		if lines[i][xpos%patternWidth]=='#':
			treeCount+=1
		xpos+=x
		i += y
	return treeCount

mySlopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
slopeKeys = ['Right 1, down 1.',\
		'Right 3, down 1.',\
		'Right 5, down 1.',\
		'Right 7, down 1.',\
		'Right 1, down 2.']

for i in range(len(mySlopes)):
	treeCounts[slopeKeys[i]]=treeCount(mySlopes[i][0],mySlopes[i][1])

finalValue=1
for key in treeCounts:
	print(f"The slope \"{key}\" hits {treeCounts[key]} trees.")
	finalValue *= treeCounts[key]

print(f"I'd get {finalValue} :P")
