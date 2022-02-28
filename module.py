import os
import shutil
#print(os.system("date"))
#os.mkdir("/Users/sylvi/OneDrive/Desktop/Test")
#print(os.getcwd())
#print(os.path.exists("/Users/sylvi/OneDrive/Desktop/Seven"))
#x = os.path.splitext("/Users/sylvi/OneDrive/Desktop/python/if.py")
#print(x[1])
#print(os.listdir())
source = input("Enter Source Folder: ")
destination = input("Enter Destination: ")
source = source+"/"
destination = destination+"/"
files = os.listdir(source)
for i in files:
    shutil.copy((source+i),destination)
