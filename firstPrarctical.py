from collections import deque
#imported a graph
graph = {
    "1": ["2", "3"],
    "2": ["1", "4", "5"],
    "3": ["1", "6"],
    "4": ["2"],
    "5": ["2"],
    "6": ["3"]
}
#using BFS with Queue
def bfs(graph, start):
    visited = set()   
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
#using DFS with Stack
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    # Visit this node
    print(node, end=" ")
    visited.add(node)

    # Visit each connected node
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
#printing the output
print("BFS traversal:")
bfs(graph, "1")

print("\n\nDFS traversal:")
dfs(graph, "1")
