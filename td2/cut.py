import os
import sys

c = sys.argv[2]
intervall = []
for i in range (4,len(sys.argv)-1):
    intervall.append(sys.argv[i])
index = []
for i in range (len(intervall)):
    numbList = intervall[i].split("-")
    index.append([int(numbList[0]),int(numbList[1])])
print("intervall = ", index)
for i in range(len(index)): 
    index[i] = [ i for i in range(index[i][0],index[i][1]+1)]
print("index = ",index)
flat_index =[item for sublist in index for item in sublist]
print(flat_index)
list_set = set(flat_index)
# convert the set to the list
unique_list = (list(list_set))

sortedList = sorted(unique_list)
print("sortedList :", sortedList)

#read file
f = open(sys.argv[len(sys.argv)-1], "r")
lines = f.readlines()
line = lines[0][0:-1]
print("Input: ", line)
line = line.split(",")
print("Output")
for i in range (1,len(sortedList)+1):
    if i in sortedList:
        print(line[i-1],end=", ")