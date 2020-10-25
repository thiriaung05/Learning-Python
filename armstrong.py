def armstrong(no):
    temp=no
    c=0
    while no>0:
        a=int(no%10)
        no=int(no/10)
        c=c+(a*a*a)
    
    if c==temp:
        print(temp,"is armstrong!")
    else:print(temp,"is not armstrong!")


number=input("Enter the armstrong number:")
num=int(number)
armstrong(num)