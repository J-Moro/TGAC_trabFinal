## Overview

This project implements an algorithm that takes a graph as input and colors it according to the 6-Color Theorem. The theorem guarantees that any planar graph can be colored with at most six colors, ensuring no two adjacent vertices share the same color.

## Features

- Accepts a graph as input in the given format (specified below).
- Implements an efficient algorithm to color the graph using at most six colors.
- Provides a file with the color assigned to each node.

## Installation

Step-by-step instructions on how to get the development environment running.

```bash
# Clone the repository
git clone https://github.com/J-Moro/graph-coloring.git

# Navigate to the project directory
cd graph-coloring

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Input Format

The graph should be provided in a plain text file where the first line contains two numbers (in base 10) separated by a space. The first number represents the number of nodes 𝑛, and the second represents the number of edges 𝑚. The following 𝑚 lines each contain two numbers (in base 10) separated by a space (both between 1 and 𝑛) indicating the existence of an edge between these nodes.
The nodes are numbered starting from 1 (up to 𝑛). The graph is simple, so edges are bidirectional (i.e., 
23 is the same as 32). The file contains 𝑚+ 1 lines in total. Test files may include up to 1000 nodes and 3×1000−6 edges.
  
### Running the Program
To color a graph, run the following command:

```bash
python main.py --input graph.txt --output
```
-   `--input`: Path to the input file containing the graph.
    
-   `--output`: (Optional) Path to save the visualization of the colored graph.

### Output
The program outputs a list of colors assigned to each vertex.
The output format consists of 𝑛 lines, each line containing two numbers (in base 10) separated by a space. The first number represents a node, and the second represents the color assigned to the node (a number from 1 to 6).


## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

## Contact

- Julia - [moronunes.julia@gmail.com](mailto:moronunes.julia@gmail.com)
- Project Link: [https://github.com/J-Moro/graph-coloring](https://github.com/J-Moro/graph-coloring)

## Aknowledgements

This project was made with help from Chat GPT and Github Copilot. In addition, the following pages were consulted as references:
- https://rollbar.com/blog/how-to-fix-indexerror-list-assignment-index-out-of-range-python/