import sys
import os
import subprocess

def read_file_to_matrix(file_path):             #Function that reads the file and returns a matrix

    matrix = []

    with open(file_path, 'r') as file:

        for line in file:
            row = line.strip().split()
            matrix.append(row)

    return matrix


if __name__ == "__main__":
    #file_path = 'test_files/rec-star_m100_deg6.txt'
    if len(sys.argv) != 2:
        print("Usage: python main.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    output_file_path = file_path[:len(file_path)-4] + '_output.txt'
    matrix = read_file_to_matrix(file_path)
    
    nodes = int(matrix[0][0])       #Get the number of nodes
    edges = int(matrix[0][1])       #Get the number of edges
    
    adj_matrix = [[0 for _ in range(nodes)] for _ in range(nodes)]   #Create an empty adjacency matrix
    low_degree_nodes = []           #List to store the nodes with degree <= 5
    node_color = [0 for _ in range(nodes)]    # List to store the color of each node
    neighbors_color = []            #List to store the colors of the neighbors of a node

    matrix = matrix[1:]             #Remove the first row from the matrix

    for row in matrix:              #Populate the adjacency matrix
        
        #Since the nodes are 1-indexed, we need to subtract 1 from the node number to get the correct index
        adj_matrix[int(row[0])-1][int(row[1])-1] = 1    
        adj_matrix[int(row[1])-1][int(row[0])-1] = 1    #Since the graph is undirected, we need to add the edge in both directions

    aux_matrix = adj_matrix.copy()  #Create a copy of the adjacency matrix to keep track of the nodes with degree <= 5
    

    while len(low_degree_nodes) < nodes:    #Iterate until all the nodes are in the list

        for i in range(len(adj_matrix)):
            if sum(aux_matrix[i]) <= 5:
                if i not in low_degree_nodes:
                    low_degree_nodes.append(i)
                
                #Set the row and column of the node to 0 to remove the edges connected to the node
                aux_matrix[i] = [0 for _ in range(len(adj_matrix))]
                for j in range(len(aux_matrix)):
                    aux_matrix[j][i] = 0

    for i in reversed(low_degree_nodes): #Iterate through the nodes in reverse order

        for k in range(len(adj_matrix)):    #Iterate through the nodes to check the neighbors of the node
            if adj_matrix[i][k] == 1:       #If there is an edge between the nodes
                if node_color[k] != 0:   #If the node has a color assigned
                    neighbors_color.append(node_color[k])

        neighbors_color.sort() #Sort the colors of the neighbors in ascending order

        color = 1
        while color in neighbors_color:     #Check if the color is already assigned to a neighbor
            color += 1
        node_color[i] = color           #Assign the color to the node
        neighbors_color.clear()
            
    with open(output_file_path, 'w') as output_file:    #Write the output to a file
        for index, color in enumerate(node_color):
            output_file.write(f"{index+1} {color}\n")

    # Run check_coloring.jl
    result = subprocess.run(["julia", "check_coloring.jl", file_path, output_file_path], capture_output=True, text=True)

    if result.returncode != 0:
        print("Error running check_coloring.jl:")
        print(result.stderr)
    else:
        print("check_coloring.jl output:")
        print(result.stdout)