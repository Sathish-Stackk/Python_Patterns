def zigzag(rows, cols):
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    for c in range(cols):
        if c % 2 == 0:
            for r in range(rows):
                matrix[r][c] = r * cols + c + 1
        else:
            for r in range(rows - 1, -1, -1):
                matrix[r][c] = (rows - 1 - r) * cols + c + 1
    for row in matrix:
        print(" ".join(str(x).rjust(2) for x in row))

zigzag(5, 5)
