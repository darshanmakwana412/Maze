import random

def RecursiveBacktracker(maze):
    stack = [] 
    stack.append(maze.maze[0][0])

    while len(stack)>0: 
        current = stack[-1]
        neighbours = []
        for key, n in enumerate(current.neighbours):
            if n!=None and n.visited==False:
                neighbours.append((key, n))

        if len(neighbours)==0:
            stack.pop()
        else:
            key, neighbour = random.choice(neighbours)
            current.connect(key)
            neighbour.connect((key+2)%4)
            stack.append(neighbour) 
            neighbour.visited = True

    return maze