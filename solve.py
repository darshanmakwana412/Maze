import argparse
import maze

def solve():

    parser = argparse.ArgumentParser()
    parser.add_argument('--maze', type=str, required=True, help='The path for the text file containing the maze')
    parser.add_argument('--method', type=str, required=True, help='The method for solving the maze')
    args = parser.parse_args()

    Maze = maze.Maze(args.maze)
    Maze.solve(args.method)

if __name__ == "__main__":
    solve()