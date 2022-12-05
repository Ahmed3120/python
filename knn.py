import numpy as np

data = [[7, 7], [7, 4], [3, 4], [1, 4]]

k = 3
x1 = 3
x2 = 7


#method for get the distance of the elements
def distances(data, x1, x2, k):
    distance = []
    #range method here depend on the length of the data here the length is 2 it start form the 0 to 2
    # in the for j in line 22 here i put (data[i] - 1) to not throw out of index error
    for i in range(len(data)):
        for j in range(len(data[i]) - 1):
            dist = np.sqrt((data[i][j]-x1)**2 + (data[i][j+1]-x2)**2)

            #here i get the abslote value of the (dist - k) to know if its near the element or no throw
            #for in line 36
            distance.append(abs(dist - k))
    
    #append is used to put element in array
    for i in range(len(distance)):
        data[i].append(distance[i])


distances(data, x1, x2, k)

for i in range(len(data)):
    num = data[i][2]
    if num < 1:
        data[i].append(1)
    else:
        data[i].append(0)
 
print(data)
