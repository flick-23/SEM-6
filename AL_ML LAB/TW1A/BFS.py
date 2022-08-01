# BFS
from collections import deque
from collections import defaultdict

class Graph:
    # constructor
    def __init__(self):
        self.graph = defaultdict(list)

    # add edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # BFS
    def BFS(self, s):
        # create a queue, enqueue source vertex and mark source vertex as visited
        queue = []
        visited = []
        # add source to queue
        queue.append(s)
        # mark source vertex as visited
        visited.append(s)
        # while queue is not empty
        while queue:
            # dequeue a vertex from queue
            s = queue.pop(0)
            print(s, end=' ')
            # get all adjacent vertices of dequeued vertex s
            for i in self.graph[s]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)


g = Graph()
g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('A', 'D')
g.addEdge('B', 'E')
g.addEdge('B', 'F')
g.addEdge('C', 'G')
g.addEdge('C', 'I')
g.addEdge('D', 'I')

print("BFS with starting node A : ", end=' ')
g.BFS('A')
