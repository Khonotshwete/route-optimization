#Kabir Bose: 100862410
#Zuhaib Shafi:
#Matthew Allicock:
#Khono Tshwete: 100885011

# the source node that the user will choose
src = input("Enter a source node from A to W (eg. S): ").capitalize()

#the graph of distances remodelled using a dictionary
graph = {
    'A': {'B':6, 'F': 5},
    'B': {'A':6, 'C':5, 'G':6},
    'C': {'B':5, 'D':7, 'H':5},
    'D': {'C':7, 'E':7, 'I':8},
    'E': {'D':7, 'I':6, 'N':15},
    'F': {'A':5, 'G':8, 'J':7},
    'G': {'B':6, 'F':8, 'H':9, 'K':8},
    'H': {'C':5, 'G':9, 'I':12}, #charger
    'I': {'D':8, 'E':6, 'H':12, 'M':10},
    'J': {'F':7, 'K':5, 'O':7},
    'K': {'G':8, 'J':5, 'L':7}, #charger
    'L': {'K':7, 'M':7},
    'M': {'I':10, 'L':7, 'N':9},
    'N': {'E':15, 'M':9, 'R':7},
    'O': {'J':7, 'P':13, 'S':9},
    'P': {'L':7, 'O':13, 'Q':8, 'U':11},
    'Q': {'P':8, 'R':9}, #charger
    'R': {'N':7, 'Q':9, 'W':10},
    'S': {'O':9, 'T':9},
    'T': {'S':9, 'U':8}, #charger
    'U': {'P':11, 'T':8, 'V':8},
    'V': {'U':8, 'W':5},
    'W': {'R':10, 'V':5}
}

def shortest_path(graph, src, dest):
    # initialize distances as infinity, except for the source node set to 0
    distances = {node: 999999999 for node in graph}
    distances[src] = 0

    # keep track of the predecessors of each node to reconstruct the path
    predecessors = {node: None for node in graph}

    # keep track of visited nodes to avoid revisiting them
    visited = set()

    # while there are nodes yet to be visited
    while visited != set(graph.keys()):
        # select the unvisited node with the smallest distance
        current_node = None
        for node in graph:
            if node not in visited:
                if current_node is None:
                    current_node = node
                elif distances[node] < distances[current_node]:
                    current_node = node

        # visit the selected node
        visited.add(current_node)

        # for each neighbor of the current node
        for neighbor, cost in graph[current_node].items():
            # calculate the new distance to the neighbor
            new_distance = distances[current_node] + cost

            # if the new distance is smaller, update the shortest distance and predecessor for this neighbor
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current_node

        # if we've reached the destination, no need to continue
        if current_node == dest:
            break

    # reconstruct the shortest path from source to destination
    path = []
    current_node = dest
    while current_node is not None:
        path.append(current_node)
        current_node = predecessors[current_node]
    path.reverse()

    # return the shortest path and its cost
    return path, distances[dest]

def outputs():
    # all the paths and costs to each charger
    path1, cost1 = shortest_path(graph, src, 'H')
    path2, cost2 = shortest_path(graph, src, 'K')
    path3, cost3 = shortest_path(graph, src, 'Q')
    path4, cost4 = shortest_path(graph, src, 'T')

    paths_costs = {'H': cost1,'K': cost2,'Q': cost3,'T': cost4}

    def sort_dict_by_values(d):
        # sort the dictionary by its values
        sorted_dict = sorted(d.items(), key=lambda item: item[1])
    
        #get the smallest key based on the smallest value
        smallest_key = sorted_dict[0][0]
    
        # print the smallest key
        return smallest_key

    print(f"Path to H: {path1} with cost of {cost1}")
    print(f"Path to K: {path2} with cost of {cost2}")
    print(f"Path to Q: {path3} with cost of {cost3}")
    print(f"Path to T: {path4} with cost of {cost4}")

    print(f"\nThe closest charger is {sort_dict_by_values(paths_costs)}")

outputs()
