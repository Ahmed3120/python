from numpy import sqrt

#,.;:<>

#the input of the function 
x1Array = [7, 7, 3, 1]
x2Array = [7, 4, 4, 4]

x1 = 3
x2 = 7
k = 3 # nearest element
tempArray = []
tempArray2 = []

for i, j in zip(x1Array, x2Array):
    distance = sqrt(pow((i - x1), 2) + pow((j - x2), 2))
    tempArray.append(distance)
    if  k - 1 <= distance < k + 1:
        tempArray2.append(1)
    else:
        tempArray2.append(0)


zippedArray = zip(x1Array, x2Array, tempArray, tempArray2)

for i in zippedArray:
    print(i)

