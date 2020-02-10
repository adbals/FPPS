import sklearn.neighbors as skln
import pandas as pd
import numpy as np
from math import pi
'''
dataset consist of lat and long
'''
instanceName = input ("File name : ")
dir = "dataset/%s/%s_xy.csv" % (instanceName,instanceName)
dataset = pd.read_csv(dir).to_numpy()

'''
Distance function is a calculation to create adjacency list
from dataset using NN to calculate distance to neighboring
nodes only.
Option 1: von Neumann; 4directions
Option 2: Moore ; 8directions
'''

#A = skln.kneighbors_graph(dataset,4,mode = 'distance',metric='haversine').toarray()
A = skln.kneighbors_graph(dataset,8,mode = 'distance',metric='haversine').toarray()

def matrix_to_list(matrix):
    graph = {}
    for i, node in enumerate(matrix):
        adj = []
        for j, connected in enumerate(node):
            if connected:
                adj.append(j)
        graph[i] = adj
    return graph

G=matrix_to_list(A)

'''
Algorithm to create back and forth flight pattern
'''

def bfs(graph, start):
    # keep track of all visited nodes
    visited = []
    # keep track of nodes to be checked
    queue = [start]

    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node not in visited:
            # add node to list of checked nodes
            visited.append(node)
            neighbours = graph[node]

            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)
    return visited

path = bfs(G,0)

gps_points = np.array([dataset[i] for i in path])

'''
Create waypoint from Algorithms

'''

def waypoint (gps_points,instanceName):
    print('Get home location')
    lat = input("Enter Latitude: ")
    long = input("Enter Longitude: ")
    alt = input("Enter Alt:")
    print ('\nGet Mission Parameters')
    hgt = input("Enter Mission Height:")
    spraytime = input('Enter Spray Time:')
    flow = input('Enter flow rate (%): ')

    flow1 = 1100 + (int(flow)*8)

    # Function to write mission file with cooordinates

    def mission_writing():
        x = 3*i+1
        y = 3*i+2
        z = 3*i+3
        file.write ('\n'+str(x)+'\t0\t10\t16\t1\t0\t0\t0\t'+str(gps_points[i, 0])+'\t'+str(gps_points[i, 1])+'\t'+str(hgt)+'\t1\n'+str(y)+'\t0\t10\t184\t9\t'+str(int(flow1))+'\t1\t'+str((int(spraytime)*2))+'	0	0	0	1')
        file.write ('\n'+str(z)+'\t0\t10\t93\t'+str(spraytime)+'\t0\t0\t0\t0\t0\t0\t1')

    # Write
    file = open("dataset/%s/%s_mission.txt"%(instanceName,instanceName),"w")
    file.write ('QGC WPL 110\n0	1	0	16	0	0	0	0\t'+str(lat)+'\t'+str(long)+'\t'+str(alt)+'\t1')

    nrows = len(gps_points)

    for i in range(nrows):
        mission_writing()
    print('Mission written as %s/%s_mission.txt'%(instanceName,instanceName))
    file.close()

def main():
    mission = waypoint(gps_points,instanceName)

    print("Path generated!")

if __name__ == '__main__':
    main()
