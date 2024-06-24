'''Write a Python program to sum of three given integers. However, if 
two values are equal sum will be zero. '''


n1=int(input("enter a number : "))
n2=int(input("enter a number : "))
n3=int(input("enter a number : "))

sum=n1+n2+n3
if n1==n2:
    print("answer : 0")
elif n2==n3:
    print("answer : 0")
elif n1==n3:
    print("answer : 0")
else:
    print("answer : ",sum)

    
