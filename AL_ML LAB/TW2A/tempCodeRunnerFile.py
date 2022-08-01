from collections import defaultdict

graph = defaultdict(list)


def addEdge(u, v, c):
    graph[u].append([v, c])


def best(start, goal):
    open = []
    visited = []
    closed = []
    open.append([start, 0])
    visited.append(start)
    while open:
        curNode = open.pop(0)[0]
        closed.append(curNode)
        print("At node : ", curNode)
        print("Close : ", closed)
        for v, c in graph[curNode]:
            if v not in visited:
                open.append([v, c])
                visited.append(v)
        print("Unsorted open : ", open)
        open.sort(key=lambda x: x[1])
        print("Sorted open : ", open, "\n")
    return False


addEdge('S', 'A', 3)
addEdge('S', 'B', 6)
addEdge('S', 'C', 5)
addEdge('A', 'E', 8)
addEdge('A', 'D', 9)
addEdge('B', 'G', 14)
addEdge('B', 'F', 12)
addEdge('C', 'H', 7)
addEdge('H', 'J', 6)
addEdge('H', 'I', 5)
addEdge('I', 'M', 2)
addEdge('I', 'L', 10)
addEdge('I', 'K', 1)

if best('S', 'I'):
    print("Path found")
else:
    print("Path not found!")
