def read_file_to_matrix(file_path):             #Function that reads the file and returns a matrix

    matrix = []

    with open(file_path, 'r') as file:

        for line in file:
            row = line.strip().split()
            matrix.append(row)

    return matrix

#TODO - get the file path from command line argument
if __name__ == "__main__":
    file_path = 'rec-star_m100_deg6.txt'
    matrix = read_file_to_matrix(file_path)

    color_list = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
    
    nodes = int(matrix[0][0])       #Get the number of nodes
    edges = int(matrix[0][1])       #Get the number of edges
    
    adj_matrix = [[0 for _ in range(nodes)] for _ in range(nodes)]   #Create an empty adjacency matrix
    low_degree_nodes = []           #List to store the nodes with degree <= 5

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

    print(low_degree_nodes)