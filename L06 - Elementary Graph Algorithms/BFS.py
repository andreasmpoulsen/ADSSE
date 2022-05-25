"""
Breadth-First Search (BFS)

# Parameters
G:
    Input graph
s:
    Selected vertex

# Returns
A breadth-first tree, rooted on s
"""

def BFS(G, s):
    Q = []
    V = []

    Q.append(s)
    V.append(s)

    while Q:
        v = Q.pop(0)
        print(v, end = " ")

        for neighbor in G[v]:
            if neighbor not in V:
                V.append(neighbor)
                Q.append(neighbor)


if __name__ == "__main__":
    graph = {
        'A' : ['B','C'],
        'B' : ['D', 'E'],
        'C' : ['F'],
        'D' : [],
        'E' : ['F'],
        'F' : []
    }

    BFS(graph, 'A')

