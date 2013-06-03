#! /usr/bin/env python3.3

def testLychrel(nbr,ctr=1):
	if ctr >= 50:
		return [nbr,ctr]
	
	lychrelTest = nbr + palindromeTransform(nbr)
	if isPalindromic(lychrelTest):
		return [lychrelTest,ctr]
	else:
		return testLychrel(lychrelTest,ctr+1)

def palindromeTransform(nbr):
	return int(str(nbr)[::-1])

def isPalindromic(i):
	if palindromeTransform(i) == i: return True


lychrelCount = notLychrelCount = 0
for n in range(1,10000):
	lychrelTerm = testLychrel(n)
	if lychrelTerm[1]<50:
		lychrelCount += 1
		print("+",lychrelCount,")",n," is a lychrel number terminating at",lychrelTerm[0],"after",lychrelTerm[1],"iterations")
	else:
		notLychrelCount += 1
		print("-",notLychrelCount,")",n,"is probably not a Lychrel number after",lychrelTerm[1],"iterations (",lychrelTerm[0],")" )
print("===Between 1 and 10,000 there are:===")
print(notLychrelCount," non-Lychrel numbers.")
print(lychrelCount," Lychrel numbers.")
