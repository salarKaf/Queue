class Queue:
    def __init__(self):
        self.items = []
        self.rear = 0
        self.front = 0

    def enqueue(self, item):
        self.rear = self.rear + 1
        self.items.append(item)

    def dequeue(self):
        if self.isEmpty():
            return "UnderFlow"
        else:
            self.front += 1
            return self.items.pop()

    def isEmpty(self):
        return self.rear == self.front

    def sizeOfQueue(self):
        return self.rear - self.front

def shortest_path(maze, start, end):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    rows, cols = len(maze), len(maze[0])
    visited = set()
    queue = Queue()

    queue.enqueue((start, 0))

    while not queue.isEmpty():
        current_pos, dist = queue.dequeue()

        if current_pos == end:
            return dist

        visited.add(current_pos)

        for dx, dy in directions:
            new_x =current_pos[0] + dx
            new_y =current_pos[1] + dy

            if 0 <= new_x < rows and 0 <= new_y < cols and maze[new_x][new_y] == 0 and (new_x, new_y) not in visited:
                queue.enqueue(((new_x, new_y), dist + 1))

    return -1


