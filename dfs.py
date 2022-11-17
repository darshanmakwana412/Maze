from collections import deque

def solve(start, end):

    '''
    start => The starting node of the maze
    end => The ending node of the maze
    '''

    stack = deque([deque([start])])
    visited = []

    while stack:
        currPath = stack.pop()
        for node in currPath[-1].neighbours:
            if node == end:
                return currPath
            elif node != None:
                if node not in visited:
                    visited.append(node)
                    path = currPath.copy()
                    path.append(node)
                    stack.append(path)