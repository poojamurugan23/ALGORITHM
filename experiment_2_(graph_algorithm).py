# -*- coding: utf-8 -*-
"""Experiment : 2 - (Graph_Algorithm).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1C8ZUOKjBLlS8CKkWkbfQAIVhNQqi28_1
"""

import time
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def add_edge(self, u, v):
        self.graph[u].append(v)
    def BFS(self, s):
        visited = [False] * (len(self.graph))
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
    def time_taken(self, s):
        print("\nTime taken to run BFS:")
        start_time = time.time()
        self.BFS(s)
        end_time = time.time()
        return end_time - start_time
if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    print("Following is Breadth First Traversal starting from vertex 2:")
    time_taken = g.time_taken(2)
    print("Time taken: ", time_taken)

import time

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, v, w):
        self.adj_list[v].append(w)
        self.adj_list[w].append(v)

    def DFS(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=' ')
        for v in self.adj_list[vertex]:
            if not visited[v]:
                self.DFS(v, visited)

def time_taken(graph, vertex):
    print("Time of my program:")
    start = time.time()
    visited = [False] * graph.num_vertices
    graph.DFS(vertex, visited)
    end = time.time()
    return end - start

if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    print("Following is DFS from (starting from vertex 2)")
    print("Time taken:", time_taken(g, 2), "seconds")

import heapq
import time

def dijkstra(graph, start):
    distances = [float('inf')] * len(graph)
    distances[start] = 0
    heap = [(0, start)]
    while heap:
        dist, curr = heapq.heappop(heap)
        if dist > distances[curr]:
            continue
        for neighbor, weight in graph[curr].items():
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
def time_taken(graph, start):
    print("Time taken by dijkstra function:")
    start_time = time.time()
    dijkstra(graph, start)
    end_time = time.time()
    return end_time - start_time
if __name__ == "__main__":
    graph = {
        0: {1: 4, 7: 8},
        1: {0: 4, 2: 8, 7: 11},
        2: {1: 8, 3: 7, 8: 2, 5: 4},
        3: {2: 7, 4: 9, 5: 14},
        4: {3: 9, 5: 10},
        5: {2: 4, 3: 14, 4: 10, 6: 2},
        6: {5: 2, 7: 1, 8: 6},
        7: {0: 8, 1: 11, 6: 1, 8: 7},
        8: {2: 2, 6: 6, 7: 7}
    }
    start = 0
    distances = dijkstra(graph, start)
    print("The shortest distances from vertex {} to all other vertices are: {}".format(start, distances))
    elapsed_time = time_taken(graph, start)
    print("Time taken by dijkstra function: {} seconds".format(elapsed_time))

fromcollections import defaultdict
import sys
import time
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))
    def primMST(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v, weight in self.graph[u]:
                if not mstSet[v] and key[v] > weight:
                    key[v] = weight
                    parent[v] = u
        self.printMST(parent)
    def minKey(self, key, mstSet):
        min = sys.maxsize
        min_index = -1
        for v in range(self.V):
            if key[v] < min and not mstSet[v]:
                min = key[v]
                min_index = v
        return min_index
    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            weight = self.getWeight(i, parent[i])
            print(parent[i], "-", i, "\t", weight)
    def getWeight(self, i, parent):
        for v, weight in self.graph[i]:
            if v == parent:
                return weight
        return None
def time_taken(graph):
    print("Time of my program")
    s = time.time()
    graph.primMST()
    return time.time() - s
g = Graph(5)
g.addEdge(0, 1, 2)
g.addEdge(0, 3, 6)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 8)
g.addEdge(1, 4, 5)
g.addEdge(2, 4, 7)
g.addEdge(3, 4, 9)
t = time_taken(g)
print("Time taken:", t)

import time
import matplotlib.pyplot as plt
def floydWarshall(graph):
    V = len(graph)
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
def time_taken(graph):
    print("Time taken by my program:")
    s = time.time()
    floydWarshall(graph)
    return time.time() - s
graph = [[0, 5, 99999, 99999],
         [50, 0, 15, 5],
         [30, 99999, 0, 99999],
         [15, 99999, 5, 0]]
print(floydWarshall(graph))
print(time_taken(graph))

import time
import matplotlib.pyplot as plt

def transitiveClosure(graph):
    V = len(graph)
    reach = [[graph[i][j] for j in range(V)] for i in range(V)]  # Using list comprehension for clarity
    for k in range(V):
        for i in range(V):
            for j in range(V):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
    return reach

def time_taken(graph):
    print("Time taken to compute transitive closure:")
    start = time.time()
    transitiveClosure(graph)
    end = time.time()
    return end - start

# Example usage
graph = [[1, 1, 0, 1],
         [0, 1, 1, 0],
         [0, 0, 1, 1],
         [0, 0, 0, 1]]
print(transitiveClosure(graph))
print(time_taken(graph))