from util import Node, StackFrontier, QueueFrontier

def main():
    start = (0,0)
    end = (4,0)

    maze = getmaze()

    path = getpath(maze, start, end)
    if path:
        print("Path found:")
        for rows in range(len(maze)):
            for collumns in range(len(maze[0])):
                if (rows, collumns) in path:
                    print("x", end=" ")
                else:
                    print(maze[rows][collumns], end=" ")
            print()
    else:
        print("No path found.")


def getpath(maze, start, end):

    begin = Node(state=start, parent=None, action=None)
    frontier = QueueFrontier()
    frontier.add(begin)

    explored = set()

    while not frontier.empty():
        node = frontier.remove()

        if node.state == end:
            path = []

            while node.parent is not None:
                path.append(node.state)
                node = node.parent
            path.append(start)
            path.reverse()
            return path

        explored.add(node.state)

        for neighbor in neighbors(maze, node.state):
            if neighbor not in explored and not frontier.contains_state(neighbor):
                child = Node(state=neighbor, parent=node, action=None)
                frontier.add(child)
    return None


def neighbors(maze, state):
    row, col = state
    neighbors = []
    rows = len(maze)
    cols = len(maze[0])

    for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
        if 0 <= r < rows and 0 <= c < cols and maze[r][c] == 0:
            neighbors.append((r, c))

    return neighbors


def getmaze():
    maze = []
    row = []

    with open("maze.txt") as file:
        for line in file:
            row = [int(char) for char in line if char != ' ' and char != '\n']
            maze.append(row)
    return maze


if __name__ == "__main__":
    main()
