Data = [
    ["sunny", "sunny", "overcast", "rain", "rain", "rain", "overcast", "sunny", "sunny", "rain", "sunny", "overcast", "overcast", "rain"],
    ["High", "High", "High", "High", "Normal", "Normal", "Normal", "High", "Normal", "Normal", "Normal", "High", "Normal", "High"],
    ["Hot", "Hot", "Hot", "Mild", "Cool", "Cool", "Cool", "Mild", "Cool", "Mild", "Mild", "Mild", "Hot", "Mild"],
    ["weak", "strong", "weak", "weak", "weak", "weak", "strong", "strong", "weak", "weak", "weak", "strong", "strong", "weak"],
    ["no", "no", "yes", "yes", "yes", "no",  "yes",  "no",  "yes",  "yes",  "yes",  "yes",  "yes",  "no"]
]
from collections import Counter
import math
import Node

def calcItems(list_of_data, items):
    sam = 0
    for i in list_of_data:
        if i == items:
            sam += 1
    return sam

def calcMultiItems(list1, first_Item, list2, second_item):
    sam = 0
    i = 0
    while i != len(list1):
        if list1[i] == first_Item and list2[i] == second_item:
            sam += 1
        i += 1
    return sam

def calclists(data1, first_Item, number):
    sam1 = []
    sam2 = []
    i = 0
    while i != len(data1[0]):
        temp = []
    
        if data1[number][i] == first_Item and data1[4][i] == "yes":
            for k in range(len(Data)):
                temp.append(data1[k][i])
            # sam2.append(data1[4][i])
            sam1.append(temp)
            

        elif data1[number][i] == first_Item and data1[4][i] == "no":
            for k in range(len(Data)):
                temp.append(data1[k][i])     
            # sam2.append(data1[4][i])
            sam1.append(temp)

        i += 1
    
    # print(sam1, sam2)
    return sam1 

def Entropy(number_yes, number_no, len_data):
    p_yes = number_yes / len_data
    p_no  = number_no / len_data
    if p_yes == 0 or p_no == 0:
        return 0
    return -(p_yes) * math.log2(p_yes) - (p_no) * math.log2(p_no)


def Gain(s, v):
    n_yes = calcItems(s, "yes")
    n_no  = len(s) - n_yes
    entropy_s = Entropy(n_yes, n_no, len(s))
    
    items_v = Counter(v)
    items_minus = Counter(v)
    
    for i in items_v.keys():
        plus = calcMultiItems(v, i, s, "yes")
        minus = calcMultiItems(v, i, s, "no")
        items_minus[i] = minus + plus
        items_v[i] = Entropy(plus, minus, calcItems(v, i))
    

    calc_gain = 0
    for i, j in zip(items_v.keys(), items_minus.keys()):
        calc_gain -= - (items_minus.get(j) / len(s) * items_v.get(i))
        
    return entropy_s -  calc_gain
    
def headRoot(lists):
    root = -1

    for i in range(len(lists) - 1):
        
        if Gain(lists[len(lists) - 1], lists[i]) > Gain(lists[len(lists) - 1], lists[i+1]):
            root = i
        else:
            root = i + 1
            
        return root

def branchesGain(list1, list2, word):
    
    s, v = calclists(list1, "sunny", list2, "yes", "no")

    for i in range(len(list1) - 1):
        
        if Gain(lists[len(Data) - 1], lists[i]) > Gain(lists[len(lists) - 1], lists[i+1]):
            root = i
        else:
            root = i + 1
            
        return root
    return Gain(s, v)

root = headRoot(Data) # set the root data
rootBranches = Counter(Data[root]) # set branches of the root
print(rootBranches[0])

# for i in rootBranches:
sm = calclists(Data, "sunny", root)
print(sm)
for i in range(len(sm)):
    print(sm[i][4], sm[i][1])

