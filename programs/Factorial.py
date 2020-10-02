
num = int(input("Enter a number: "))   # To take input from the user
factorial = 1
# check if the number is negative, positive or zero
if num < 0:
   print("Factorial is not defined for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for f in range(1,num + 1):
       factorial = factorial*f
   print("The factorial of",num,"is",factorial)
