import numpy as np

k = 3
data = [15,15,16,19,19,20,20,21,22,28,35,40,41,42,43,44,60,61,65]


def computeDistance(c, d):
    return np.sqrt(
        
        (c - d) ** 2
        
    )

def upDateCenter(k):
    smu = 0
    for i in k:
        smu += i
    return smu/len(k)

centroids = [16, 22]


clusters = []

for c in centroids:
    oldDist = float('inf')
    clst = []
    for d in data:
        newDist = computeDistance(c, d)
        if oldDist > newDist:
            oldDist = newDist
            print(newDist)
            clst.append(d)
            
    clusters.append(clst)

counts = 0
for k in clusters:
    
    print(k, "dd")
    centroids[counts] = upDateCenter(k)
    counts += 1

print(centroids)
print(clusters) 

# while oldCoid != centroid1 and oldCoid2 != centroid2:
    
#        cluster1 = []
#        cluster2 = []
       
#        for i in range(len(array)) :
#            dis = centroid1 - array[i]
#            dis = abs(dis)
#            print('  ',array[i])
#            if dis > abs(centroid2 - array[i]) :
#                cluster2.append(array[i])
#            else :
#                cluster1.append(array[i])
        
#        sum = 0
#        sum2 = 0
       
#     #    print('cluster1 = ',cluster1)
#     #    print('cluster2 = ',cluster2)
       
#        for i in range(len(cluster1)) :
#            sum =  sum + cluster1[i]
    
#        for i in range(len(cluster2)) :
#            sum2 = sum2 + cluster2[i]
        
#        oldCoid = centroid1
#        oldCoid2 = centroid2   
#        centroid1 = int(sum / len(cluster1))
#        centroid2 = int(sum2 / len(cluster2))
#        print('cen',centroid1,' ', sum)
#        print('cen',centroid2,' ', sum2)











# def reCalcCentroids():  
#     for k in range(K):  
#         if sum(classifications == k) > 0:  
#             centroids[k] = sum(points[classifications == k]) / sum(classifications == k)  

# #first initilize the centroid randomly
# coid = np.random.choice(data, k, False)
# clusters = []
# def createCluster(k, centeroid):
#     clusters = [[] for _ in range(k)]
#     distances = [computeDistance(sample, point) for point in centroids]
#     closest_index = np.argmin(distances)
    
# print(clusters)
# def _closest_centroid(centroids):
#         # distance of the current sample to each centroid
#         distances = [computeDistance(data, point) for point in centroids]
#         closest_index = np.argmin(distances)
#         return closest_index
# print(_closest_centroid(coid))

# print(_closest_centroid(53, coid))









# last_Centroids = centroids + 1  
# while not np.array_equal(centroids, last_Centroids):  
#     last_Centroids = np.copy(centroids)  
#     reCalcCentroids()  
#     assignPntsToCentroids()  
#     iteration += 1  
#     updatePlot(iteration)  
