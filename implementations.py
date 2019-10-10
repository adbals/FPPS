import networkx as nx
import Graph_TSP as Graph
import dataset_processing as D
import numpy as np
import matplotlib.pyplot as plt
import os
import adjMatrix as adj
import graph_visualizer as graphVis
from functools import partial

#Data directory names
dataDir = "datasetTSP"

while (True):
	try:
		instanceName = input("\nEnter the TSP directory you would like to approximate: ")
		adjMat_response = input("Do you have an adjacency matrix .txt file for your instance?(Y/N):")
        
		if adjMat_response.lower() in ['n','no'] :
			print ("Calculating your adjacency matrix...")
			adj.createAdjMatrixFile(instanceName)
			print ("Done! Your adjMatrix has been created.")
		sol_response = input("Do you have a solution .txt file for your instance?(Y/N): ")
		solExist = True
		if sol_response.lower() in ['n', 'no'] :
			print("That's alright! The 1-tree LB can be used as reference points for comparisons across the 3 algorithms. ")
			solExist = False
		
		#Feed in a directory which has your xy coordinates and your adjacency matrices
		instance_DS = D.dataset_processing(dataDir,instanceName, solExist)
		vis_response = input("Would you like visualizations for the algorithms? (Y/N): ")		
		break
	except (IOError, NameError):
		print("This is not a valid instance. Please put in a valid directory name! Please also make sure the  %s_s.txt file exists in the directory.")
	except (IndexError):
		print("Please make sure your %s_s.txt's first and last value are the same. ")
######################
###Initialization
######################
instance_graph = Graph.Graph_TSP(instance_DS.nodeDict,instance_DS.adjMatrix, instanceName, instance_DS.solution)
nodeDict = instance_graph.nodeDict

nearestNeighbor = instance_graph.nearestNeighbor()
greedy = instance_graph.greedy()
convHullTour, visualTour = instance_graph.convexhullInsert()
oneTreeLB= instance_graph.oneTreeBound()
upperBound = instance_graph.upperBound()

print("Cost for nearestNeighbor: " + str(instance_graph.cost(nearestNeighbor)))
print("NN Time :  " + str(instance_graph.cost(nearestNeighbor)/3))
print("Cost for greedy: " + str(instance_graph.cost(greedy)))
print("Greedy Time :  " + str(instance_graph.cost(greedy)/3))
print("Cost for Convex Hull Insertion : " + str(instance_graph.cost(convHullTour)))
print("ConvexHull Time:  " + str(instance_graph.cost(convHullTour)/3))
print("The one-tree Lower Bound is: " + str(oneTreeLB))

print("The Upper Bound (Calculated by 2*cost of MST) is: "  + str(upperBound))
if solExist:
	optimal = instance_DS.solution
	print("Optimal Cost : " + str(instance_graph.cost(optimal)))
if (vis_response.lower() in ['y','yes']):
	print("\nCreating your graph visualizations...")
	graph_visuals = graphVis.graph_visualizer(solExist)
	graph_visuals.snapshotMaker(instance_graph)
    
print('DONE!')