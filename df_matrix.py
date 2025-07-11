def dfs_on_matrix(matrix, start_row, start_col, visited=None):
    if visited is None:
        visited = set()  # Create a set to keep track of visited cells

    rows = len(matrix)
    cols = len(matrix[0])

    # Check if the current cell is within the matrix bounds and not visited
    if (0 <= start_row < rows) and (0 <= start_col < cols) and (start_row, start_col) not in visited:
        visited.add((start_row, start_col))  # Mark the current cell as visited
        print("Visited cell at:", start_row, start_col, "value is ", matrix[start_row][start_col])

        # Define possible movements (up, down, left, right)
        movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Recur for all possible neighboring cells
        for dx, dy in movements:
            next_row, next_col = start_row + dx, start_col + dy
            dfs_on_matrix(matrix, next_row, next_col, visited)

# Example usage:
# Creating a matrix:
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]

# Performing DFS on the matrix
print("DFS traversal on the matrix:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("[1, 2, 3] \n[4, 5, 6] \n[7, 8, 9]")
dfs_on_matrix(matrix, 0, 0)