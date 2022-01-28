with open("20input-2-2.txt") as f:
	lines = f.readlines()

lines = [ line.strip() for line in lines ]

pos1 = []
pos2 = []
letters = []
passwords = []
for line in lines:
	line=line.split(':')	
	passwords.append(line[1].strip())	
	line[0]=line[0].split(' ')	
	letters.append(line[0][1])
	line[0][0]=line[0][0].split('-')
	pos1.append(int(line[0][0][0]))
	pos2.append(int(line[0][0][1]))

validCount=0
for i in range(len(passwords)):
	p1=pos1[i]
	p2=pos2[i]	
	letter=letters[i]
	if (passwords[i][p1-1]==letter)^(passwords[i][p2-1]==letter):
		validCount += 1

print(f"You have {validCount} valid passwords.")
	
