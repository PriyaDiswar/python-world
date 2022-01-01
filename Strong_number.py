#To find the given number is strong number or not


import math
n=int(input("Enter number to find strong or not: "))
a=n
s=0
while n>0:
	s=s+math.factorial(n%10)
	n=n//10
if (s==a):
	print("The given number",a,"is a strong number")
else:
	print("The given number",a,"is not a strong number")
