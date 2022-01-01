#Write a program to convert the temperature given in Fahrenheit to Celsius and vice versa.

a=input("Please enter temperature with unit: ")
b=int(a[:-1])

if (a[-1] in ['f','c','F','C']):
	if (a[-1]=="F"or a[-1]=="f"):
		c0=(b-32)*5/9
		c0=round(c0,2)
		print("{} F = {} C".format(b,c0))
	else:
		f0=(b*9/5)+32
		f0=round(f0,2)
		print("{} C = {} F".format(b,f0))
else:
	print("Unrecognized unit:",a[-1])
