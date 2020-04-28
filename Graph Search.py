from collections import defaultdict


# This class represents a directed graph using adjacency list representation
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    # function to add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

        # Use BFS to check path between s and d

    def edge_exists(self, s, d):
        # Mark all the vertices as not visited
        visited = [False] * (self.V)

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from queue
            n = queue.pop(0)

            # If this adjacent node is the destination node,
            # then return true
            if n == d:
                return True

            #  Else, continue to do BFS
            for i in self.graph[n]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        return False

    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print(s, end=" ")

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


# Create a graph given in the above diagram
g = Graph(11)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(4,5)
g.add_edge(2,5)
g.add_edge(6,2)
g.add_edge(7,1)
g.add_edge(10,2)
g.add_edge(3,8)
g.add_edge(2,7)
g.add_edge(8,7)
g.add_edge(8,2)
g.add_edge(10,4)
g.add_edge(4,3)
g.add_edge(3,6)
g.add_edge(2,5)
g.add_edge(2,9)
g.add_edge(2,4)
g.add_edge(5,1)
g.add_edge(5,3)
g.add_edge(5,9)
g.add_edge(6,10)
g.add_edge(7,4)
g.add_edge(7,10)
g.add_edge(7,9)

u = 1; v = 7

if g.edge_exists(u, v):
    print("There is a path from %d to %d" % (u, v))
else:
    print("There is no path from %d to %d" % (u, v))

u = 10; v = 9
if g.edge_exists(u, v):
    print("There is a path from %d to %d" % (u, v))
else:
    print("There is no path from %d to %d" % (u, v))

print ("The following is all vertices:")
g.BFS(0)
g.BFS(1)
g.BFS(2)
g.BFS(3)
g.BFS(4)
g.BFS(5)
g.BFS(6)
g.BFS(7)
g.BFS(8)
g.BFS(9)
g.BFS(10)