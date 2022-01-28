with open("20input-2-1.txt") as f:
	lines = f.readlines()

lines = [ line.strip() for line in lines ]

lows = []
highs = []
letters = []
passwords = []
for line in lines:
	line=line.split(':')	
	passwords.append(line[1].strip())	
	line[0]=line[0].split(' ')	
	letters.append(line[0][1])
	line[0][0]=line[0][0].split('-')
	lows.append(line[0][0][0])
	highs.append(line[0][0][1])


validCount=0
for i in range(len(passwords)):
	limitChar = letters[i]
	least = int(lows[i])
	most = int(highs[i])
	charCount=0
	for j in range(len(passwords[i])):
		if passwords[i][j]==limitChar:
			charCount += 1
			
	if least<=charCount<=most:
		validCount += 1

print(f"{validCount} passwords are valid.")

