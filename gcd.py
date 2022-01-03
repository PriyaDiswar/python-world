#Write a program to find the G.C.D. of two given numbers 

a=int(input("Please enter an integer: "))
b=int(input("Please enter another integer: "))
c=min(abs(a),abs(b))       # gcd of negative numbers is equal to their absolute value
if (a!=0 and b!=0):
    for i in range(c,0,-1):
	    if (a%i==0)and(b%i==0):
		    print("The GCD of {} and {} is {}".format(a,b,i))
		    break
else:
	print("Numbers must be non zero")
