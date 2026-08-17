"Based on garden input createa minesweeper view"
def annotate(garden):
    "Based on garden input createa minesweeper view"
    if not garden:
        return []

    width = len(garden[0])

    # Validate that the garden is rectangular
    # and contains only spaces or flowers.
    for row in garden:
        if len(row) != width:
            raise ValueError("The board is invalid with current input.")

        if any(cell not in (" ", "*") for cell in row):
            raise ValueError("The board is invalid with current input.")

    result = []

    for row_index, row in enumerate(garden):
        annotated_row = []

        for col_index, cell in enumerate(row):
            if cell == "*":
                annotated_row.append("*")
                continue

            flower_count = 0

            for row_offset in (-1, 0, 1):
                for col_offset in (-1, 0, 1):
                    # Skip the current square itself.
                    if row_offset == 0 and col_offset == 0:
                        continue

                    neighbor_row = row_index + row_offset
                    neighbor_col = col_index + col_offset

                    if (
                        0 <= neighbor_row < len(garden)
                        and 0 <= neighbor_col < width
                        and garden[neighbor_row][neighbor_col] == "*"
                    ):
                        flower_count += 1

            if flower_count == 0:
                annotated_row.append(" ")
            else:
                annotated_row.append(str(flower_count))

        result.append("".join(annotated_row))

    return result