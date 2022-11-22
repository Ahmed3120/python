import numpy as np
import random

def computeDistance(point1, point2):
    
    return (
        (
            (point1[0] - point2[0]) **2 +
            (point1[1] - point2[1]) **2
        ) ** 0.5
    )


data = [[1, 1, 0, 2, 3], [1, 0, 2, 4, 5]]
k = 2

coid0 = [data[0][0], data[1][0]]
coid1 = [data[0][1], data[1][1]]

# print(coid1, coid2)
clust = [[] for i in range(k)]

labels = []
for i in data:
    minDist = float('inf')
    label = None
    print(i)
    for j, centroid in enumerate([coid0, coid1]):
        newDist = computeDistance(i, centroid)
        print(newDist)
        if minDist > newDist:
            minDist = newDist
            label = i
    labels.append(label)
print(labels)






























# def randomVal(low, high):
#     return low + (high - low) * random.random()


# def initCentroids(data, k):
#     xMin = yMin = float('inf')
#     xMax = yMax = float('-inf')
    
#     for point in data:
#         xMin = min(point[0], xMin)
#         xMax = max(point[0], xMax)
#         yMin = min(point[1], yMin)
#         yMax = max(point[1], yMax)
        
#     centroids = []
#     for i in range(k):
#         centroids.append([randomVal(xMin, xMax), 
#                          randomVal(yMin, yMax)])
#     return centroids

#     # clusters = []
#     # random_sample
# def getLabels(data, centroids):
#     labels = []
    
#     for i in data:
#         minDist = float('inf')
#         label = None
        
#         for j, centroid in enumerate(centroids):
#             newDist = computeDistance(i, centroid)
#             if minDist > newDist:
#                 minDist = newDist
#                 label = i
#         labels.append(label)
#     return labels

# def computeDistance(point1, point2):
#     return np.sqrt(
#         (
#             (point1[0] - point2[0]) **2 +
#             (point1[1] - point2[1]) **2
#         )
#         )
    
# def reCalcCentroids(points, labels, k):
#     newCentroids = [[0,0] for i in range(k)]
#     counts = [0] * k
#     i = 0
#     for point, label in zip(points, labels):
#         # print(point, label)
#         # print(point[0])
#         # print()
#         newCentroids[i][0] += point[0]
#         newCentroids[i][1] += point[1]
#         counts[i] += 1
#         i += 1
#         # print(counts)
    
#     for i, (x, y) in enumerate(newCentroids): 
#         # print(i, x, y)
#         # print(counts[i])
#         newCentroids[i] = (x / counts[i], y / counts[i])
#     return newCentroids
    
# def isFinshed(oldCentroids, newCentroids, thr=1e-5):
#     totalMovement = 0
#     for oldPoint, newPoint in zip(oldCentroids, newCentroids):
#         totalMovement += computeDistance(oldPoint, newPoint)
#     return totalMovement < thr



# def main(data, k):
#     centroids = initCentroids(data, k)
#     print(centroids)
#     while True:
#         oldCentroids = centroids
#         labels = getLabels(data, centroids)
        
#         centroids = reCalcCentroids(oldCentroids, centroids, k)

#         if isFinshed(oldCentroids, centroids):
#             break
#     return labels, centroids
# k = 3
# data = [[15,15,16,19,19,20,20,21, 88, 10, 11], [22,28,35,40,41,42,43,44,60,61,65]]
# print(main(data, k))
# # print(int(random.random()))








# # centroids = initCentroids(data, k)
# # print(centroids)
# # counts = [0] * k

# # points = [10, 20, 30, 40, 50]
# # labels = [10, 20, 30, 40, 50]

# # newCentroids = [[0,0] for i in range(k)]    
# # for point, label in zip(points, labels):
# #     print(point)
# # print(newCentroids)
    



