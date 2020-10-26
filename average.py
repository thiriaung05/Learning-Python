number1=input("Enter number1:")
num1=int(number1)
number2=input("Enter number2:")
num2=int(number2)
sum=0

multi=num1*num2
if multi>=1000:
    sum=num1+num2
    print("The result is",sum)
else:print("The result is",multi)