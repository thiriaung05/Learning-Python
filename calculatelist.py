def input_list(no,num):
    for i in range(0,no):
        number=input("Enter a input list:")
        num.append(int(number))

def calculate_list(list1,list2,list3,no):
    print("Result List is")
    for i in range(0,no):
        if list1[i]%2!=0:
            list3.append(list1[i])
     
    for i in range(0,no):
        if list2[i]%2==0:
            list3.append(list2[i])
    
    for j in range(0,len(list3)):
        print(list3[j])

number=input("Enter the loop number:")
no=int(number)
list1=[]
list2=[]
list3=[]
input_list(no,list1)
input_list(no,list2)
calculate_list(list1,list2,list3,no)