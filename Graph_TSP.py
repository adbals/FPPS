import algorithms
import bounds
class Graph_TSP:
	#Nodes should be a dictionary of key value pairing : node num to xy coordinates
	#Edges are implied in the adjacency matrix 
	#Adjacency matrix will be n x n; where n is the number of nodes
	def __init__(self, nodeDict, adjMatrix,instanceName, solution):
		self.nodeDict = nodeDict
		self.adjMatrix = adjMatrix
		self.counts = len(nodeDict)
		self.edgeDict = {}
		self.instanceName = instanceName
		self.solution = solution
		for i in range(self.counts):
			if self.counts > 1:
				for j in range(i+1, self.counts):
					vertices = (i,j)
					self.edgeDict[vertices] = self.adjMatrix[i,j]
		self.Bounds = bounds.Bounds(self.nodeDict, self.adjMatrix)
		self.solutions = algorithms.Algorithms(self.nodeDict, self.adjMatrix,self.counts, self.edgeDict)

	def oneTreeBound(self):
		return self.Bounds.calculateOTB(self.adjMatrix)[0]
	def upperBound(self):
		return self.Bounds.calculateMSTUpperBound()
	def randomSolution(self):
		return self.solutions.random()
	def nearestNeighbor(self):
		return self.solutions.nn()
	def greedy(self):
		return self.solutions.g()
	def convexhullInsert(self):
		return self.solutions.convHull()
	
	def cost(self,path):
		counter = 0
		for edge in path:
			checkEdge = edge
			if (checkEdge not in self.edgeDict):
				checkEdge = (edge[1],edge[0])
			counter += self.edgeDict[checkEdge]
		return counter

