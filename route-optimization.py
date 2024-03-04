#Kabir Bose: 100862410

#used to make an infinite number (sys.maxsize)
from sys import maxsize

#the graph of distances remodelled using a dictionary
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

def shortest_path(graph,start,dest):
    costs = {} #holds costs of reaching each node in the graph
    pred = {} #holds predecessor of path that led to that node
    nodes = graph #to iterate through all nodes (essentially a temp variable)
    inf = maxsize #infinite number (max size from sys library)
    trace = [] #traces back all nodes

    #set the costs as infinity for all nodes
    for node in nodes:
        costs[node] = inf

    #set the cost of the source node to 0
    costs[start] = 0

    #loop through every single node in the graph
    while nodes:
        min_distance = None

        for node in nodes:

            #find the min_distance every time the graph is iterated
            if min_distance is None or costs[node] < costs[min_distance]:
                min_distance = node

        #for the node with the lowest cost find all possible items
        path_options = graph[min_distance].items()

        #continue calculating cost for each path and only update it if it is lower than the existing cost
        for child_node, weight in path_options:

            if weight + costs[min_distance] < costs[child_node]:
                costs[child_node] = weight + costs[min_distance]
                pred[child_node] = min_distance

        #remove any nodes that have already been visited
        nodes.pop(min_distance)

    #when the current node is equal to the destination node...
    currentNode = dest

    #trace back path to source node and calculate total cost
    while currentNode != start:
        try:
            trace.insert(0,currentNode)
            currentNode = pred[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    trace.insert(0,start)

    #if the cost is inf, the node had not been reached.
    if costs[dest] != inf:
        print('Shortest distance: ' + str(costs[dest]))
        print('Path to distance: ' + str(trace))

source = 'A'

#! Function can only be called once
# shortest_path(graph, source, 'H')
shortest_path(graph, source, 'K')
# shortest_path(graph, source, 'Q')
# shortest_path(graph, source, 'T')