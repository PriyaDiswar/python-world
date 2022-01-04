#Write a program to check the numbers are even or odd upto given number and print them. 

n=int(input("Please enter a number: "))
print("Odd and Even numbers")
for i in range(0,n):
	if i%2==0:
		print("{} is an even number".format(i))
	else:
		print("{} is an odd number".format(i))
