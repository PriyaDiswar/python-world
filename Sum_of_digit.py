##Write a program to print the sum of digits of a number.

n=int(input("Enter the number: "))
a=n
s=0
while n>0:
	s=s+n%10
	n=n//10
print("The sum of digits of",a,"is",s)
