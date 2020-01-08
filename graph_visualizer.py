import matplotlib.pyplot as plt
import networkx as nx
import Graph_TSP as Graph
import dataset_processing as D
import numpy as np
import matplotlib.pyplot as plt
import os

class graph_visualizer:
	def __init__(self,solExist):
		self.solExist = solExist
		return
	######################
	###Create Snapshots
	######################
	def snapshotMaker(self,dataGraph):
		algorithms = ["NearestNeighbor"]
		newDir = dataGraph.instanceName
		if not os.path.exists(newDir):
			os.makedirs(newDir)
		for alg in algorithms:
			newFolder = "%s/%s" % (dataGraph.instanceName, alg) 
			if not os.path.exists(newFolder):
			    os.makedirs(newFolder)
			if alg == "ConvHull":
				convHullTour,visualTour = dataGraph.convexhullInsert()
				self.snapshotConvHelper(dataGraph,visualTour, newFolder,alg)

	def snapshotConvHelper(self,dataGraph,algEdges, directory,alg):
		fig = plt.figure(figsize=(20,20))
		for i in range(0,len(algEdges)):
		    G = nx.Graph()
		    G.add_nodes_from(dataGraph.nodeDict.keys())
		    nx.draw_networkx_nodes(G,dataGraph.nodeDict,node_size=20,nodelist = dataGraph.nodeDict.keys(),node_color='r')
		    #For Visualization of Convex Hull Paths formed by algorithm, visualTour[i]
		    nx.draw_networkx_edges(G,dataGraph.nodeDict, edgelist = algEdges[i])
		    dtry = "%s/%s%s.png" % (directory,alg,i)
		    plt.savefig(dtry)
		    plt.clf()
		for n, p in dataGraph.nodeDict.items():
		    G.node[n]['pos'] = p
		plt.close('all')

	def snapshotHelper(self,dataGraph,algEdges, directory,alg):
		fig = plt.figure(figsize=(20,20))
		for i in range(0,len(algEdges)):
		    G = nx.Graph()
		    G.add_nodes_from(dataGraph.nodeDict.keys())
		    nx.draw_networkx_nodes(G,dataGraph.nodeDict,node_size=10,nodelist = dataGraph.nodeDict.keys(),node_color='r')
		    #For Visualization of Convex Hull Paths formed by algorithm, visualTour[i]
		    if i != len(algEdges)- 1:
		    	edgelist = algEdges[:i]
		    else:
		    	edgelist = algEdges
		    nx.draw_networkx_edges(G,dataGraph.nodeDict, edgelist = edgelist)
		    dtry = "%s/%s%s.png" % (directory,alg,i)
		    plt.savefig(dtry)
		    plt.clf()
		for n, p in dataGraph.nodeDict.items():
		    G.node[n]['pos'] = p
		plt.close('all')
