import os
import sys

##home_dir = os.system("cat file1.txt")
for i in range(len(sys.argv)):
    print(sys.argv[i])
for i in range(1,len(sys.argv)):
    home_dir = os.system("cat "+sys.argv[i])