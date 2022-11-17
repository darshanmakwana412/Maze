from collections import deque

def solve(start, end):

    queue = deque([deque([start])])
    visited = []

    while queue:
        currPath = queue.popleft()
        for node in currPath[-1].neighbours:
            if node == end:
                return currPath
            elif node != None:
                if id(node) not in visited:
                    visited.append(id(node))
                    path = currPath.copy()
                    path.append(node)
                    queue.append(path)