class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_matrix = [[0] * vertices for _ in range(vertices)]

    def is_safe(self, vertex, color, colors):
        for v in range(self.vertices):
            if self.adjacency_matrix[vertex][v] == 1 and colors[v] == color:
                return False
        return True

    def graph_coloring_util(self, num_colors, colors, vertex):
        if vertex == self.vertices:
            return True

        for color in range(1, num_colors + 1):
            if self.is_safe(vertex, color, colors):
                colors[vertex] = color
                if self.graph_coloring_util(num_colors, colors, vertex + 1):
                    return True
                colors[vertex] = 0

        return False

    def graph_coloring(self, num_colors):
        colors = [0] * self.vertices

        if not self.graph_coloring_util(num_colors, colors, 0):
            print("No solution exists.")
        else:
            print("Graph coloring solution:")
            for vertex in range(self.vertices):
                print(f"Vertex {vertex + 1}: Color {colors[vertex]}")


# Example usage
if __name__ == "__main__":
    # Create a graph
    graph = Graph(4)
    graph.adjacency_matrix = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]

    num_colors = 3  # Number of colors available
    graph.graph_coloring(num_colors)
