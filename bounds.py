import random
import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree

class Bounds:
	def __init__(self, nodeDict, adjMatrix):
		self.nodeDict = nodeDict
		self.adjMatrix = adjMatrix
		self.counts = len(nodeDict)
		self.edgeDict = {}
		for i in range(self.counts):
			for j in range(i+1, self.counts):
				vertices = (i,j)
				self.edgeDict[vertices] = self.adjMatrix[i,j]

	'''
	1-tree Bound 
	  	A form of lower bound that utilizes the 1-tree based on Chapter 7 of The Traveling Salesman Problem: A Computational Study by Cook
			1. Pick a random node v0.
 			2. Get the length of the MST after disregarding the random node. 
 			3. Let S be the sum of the cheapest two edges incident with the random node v0. 
 			4. Output the sum of 2 and 3.
 		The 1-Tree bound should approximately be 90.5% of the optimal cost. The best 1-Tree lower bound will be the maximum cost of the many MSTs we get.
 	'''
	def calculateOTB(self,adjMatrix):
		maxOTBLB = -10000000
		bestTree = []
		for initNode in range(0,self.counts):
			MSTedges = self.OTBHelper(adjMatrix,initNode)
			r = self.calcCost(MSTedges)
			# s is the sum of the cheapest two edges incident with the random node v0.
			s = 0
			edgeLengths = adjMatrix[initNode]	
			nodeNums = range(0,self.counts)
			twoNN = sorted(zip(edgeLengths, nodeNums))[1:3]	
			s = twoNN[0][0] + twoNN[1][0]
			temp = r + s
			if temp > maxOTBLB:
				maxOTBLB = temp
				oneTreeEdges = MSTedges[:]
				oneTreeEdges.append((initNode,twoNN[0][1]))
				oneTreeEdges.append((initNode,twoNN[1][1]))
				bestTree = oneTreeEdges
		return [maxOTBLB, bestTree]
	def calculateOptimalOTB(self,adjMatrix):
		minOTBLB = 1000000
		bestTree = []
		for initNode in range(0,self.counts):
			MSTedges = self.OTBHelper(adjMatrix,initNode)
			r = self.calcAdjustedCost(MSTedges, adjMatrix)
			# s is the sum of the cheapest two edges incident with the random node v0.
			s = 0
			edgeLengths = adjMatrix[initNode]	
			nodeNums = range(0,self.counts)
			twoNN = sorted(zip(edgeLengths, nodeNums))[1:3]	
			s = twoNN[0][0] + twoNN[1][0]
			temp = r + s
			if temp < minOTBLB:
				minOTBLB = temp
				oneTreeEdges = MSTedges[:]
				oneTreeEdges.append((initNode,twoNN[0][1]))
				oneTreeEdges.append((initNode,twoNN[1][1]))
				bestTree = oneTreeEdges
		return [minOTBLB, bestTree]
	def OTBHelper(self,adjMatrix,initNode):
		#Create an AdjMatrix without the row & col containing the initNode
		newAdjMat = adjMatrix
		newAdjMat = np.delete(newAdjMat,initNode,axis= 0)
		newAdjMat = np.delete(newAdjMat,initNode,axis = 1)
		#Calculate MST length without the initNode
		mst = minimum_spanning_tree(newAdjMat)
		MSTedges = []
		Z = mst.toarray().astype(float)
		for i in range(len(Z)):
			array = np.nonzero(Z[i])[0]
			for index in array:
				x = i
				y = index
				if i >= initNode:
					x +=1
				if index >= initNode:
					y +=1 
				tuplex = (x,y)
				MSTedges.append(tuplex)
		return MSTedges
	def calcAdjustedCost(self,MSTedges, adjMatrix):
		r = 0
		for edge in MSTedges:
			r += adjMatrix[edge[0],edge[1]]
		return r
	def calcCost(self,MSTedges):
		# r is the length of the MST we have without the initNode
		r = 0
		for edge in MSTedges:
			checkEdge = edge
			if (checkEdge not in self.edgeDict):
				checkEdge = (edge[1],edge[0])
			r += self.edgeDict[checkEdge]
		return r
	'''
	  MST Upper Bound 
	    Simply 2* the MST cost of the original dataSet
	'''
	def calculateMSTUpperBound(self):
		mst = minimum_spanning_tree(self.adjMatrix)
		MSTedges = []
		Z = mst.toarray().astype(float)
		for i in range(len(Z)):
			array = np.nonzero(Z[i])[0]
			for index in array:
				tuplex = (i,index)
				MSTedges.append(tuplex)
		cost = 0
		for edge in MSTedges:
			checkEdge = edge
			if (checkEdge not in self.edgeDict):
				checkEdge = (edge[1],edge[0])
			cost += self.edgeDict[checkEdge]
		return 2*cost