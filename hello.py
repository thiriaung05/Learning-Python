import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")
if os.path.exists("myfolder"):
    os.rmdir("myfolder")
else:
    print("The folder does not exist")