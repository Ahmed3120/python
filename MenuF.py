x = [10, 2, 12, 4, 62, 30, 32]

# c1 = x[int(len(x)/2)]
# c2 = x[int(len(x)/2) + 1]

# d1 = []
# d2 = []


# for i in range(len(x)):
#     res = x[i] - c1
#     d1.append(res)
    
# print(d1)

# for i in range(len(x)):
#     res = x[i] - c2
#     d2.append(res)
    
# print(d2)

# res
# for i in range(len(d1)):
#     res = d1[i-1] + d1[i]

# d1Centeroid = res/len(d1)

# for i in range(len(d2)):
#     res = d2[i-1] + d2[i]
    
# d2Centeroid = res/len(d2)
import numpy as np
import random

data = [15,15,16,19,19,20,20,21,22,28,35,40,41,42,43,44,60,61,65]
k = 2

c1 = 16
c2 = 22

num_iters = 2
num_clusters = 2

centroids = data
assigned_centroids = np.zeros(len(data), dtype = np.int32)

def computeDistance(x, coid):
    return np.sqrt(np.sum((x - coid) ** 2))

def compute_l2_distance(x, centroid):
    
       # Initialise the distance to 0
    dist = 0
    
    # Loop over the dimensions. Take sqaured difference and add to `dist` 
    dist += (centroid - x)**2
        
    return dist

def get_closest_centroid(x, centroids):
    
    centroid_distances = []
    
    # Loop over each centroid and compute the distance from data point.
    for centroid in centroids:
        dist = compute_l2_distance(x, centroid)
        centroid_distances.append(dist)
    
    # Get the index of the centroid with the smallest distance to the data point 
    closest_centroid_index =  min(range(len(centroid_distances)), key=lambda x: centroid_distances[x])
    
    return closest_centroid_index

def compute_sse(data, centroids, assigned_centroids):
    # Initialise SSE 
    sse = 0
    sse = compute_l2_distance(data, centroids[assigned_centroids]).sum() / len(data)
    
    return sse


# for n in range(num_iters):
    
#     # Loop over each data point
#     for i in range(len(data)):
#         x = data[i]
        
#         # x = x[None, :]   
        
#         # Get the closest centroid
#         closest_centroid = get_closest_centroid(x, centroids)
        
#         # Assign the centroid to the data point.
#         assigned_centroids[i] = closest_centroid
    
#     # Loop over centroids and compute the new ones.
#     for c in range(len(centroids)):
#         # Get all the data points belonging to a particular cluster
#         cluster_data = data[assigned_centroids == c]
        
#         # Compute the average of cluster members to compute new centroid
#         new_centroid = cluster_data.mean(axis = 0)
        
#         # assign the new centroid
#         centroids[c] = new_centroid
        
#     # Compute the SSE for the iteration
#     sse = compute_sse(data, centroids, assigned_centroids)
#     sse_list.append(sse)
    
# print(sse)
# print(centroids)
# print(assigned_centroids)
# grp = 0
# for x in range(k-1):
#     for y in arr:
#         res = int(np.sqrt(pow((y - x) , 2)))
#         if c1 >= res:
#             itration1.append(res)
#         else:
#             itration2.append(res)
#         grp = ((y-1) + y)
#     print(grp/len(arr))


# print(itration1)
# print(itration2)