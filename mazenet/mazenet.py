class Maze:

    class Node:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.neighbours = [None, None, None, None]
            self.links = [False, False, False, False]
            self.weights = [0, 0, 0, 0]
            self.visited = False
            self.type = "   "
            # North East South West

        def connect(self, key):
            self.links[key] = True

        def disconnect(self, key):
            self.links[key] = False

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.maze = self.initMaze()
        self.configureNodes()
    
    def initMaze(self):
        rows = []
        for i in range(self.rows):
            columns = []
            for j in range(self.columns):
                columns.append(self.Node(i,j))
            rows.append(columns)
        return rows  

    def getNeighbor(self, row, column):
        if not (0 <= row < self.rows):
            return None
        if not (0 <= column < self.columns):
            return None
        return self.maze[row][column]  

    def configureNodes(self):
        for i in range(self.rows):
            for j in range(self.columns):
                nodes = self.maze[i][j].neighbours
                nodes[0] = self.getNeighbor(i-1,j)
                nodes[1] = self.getNeighbor(i,j+1)
                nodes[2] = self.getNeighbor(i+1,j)
                nodes[3] = self.getNeighbor(i,j-1)

    def display(self):
        output = "+" + "---+" * self.columns + "\n"
        for i in range(self.rows):
            top = "|"
            bottom = "+"
            for j in range(self.columns):
                node = self.maze[i][j]
                body = node.type
                if node.links[1]:
                    east_boundary=" "
                else:
                    east_boundary="|"

                top = top + body + east_boundary
                if node.links[2]:
                    south_boundary="   "
                else:
                    south_boundary="---"

                corner = "+"
                bottom = bottom + south_boundary + corner
            
            output = output + top + "\n"
            output = output + bottom + "\n"
        return output

    def save(self, filename):
        with open(filename, "w") as f:
            f.writelines(self.display())
        f.close()

    def __str__(self):
        return self.display()