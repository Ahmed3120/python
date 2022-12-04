import numpy as np

data = [[7, 7], [7, 4], [3, 4], [1, 4]]



k = 3
x1 = 3
x2 = 7



def main():
    return

#method for get the distance of the elements
def distances(data, x1, x2, k):
    distance = []
    for i in range(len(data)):
        for j in range(len(data[i]) - 1):
            dist = np.sqrt((data[i][j]-x1)**2 + (data[i][j+1]-x2)**2)
            distance.append(abs(dist - k))
    
    for i in range(len(distance)):
        data[i].append(distance[i])


distances(data, x1, x2, k)

for i in range(len(data)):
    num = data[i][2]
    if num < 1:
        data[i].append("good")
    else:
        data[i].append("bad")
 
print(data)