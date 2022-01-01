##Program to determine if a number is perfect number and abundant number and deficient number 

n=int(input("Enter an integer: "))
l=[]
s=0
for i in range(1,n):
	if (n%i==0):
		l.append(i)
print("The factors of",n,"are:",l)
length=len(l)
for a in range(0,length):
	s=s+l[a]
print("The sum of the factors is:",s)
if s==n:
	print("The given number",n,"is a perfect number")
elif s>n:
	print("The given number",n,"is an abundant number")
else:
	print("The given number",n,"is a deficient number")
	
