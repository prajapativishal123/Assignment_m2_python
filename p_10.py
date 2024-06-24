'''Write a Python program that will return true if the two given integer 
values are equal or their sum or difference is 5.'''

n1=int(input("enter a number : "))
n2=int(input("enter a number : "))
if n1==n2:
    print("true")
elif n1+n2==5:
    print("true")
elif abs(n1 - n2) == 5:
    print("true")
else:
    print(n1+n2)
