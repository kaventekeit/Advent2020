import re

with open("20input-4-1.txt") as f:
	blob = f.read()

passports = blob.split('\n\n')
passports = [ passport.strip() for passport in passports ]

required = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

# --------------------------------------------------------------
# --- Initialize an array marking indices of valid passports ---
# --------------------------------------------------------------

isValid = []
for i in range(len(passports)):
	isValid.append(True)

# ----------------------------------------------------------------------------
# --- Repeat regex code from previous problem to mark incomplete passports ---
# ----------------------------------------------------------------------------

for i in range(len(passports)):
	for j in range(len(required)):
		check=re.compile(required[j])
		reqr = check.search(passports[i])
		if reqr==None:
			isValid[i]=False

# -----------------------------------------------------------------------------
# --- Now things get interesting. ---------------------------------------------
# --- We refactor passports into a list of lists, each one field:value pair ---
# -----------------------------------------------------------------------------

listArr = []			
for i in range(len(passports)):
	tPassArr = []
	charBuf = ''
	j = 0
	while True:
		if passports[i][j]!=(' ') and passports[i][j]!=('\n'):
			charBuf += passports[i][j]
		else:
			tPassArr.append(charBuf)
			charBuf = ''
		j += 1
		if not j in range(len(passports[i])):
			tPassArr.append(charBuf)
			charBuf = ''
			break
	listArr.append(tPassArr)

print(listArr)


# -----------------------------------------------------------------------------
# --- A function called validCheck checks a SINGLE field:value pair for -------
# --- validity, returning a bool. ---------------------------------------------
# -----------------------------------------------------------------------------

def validCheck(pair:str) -> bool:
	if pair[0]=='b' and pair[1]=='y' and pair[2]=='r':
		if len(pair[4:])!=4:	
			return False
		try:
			year = int(pair[4:])
		except:
			return False
		if 1920<=year<=2002:
			return True
		else:
			return False
	elif pair[0]=='i' and pair[1]=='y' and pair[2]=='r':
		if len(pair[4:])!=4:
			return False
		try:
			year = int(pair[4:])
		except:
			return False
		if 2010<=year<=2020:
			return True
		else:
			return False
	elif pair[0]=='e' and pair[1]=='y' and pair[2]=='r':
		if len(pair[4:])!=4:
			return False
		try:
			year = int(pair[4:])
		except:
			return False
		if 2020<=year<=2030:
			return True
		else:
			return False
	elif pair[0]=='h' and pair[1]=='g' and pair[2]=='t':
		numStrBuf = ''
		i = 4
		units = pair[-2:]
		while i in range(len(pair)):
			try: 
				myInt = int(pair[i])
				numStrBuf += pair[i]
				i += 1
			except:
				break
		num = int(numStrBuf)
		if units == 'in':
			if 59<=num<=76:
				return True
			else:
				return False
		elif units == 'cm':
			if 150<=num<=193:
				return True
			else:	
				return False
		else:
			return False		
	elif pair[0]=='h' and pair[1]=='c' and pair[2]=='l':
		if pair[4]!='#':
			return False
		else:
			if len(pair[5:])==6:
				return True
			else:
				return False
	elif pair[0]=='e' and pair[1]=='c' and pair[2]=='l':
		if pair[4:]=='amb'\
		or pair[4:]=='blu'\
		or pair[4:]=='brn'\
		or pair[4:]=='gry'\
		or pair[4:]=='grn'\
		or pair[4:]=='hzl'\
		or pair[4:]=='oth':
			return True
		else:
			return False
	elif pair[0]=='p' and pair[1]=='i' and pair[2]=='d':
		if len(pair[4:])!=9:
			return False
		else:
			try:
				myInt = int(pair[4:])
				return True
			except:
				return False
	elif pair[0]=='c' and pair[1]=='i' and pair[2]=='d':
		return True
	else:
		return False

# --------------------------------------------------------------------
# --- We use the result of validCheck to set each item in isValid. ---
# --------------------------------------------------------------------

for i in range(len(listArr)):
	if isValid[i]==True:
		for j in range(len(listArr[i])):
			if validCheck(listArr[i][j])==False:
				isValid[i]=False

validCount=0
for i in range(len(passports)):
	if isValid[i]==True:
		validCount += 1

# -------------
# --- DONE! ---
# -------------

print(f"You have {validCount} valid passports.")

	
print(f"(This is out of {len(passports)} total.)")			

