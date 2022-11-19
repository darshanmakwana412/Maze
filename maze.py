class Maze():
    class Node:
        def __init__(self, position):
            self.position = position
            self.neighbours = [None, None, None, None]
            self.weights = [0, 0, 0, 0]

    def __init__(self, maze):
        self.parse_txt(maze)
        self.create_dense_graph()

    def solve(self, method):
        if method == "bfs":
            import bfs
            path = bfs.solve(self.start, self.end)
            self.create_txt(path)
        elif method =="dfs":
            import dfs
            path = dfs.solve(self.start, self.end)
            self.create_txt(path)
        else:
            print("Invalid method provided")

    def create_txt(self, path):
        with open('solution.txt','w') as solution:
            maze = self.maze
            for node in list(path)[1:]:
                pos = node.position
                maze[pos[0]][pos[1]] = "o"
            
            for line in maze:
                solution.write(" ".join(line))
                solution.write("\n")
            

    def create_dense_graph(self):

        width = len(self.maze[0])
        height = len(self.maze)

        count = 0

        self.start = None
        self.end = None

        top_node_list = [None]*width
        left_node = None

        for i in range(height):
            for j in range(width):

                block = self.maze[i][j]

                if block in ["+", "-", "|"]:
                    # We have a wall
                    top_node_list[j] = None
                    left_node = None

                else:
                    # We have an empty cell
                    new_node = self.Node([i, j])
                    
                    if top_node_list[j] != None:
                        new_node.neighbours[0] = top_node_list[j]
                        top_node_list[j].neighbours[2] = new_node
                    top_node_list[j] = new_node

                    if left_node != None:
                        new_node.neighbours[3] = left_node
                        left_node.neighbours[1] = new_node
                    left_node = new_node

                    if block == "S":
                        # Yaay! we got the starting node
                        self.start = new_node
                    elif block == "E":
                        # Yaay! we got the ending node
                        self.end = new_node

                    count = count + 1
                
        print(f"Total nodes created: {count}")
        print(f"Starting Node: {self.start} at {self.start.position}")
        print(f"Starting Node: {self.end} at {self.end.position}")

    def parse_txt(self, txt_path):

        self.txt_path = txt_path

        with open(self.txt_path) as f:

            lines = f.readlines()
            maze = []

            for line in lines:
                maze_line = []
                for block in line[::2]:
                    if block != "\n":
                        maze_line.append(block)
                maze.append(maze_line)

            self.maze = maze