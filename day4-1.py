import re

with open("20input-4-1.txt") as f:
	blob = f.read()

passports = blob.split('\n\n')
passports = [ passport.strip() for passport in passports ]

required = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

validCount=0
for i in range(len(passports)):
	isValid=True
	for j in range(len(required)):
		check=re.compile(required[j])
		reqr = check.search(passports[i])
		if reqr==None:
			isValid=False
	if isValid==True:
		validCount += 1

print(f"You have {validCount} valid passports.")

print(f"(This is out of {len(passports)} total.)")			
