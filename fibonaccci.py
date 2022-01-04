#program to Calculate Fibonacci numbers less than a given number and calculates the sum of all alternate numbers (even numbered) in the generated list.

n=int(input("Please enter a number: "))
a=0
b=1
c=a+b
print(a)
print(b)
l=[0,1]
while c<=n:
	print(c)
	l.append(c)
	a=b
	b=c
	c=a+b
s=0
length=len(l)
for i in range(0,length,2):
	s=s+l[i]
print("Sum =",s)
