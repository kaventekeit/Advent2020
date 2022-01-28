with open("20input-5-2.txt") as f:
	passes = [ line.strip() for line in f.readlines() ]

myPosArr = []
for i in range(len(passes)):

	myRowInd = []
	for j in range(128):
		myRowInd.append(j)
	for k in range(7):
		if passes[i][k]=="F":
			myRowInd = myRowInd[:len(myRowInd)//2]
		elif passes[i][k]=="B":
			myRowInd = myRowInd[len(myRowInd)//2:]
	myRowInd = myRowInd[0]	

	myColInd = []
	for j in range(8):
		myColInd.append(j)
	for k in range(7,10):
		if passes[i][k]=="L":
			myColInd = myColInd[:len(myColInd)//2]
		elif passes[i][k]=="R":
			myColInd = myColInd[len(myColInd)//2:]
	myColInd = myColInd[0]
	
	rowcol = [myRowInd, myColInd]
	myPosArr.append(rowcol)

EverySeatInOrder = []

row = 0
col = 0

while row<128:
	for i in range(len(myPosArr)):
		if myPosArr[i][0]==row and myPosArr[i][1]==col:
			EverySeatInOrder.append(myPosArr[i])
	col += 1
	col = col % 8
	if col==0:
		row += 1

mySeat = [0,0]
for i in range(len(EverySeatInOrder)-1):
	currSeat = EverySeatInOrder[i]
	nextSeat = EverySeatInOrder[i+1]

	if nextSeat[1]-currSeat[1]==2: # gap in row
		mySeat = [nextSeat[0],currSeat[1]+1]
	elif nextSeat[1]-currSeat[1]==-6\
		and currSeat[1]==7: # gap @ beginning of row
		mySeat = [nextSeat[0],0]
	elif nextSeat[1]-currSeat[1]==-6\
		and currSeat[1]==6: # gap @ end of row
		mySeat = [currSeat[0],7]

print(f" {len(EverySeatInOrder)} should be the same as {len(myPosArr)} ")

print(f"My seat is {mySeat}.")

print(f"My seat ID is {mySeat[0]*8+mySeat[1]}.")	
