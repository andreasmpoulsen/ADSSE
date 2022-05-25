"""
Depth-First Search (DFS)

# Parameters
G:
    Input graph
u:
    Selected vertex
V:
    List of visited nodes

# Returns
A depth-first tree, rooted on u
"""

V = []

def DFS(G, u, V):
    if u not in V:
        print(u, end=" ")
        V.append(u)

        for child in G[u]:
            DFS(G, child, V)
        
if __name__ == "__main__":
    graph = {
        'A' : ['B','C'],
        'B' : ['D', 'E'],
        'C' : ['F'],
        'D' : [],
        'E' : ['F'],
        'F' : []
    }

    DFS(graph, 'A', V)