from collections import Counter
from collections import OrderedDict

def hasTheChars(subString, word):
    isFound = False
    for i in subString:
        
        if i in word:
            isFound = True
        else:
            return False
    return isFound

#method used for remove repeated chars
def removeRepeatedChars(s):    
    #using orderdDict methods to remove the repeated chars   
    return "".join(OrderedDict.fromkeys(s))

def merageData(a, data):
    b = {}
    for i in a:
        for j in a:
            if i != j and i + j not in b.keys() and j + i not in b.keys():
                newWord = removeRepeatedChars(i + j)
                b[newWord] = 0
    for i in b:
        for j in data:
            if hasTheChars(i, j):
                b[i] += 1
    return b


#check if the data reptaion is bigger or less then the support
def checkSupport(data, support):
    newDic = {}
        
    for i in data:
            
        if data.get(i) >= support:
            newDic[i] = data.get(i)

    return newDic



def main(data, support):
    letter = []
    
    for i in data:
        for j in i:
            letter.append(j)
        
    
    a = dict(Counter(sorted(letter)))
    
    old = 0
    while len(a) > 1 :
        a = checkSupport(a, support)
        
        if a == old:
            print("Result : ", a)
            break

        print(a)
    
        a = merageData(a, data)
        old = a

        
        
    
inp = ["acd", "bce", "abce", "be"] 

support = 2
main(inp, support)

