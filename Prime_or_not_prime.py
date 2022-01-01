#Write a program to determine if a number is prime or not

n=int(input("Enter number to find prime or not: "))
for i in range(2,n):
	if (n%i==0):
		print("The given number",n,"is not a prime number")
		break
else:
	if (n<2):
		print("The given number",n,"is not a prime number")
	else:
		print("The given number",n,"is a prime number")
	
