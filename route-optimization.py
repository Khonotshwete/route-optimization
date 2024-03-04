# Kabir Bose: 100862410

import sys
from heapq import heapify, heappush, heappop

# re-creates the graph from the diagram in python
graph = {
    'A': {'B':6, 'F': 5},
    'B': {'A':6, 'C':5, 'G':6},
    'C': {'B':5, 'D':7, 'H':5},
    'D': {'C':7, 'E':7, 'I':8},
    'E': {'D':7, 'I':6, 'N':15},
    'F': {'A':5, 'G':8, 'J':7},
    'G': {'B':6, 'F':8, 'H':9, 'K':8},
    'H': {'C':5, 'G':9, 'I':12},
    'I': {'D':8, 'E':6, 'H':12, 'M':10},
    'J': {'F':7, 'K':5, 'O':7},
    'K': {'G':8, 'J':5, 'L':7},
    'L': {'K':7, 'M':7},
    'M': {'I':10, 'L':7, 'N':9},
    'N': {'E':15, 'M':9, 'R':7},
    'O': {'J':7, 'P':13, 'S':9},
    'P': {'L':7, 'O':13, 'Q':8, 'U':11},
    'Q': {'P':8, 'R':9},
    'R': {'N':7, 'Q':9, 'W':10},
    'S': {'O':9, 'T':9},
    'T': {'S':9, 'U':8},
    'U': {'P':11, 'T':8, 'V':8},
    'V': {'U':8, 'W':5},
    'W': {'R':10, 'V':5}
}

def dijsktra(graph, src, dest):
    # infinite value to assign as a cost for all nodes as default
    inf = sys.maxsize

    # holds all predecessor nodes to get to a dest and the cost of the src node
    node_data = {
        'A': {'cost':inf, 'pred':[]},
        'B': {'cost':inf, 'pred':[]},
        'C': {'cost':inf, 'pred':[]},
        'D': {'cost':inf, 'pred':[]},
        'E': {'cost':inf, 'pred':[]},
        'F': {'cost':inf, 'pred':[]},
        'G': {'cost':inf, 'pred':[]},
        'H': {'cost':inf, 'pred':[]},
        'I': {'cost':inf, 'pred':[]},
        'J': {'cost':inf, 'pred':[]},
        'K': {'cost':inf, 'pred':[]},
        'L': {'cost':inf, 'pred':[]},
        'M': {'cost':inf, 'pred':[]},
        'N': {'cost':inf, 'pred':[]},
        'O': {'cost':inf, 'pred':[]},
        'P': {'cost':inf, 'pred':[]},
        'Q': {'cost':inf, 'pred':[]},
        'R': {'cost':inf, 'pred':[]},
        'S': {'cost':inf, 'pred':[]},
        'T': {'cost':inf, 'pred':[]},
        'U': {'cost':inf, 'pred':[]},
        'V': {'cost':inf, 'pred':[]},
        'W': {'cost':inf, 'pred':[]},
    }

    node_data[src]['cost'] = 0 # assigns the cost of src node to 0

    visited = [] # keeps track of all visited nodes

    temp = src # the neighbor node with the smallest cost for the node that is being visited

    for i in range(len(graph)-1): # run loop till all nodes are visited
        if temp not in visited: # check if temp node has been visited
            visited.append(temp)

            min_heap = []

            for j in graph[temp]: # check if neighbor has a minimum cost
                if j not in visited: # if neighbor is not visited
                    cost = node_data[temp]['cost'] + graph[temp][j] #add the cost to that neighbor
            
                    if cost < node_data[j]['cost']: # if neighbor costs are less than calculated cost
                        node_data[j]['cost'] = cost # assign the new costs to neighbors
                        node_data[j]['pred'] = node_data[temp]['pred'] + list(temp) # assign predecessor if low cost
                    
                    heappush(min_heap, (node_data[j]['cost'], j)) # push cost of every neighbor inside min_heap
        
        heapify(min_heap)
        temp = min_heap[0][1]
    
    print('Shortest distance: ' + str(node_data[dest]['cost']))
    print('Shortest path: ' + str(node_data[dest]['pred'] + list(dest)))
            
    return 0

dijsktra(graph, 'H', 'A')