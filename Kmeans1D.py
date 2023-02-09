import random

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

centroid1 = random.choice(array)
centroid2 = random.choice(array)

#here check if the centroids equl each other
if centroid1 == centroid2:
    centroid1 = random.choice(array)

#old centroids
oldCentroid1 = 0
oldCentroid2 = 0


#main loop
while oldCentroid1 != centroid1 and oldCentroid2 != centroid2:
    
    cluster1 = []
    cluster2 = []
    
    for i in range(len(array)) :
        
        dis = abs(centroid1 - array[i]) # return the absolute value of dis

        if dis > abs(centroid2 - array[i]) :
            cluster2.append(array[i])
            
        else :
            cluster1.append(array[i])

    print('cen',centroid1)
    print('cen',centroid2) 
            
    print('cluster1 = ',cluster1)
    print('cluster2 = ',cluster2)
    print("++++++++++++++++++++++++++++")
    oldCentroid1 = centroid1
    oldCentroid2 = centroid2   #append new centroid to old centroid variable
    
    centroid1 = sum(cluster1) / len(cluster1)
    centroid2 = sum(cluster2) / len(cluster2) #get new centroids sum function can sum all list element
 