def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    word = "XMAS"
    word_length = len(word)
    count = 0

    # Directions: (row_step, col_step)
    directions = [
        (0, 1),   # Right
        (0, -1),  # Left
        (1, 0),   # Down
        (-1, 0),  # Up
        (1, 1),   # Down-right diagonal
        (1, -1),  # Down-left diagonal
        (-1, 1),  # Up-right diagonal
        (-1, -1)  # Up-left diagonal
    ]

    def is_valid_position(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def find_word_from_position(r, c, dr, dc):
        # Check if "XMAS" starts from (r, c) in direction (dr, dc)
        for i in range(word_length):
            nr, nc = r + dr * i, c + dc * i
            if not is_valid_position(nr, nc) or grid[nr][nc] != word[i]:
                return False
        return True

    # Traverse every position in the grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "X":  # Only start search from 'X'
                for dr, dc in directions:
                    if find_word_from_position(r, c, dr, dc):
                        count += 1

    return count


# Example Grid (replace this with your actual input)
grid = [
"....XXMAS.",
".SAMXMS...",
"...S..A...",
"..A.A.MS.X",
"XMASAMX.MM",
"X.....XA.A",
"S.S.S.S.SS",
".A.A.A.A.A",
".A.A.A.A.A",
"..M.M.M.MM",
".X.X.XMASX"
]

# Count occurrences of "XMAS"
result = count_xmas(grid)
print("Occurrences of 'XMAS':", result)
