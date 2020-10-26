Inputloop=input("Enter the number:")
loop=int(Inputloop)
num=[]

for i in range(0,loop):
    number=input("Enter the list number:")
    num.append(int(number))

num1=num[0]
num2=num[loop-1]
if num1==num2:
    print("Result is True")
else:print("Result is False")