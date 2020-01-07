import Graph_TSP as Graph
import dataset_processing as D
import numpy as np
import adjMatrix as adj
import graph_visualizer as graphVis
import gen_path as GP
from collections import defaultdict

#Data directory names
dataDir = "datasetTSP"

while (True):
	try:
		instanceName = input("\nEnter the TSP directory you would like to approximate: ")
        
		adj.createAdjMatrixFile(instanceName)
		print ("Done! Your adjMatrix has been created.")
		
		solExist = False
		
		#Feed in a directory which has your xy coordinates and your adjacency matrices
		instance_DS = D.dataset_processing(dataDir,instanceName, solExist)
		vis_response = input("Would you like visualizations for the algorithms? (Y/N): ")		
		break
	except (IOError, NameError):
		print("This is not a valid instance. Please put in a valid directory name! Please also make sure the  %s_xy.txt file format is correct.")
	except (IndexError):
		print("Please make sure your %s_s.txt's first and last value are the same. ")
######################
###Initialization#####
######################
instance_graph = Graph.Graph_TSP(instance_DS.nodeDict,instance_DS.adjMatrix, instanceName, instance_DS.solution)
nodeDict = instance_graph.nodeDict

convHullTour, visualTour = instance_graph.convexhullInsert()
print("Cost for Convex Hull Insertion : " + str(instance_graph.cost(convHullTour)))
print("ConvexHull Time:  " + str(instance_graph.cost(convHullTour)/3))

if (vis_response.lower() in ['y','yes']):
	print("\nCreating your graph visualizations...")
	graph_visuals = graphVis.graph_visualizer(solExist)
	graph_visuals.snapshotMaker(instance_graph)

######################
###PROCESSING OUT#####
######################
    
adjx = defaultdict(set)
for x, y in convHullTour:
    adjx[x].add(y)
    adjx[y].add(x)

col = defaultdict(int)
def dfs(x, parent=None):
    if col[x] == 1: return True
    if col[x] == 2: return False
    col[x] = 1
    res = False
    for y in adjx[x]:
        if y == parent: continue
        if dfs(y, x): res = True
    col[x] = 2
    return res

for x in adjx:
    if dfs(x):
        print ("Path generated!")

coord_list = list(nodeDict.values())        
path = list(col.keys())
gps_points = np.array([coord_list[i] for i in path])

waypoint = GP.waypoint(gps_points,instanceName)


print('DONE!')
