# class Node(object):
    
#     def __init__(self):
#         self.value = None
#         self.decision = None
#         self.childs = None
    
import math
items = ['acd' , 'bce' , 'abce', 'be']
minSupport = 2
print(items)

al = []
for item in items :
    for i in item :
        al.append(i)
print(al)

withoutFre = [] # a b c d e
[withoutFre.append(x) for x in al if x not in withoutFre]
print(withoutFre)

itemsWithFreq = []
for letter in withoutFre : #a => b
    freq = 0 #2
    for item in items: #abc => dea
        if letter in item:
            freq+=1
    itemsWithFreq.append((letter , freq))

print(itemsWithFreq)

firstDelete = []
for item in itemsWithFreq : # ('a',2)
    if item[1] >= minSupport: #2
        firstDelete.append(item[0])

print(firstDelete)

twoDim = []
flag=1
for item in firstDelete:
    for item_id in range(0,len(firstDelete)-flag) :
        twoDim.append(item+firstDelete[item_id+flag])
    flag+=1

print(twoDim)

itemsWithFreq = [] 
for str in twoDim : # ac
    freq = 0 
    for item in items: # abc
        if str[0] in item and str[1] in item:
            freq+=1
    itemsWithFreq.append((str , freq))

print(itemsWithFreq)

secondDeleted = []
for item in itemsWithFreq : # ('ac',1)
    if item[1] >= minSupport: #2
        secondDeleted.append(item[0])

print(secondDeleted)
        

