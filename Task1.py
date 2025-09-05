def func(x):
     if x < 0:
         return "not defined for negative numbers"
     elif(x==0):
         return 1
     else:
         return x * func(x-1)

x=int(input("Enter a number: "))
print("Factorial of ",x,"is",func(x))

