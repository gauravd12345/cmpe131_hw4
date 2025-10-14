def cacti_number(plot):
    # ---- Input validation ----
    if not isinstance(plot, list):
        raise TypeError("Input must be a list of lists.")
    if len(plot) == 0:
        raise ValueError("Plot must not be empty.")
    row_len = None
    for row in plot:
        if not isinstance(row, list):
            raise TypeError("Each row must be a list.")
        if row_len is None:
            row_len = len(row)
            if row_len == 0:
                raise ValueError("Rows must not be empty.")
        elif len(row) != row_len:
            raise ValueError("All rows must have the same length (rectangle).")
        for cell in row:
            if not isinstance(cell, int) or cell not in (0, 1):
                raise TypeError("Cells must be integers 0 or 1.")

    r, c = len(plot), row_len

    # Ensure the initial plot has no illegal adjacencies (as stated, but we validate)
    def has_adjacent_one(i, j):
        return (
            (i > 0 and plot[i-1][j] == 1) or
            (i+1 < r and plot[i+1][j] == 1) or
            (j > 0 and plot[i][j-1] == 1) or
            (j+1 < c and plot[i][j+1] == 1)
        )

    for i in range(r):
        for j in range(c):
            if plot[i][j] == 1 and has_adjacent_one(i, j):
                raise ValueError("Input plot has adjacent cacti.")

    # ---- Greedy placement: scan top-left to bottom-right ----
    # Work on a copy so we can place new cacti as 1's
    grid = [row[:] for row in plot]
    added = 0

    for i in range(r):
        for j in range(c):
            if grid[i][j] == 0:
                up    = (i > 0     and grid[i-1][j] == 1)
                down  = (i+1 < r   and grid[i+1][j] == 1)
                left  = (j > 0     and grid[i][j-1] == 1)
                right = (j+1 < c   and grid[i][j+1] == 1)
                if not (up or down or left or right):
                    grid[i][j] = 1
                    added += 1

    return added