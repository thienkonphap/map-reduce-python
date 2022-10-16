from curses.ascii import isalpha
from itertools import count
import sys
import copy

f = open(sys.argv[len(sys.argv)-1], "r")

lines = f.readlines()
for i in range (len(lines)):
    lines[i] = lines[i][0:-1]
linesNoSpace = copy.copy(lines)
for i in range(len(linesNoSpace)):
    linesNoSpace[i] = linesNoSpace[i].replace(" ","")

countCharacter = 0
for i in linesNoSpace:
    countCharacter+=len(i)
#Words count
countWords = 0
lines_mots = copy.copy(lines)
for i in range(len(lines_mots)):
    lines_mots[i] = lines_mots[i].split(" ")
dict_word = {}
countWords = 0
maxWords = 0
keyMaxWords = ""
wordlusLongue = ""
for i in lines_mots:
    for j in i:
        if j in dict_word and j.isalpha():
            dict_word[j] +=1
        else:
            dict_word[j] = 1
print(dict_word)
for i in dict_word:
    countWords+=dict_word[i]
    if dict_word[i]>maxWords:
        maxWords = dict_word[i]
        keyMaxWords=i
    wordlusLongue = i if len(wordlusLongue)<= len(i) else wordlusLongue

print("Nombre de lignes : ", len(lines))
print("Nombre de caracteres", countCharacter)
print("Nombre de mots : ",countWords )
print("Mot le plus frequent : ",keyMaxWords , " frequence = " ,maxWords)
print("Mot le plus long : ", wordlusLongue)
print("Moyenne du nombre de mots par ligne",countWords//len(lines))

countchar = dict()
print(lines)
for i in lines:
    for j in range(len(i)):
        if i[j] in countchar.keys() and i[j].isalpha():
            countchar[i[j]] += 1
        elif i[j] not in countchar.keys():
            countchar[i[j]]=1
            
print("Lettre la plus frequente : ",max(countchar.items(), key = lambda k : k[1]))