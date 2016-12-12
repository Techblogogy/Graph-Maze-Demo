from collections import deque
import pprint as pp

graph = {}

visited = {}

def addVertex(v):
    if v not in graph:
        graph[v] = {}

def addEdge(v1, v2):
    if (v1 in graph) and (v2 in graph):
        graph[v1][v2] = True
        graph[v2][v1] = True

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if i not in visited:
            print v, ">", i
            dfs(i)

def bfs(v):
    items = deque([])

    items.append(v)
    visited[v] = True

    while items:
        top = items.popleft()
        print top

        for i in graph[top]:
            if i not in visited:
                items.append(i)
                visited[i] = True



addVertex("John")
addVertex("Dave")
addVertex("Anna")
addVertex("George")
addVertex("Tanya")


addEdge("John", "Tanya")

addEdge("Anna", "George")
addEdge("Anna", "John")
addEdge("Anna", "Dave")

addEdge("Tanya", "Anna")
addEdge("Tanya", "Dave")
addEdge("Tanya", "George")


pp.pprint(graph)

dfs("George")
visited = {}
bfs("George")
