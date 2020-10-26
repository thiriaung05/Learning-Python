row=5
char=65

for i in range(0,row):
    for j in range(0,i+1):
        print(chr(char),end=" ")
    char=char+1
    print("\r")