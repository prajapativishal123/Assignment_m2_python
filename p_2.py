''' Write a Python program to get the Factorial number of given number.'''
num=int(input("enter number : "))
result=1
for i in range(1,num+1):
    result=result*i
    
print("fectorial number : ",result)
    
