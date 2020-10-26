row=5
char=65
col=1

for i in range(0,row):
    for j in range(0,col):
        print(chr(char),end=" ")
        char=char+1
    col=col+2
    print("\r")