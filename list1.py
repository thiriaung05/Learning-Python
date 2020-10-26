def input_list(no,num):
    for i in range(0,no):
        number=input("Enter a input list:")
        num.append(int(number))
        
def output_list(num,no):
    print("Divisible of",no,"in a list")
    for i in range(0,no):
        if num[i]%5==0:
            print(num[i])
        
inputList=input("Enter a loop number:")
list=int(inputList)
num=[]
input_list(list,num)
output_list(num,list)