def read_file_to_matrix(file_path):             #Function that reads the file and returns a matrix

    matrix = []

    with open(file_path, 'r') as file:

        for line in file:
            row = line.strip().split()
            matrix.append(row)

    return matrix

if __name__ == "__main__":
    file_path = 'rec-star_m100_deg6.txt'
    matrix = read_file_to_matrix(file_path)

    nodes = matrix[0][0]
    edges = matrix[0][1]

    matrix = matrix[1:]

    print(nodes, edges)
    for row in matrix:
        print(row)