def factorial(no):
    if no==0:
        return 1
    else:
        return no*factorial(no-1)
    

number=input("Enter the factorial number:")
no=int(number)
n=factorial(no)
print(no,"factorial is",n)