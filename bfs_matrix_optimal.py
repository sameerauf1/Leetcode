from collections import deque

def bfs_on_matrix(matrix, start_row, start_col):
    rows = len(matrix)
    cols = len(matrix[0])

    # Define possible movements (up, down, left, right)
    movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    queue = deque()
    queue.append((start_row, start_col))
    visited = set()  # Keep track of visited cells

    while queue:
        current_row, current_col = queue.popleft()  # O(1) instead of O(n)
        
        # Check bounds and whether it's visited
        if (0 <= current_row < rows and 
            0 <= current_col < cols and 
            (current_row, current_col) not in visited):
            
            visited.add((current_row, current_col))
            print("Visited cell at:", current_row, current_col, 
                  "value", matrix[current_row][current_col])

            # Add neighbors to the queue
            for dx, dy in movements:
                next_row = current_row + dx
                next_col = current_col + dy
                queue.append((next_row, next_col))

# Example usage:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("BFS traversal on the matrix:")
bfs_on_matrix(matrix, 0, 0)

#note must use deque for O(1) pop operation