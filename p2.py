# Project 1 problem 2

import sys
import numpy as np


# State class uitilized to make a DFS.
# A DFS is then simply an array of State objects.
class State:
	def __init__(self, transitions = [], accepting = False):
		self.transitions = transitions
		self.accepting = accepting

	# Add an outgoing transition to State
	def addTransition(self, transition):
		self.transitions.append(transition)


# Function creates a 2-diemnsional table for the first step of problem 2.
# i = 0 through k.
# j = digits permitted.
def makeTable(k, digits):
	table = [[None for i in range(len(digits))] for i in range(k)]

	count =  0
	for i in range(k):
		for j in range(len(digits)):
			iCATj = int( str(i) + str(digits[j]) )
			table[i][j] = iCATj % k
	
	return table


# Uses a BFS traveral to find the shortest path from u to an accepting state
# utilizing the State object
def BFS(G, u):
	visited = [0 for i in range(len(G))]
	parent = [0 for i in range(len(G))]
	q = []
	visited[u] = True
	q.append(u)

	while q:
		x = q.pop(0)
		for y in G[x].transitions:
			if visited[y] == False:
				visited[y] = True
				parent[y] = x
				q.append(y)
				if G[y].accepting == True:
					return findShortestPath(parent, y)

	return "No path found."


# Takes in the parent array generated by BFS, and the accepting state
# that trigerred BFS's call to this function
def findShortestPath(parent, end):
	path = [end]
	while path[-1] != 0:
		path.append(parent[path[-1]])
		path.reverse()
		return path


# MakeTable TEST CODE
#--------------------------------
print(np.matrix(makeTable(13, [2, 7])))
#--------------------------------


# BFS TEST CODE
#--------------------------------
# graph = []
# graph.append(State([1, 3]))
# graph.append(State([2, 4]))
# graph.append(State([4]))
# graph.append(State([5]))
# graph.append(State([5]))
# graph.append(State([], True))

# print BFS(graph, 0)
#--------------------------------
