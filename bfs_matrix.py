def bfs_on_matrix(matrix, start_row, start_col):
    rows = len(matrix)
    cols = len(matrix[0])

    # Define possible movements (up, down, left, right)
    movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    queue = [(start_row, start_col)]
    visited = set()  # Create a set to keep track of visited cells

    while queue:
        current_row, current_col = queue.pop(0)
        if (0 <= current_row < rows) and (0 <= current_col < cols) and (current_row, current_col) not in visited:
            visited.add((current_row, current_col))  # Mark the current cell as visited
            print("Visited cell at:", current_row, current_col, "value", matrix[current_row][current_col])

            # Check neighboring cells and add them to the queue
            for dx, dy in movements:
                next_row, next_col = current_row + dx, current_col + dy
                queue.append((next_row, next_col))

# Example usage:
# Creating a matrix:
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]

# Performing BFS on the matrix
print("BFS traversal on the matrix:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("[1, 2, 3]\n[4, 5, 6]\n[7, 8, 9]")
bfs_on_matrix(matrix, 0, 0)

