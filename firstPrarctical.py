from collections import deque
#imported a graph
graph = {
    "a": ["b", "c"],
    "b": ["a", "d", "e"],
    "c": ["a", "f"],
    "d": ["b"],
    "e": ["b"],
    "f": ["c"]
}
#using BFS with Queue
def bfs(start):
    visited = []   
    queue = [start]

    while queue:
        node = queue.pop(0)

        if node not in visited:
            visited.append(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return visited
#using DFS with Stack
def dfs(node, visited):
    visited.append(node)

    # Visit each connected node
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)
    return visited
    
start='a'
#printing the output
print("BFS traversal:",bfs(start))

print("DFS traversal:",dfs(start,[]))
