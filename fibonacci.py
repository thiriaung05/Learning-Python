def fibonacci(num1,num2):
    print(num1,num2,end=" ")
    for i in range(0,5):
        num3=num1+num2
        num1=num2
        num2=num3
        print(num3,end=" ")

num1=1
num2=2
fibonacci(num1,num2)