with open('20input-1-1.txt') as f:
	lines = f.readlines()

numsArr = [ int(str(line.strip())) for line in lines ]
	
print(numsArr)

def printbalance(nums):
	retArr = []
	balance = 0
	for i in range(len(nums)):
		num1 = nums[i]
		for j in range(len(nums)):
			num2 = nums[j]
	
			if num1+num2==2020:
				balance=num1*num2
				retArr = [balance, num1, num2]
				return retArr
	return retArr

myArr = printbalance(numsArr)

if myArr != []:
	print(f"Your balance is {myArr[0]}.")
	print(f"This was gotten by multiplying {myArr[1]} and {myArr[2]}.")
else:
	print("???")
