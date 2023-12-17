'''
Dijstras algorithm shortest path
Dijkstra's algorithm is a popular algorithm in computer science 
for finding the shortest path between nodes in a graph, which may represent, 
for example, road networks. 
The algorithm maintains a set of nodes whose shortest distance from the source is known. 
It repeatedly selects the node with the smallest tentative distance, updates the distances of its neighbors, and adds the node to the set of visited nodes. 
The process continues until the algorithm has visited all nodes or reached the destination.
'''
import sys

def dijkstra(graph, start):
    # Number of nodes in the graph
    num_nodes = len(graph)
    
    # Initialize distance array with infinity for all nodes
    distances = [float('inf')] * num_nodes
    
    # Distance from the start node to itself is 0
    distances[start] = 0
    
    # Set to keep track of visited nodes
    visited = set()
    
    while len(visited) < num_nodes:
        # Find the node with the smallest tentative distance
        current_node = min((node for node in range(num_nodes) if node not in visited), key=lambda x: distances[x])
        
        # Mark the current node as visited
        visited.add(current_node)
        
        # Update the distances of neighbors of the current node
        for neighbor in range(num_nodes):
            if graph[current_node][neighbor] > 0:  # There is a connection
                new_distance = distances[current_node] + graph[current_node][neighbor]
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
    
    return distances

# Example graph represented as an adjacency matrix
graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

start_node = 0
result = dijkstra(graph, start_node)
print("Shortest distances from node", start_node)
for i, distance in enumerate(result):
    print(f"To {i}: {distance}")
