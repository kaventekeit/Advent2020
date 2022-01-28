with open("20input-5-1.txt") as f:
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

highest = 0
for i in range(len(myPosArr)):
	seatID = myPosArr[i][0]*8 + myPosArr[i][1]
	if highest<seatID:
		highest = seatID
	
print(f"The highest seat ID is {highest}.")
