"calculate the diamond based on the input"
def rows(letter):
    "Calculates the diamong based on the character input"
    target_index = ord(letter.upper()) - ord("A")
    result = []

    for row in range(2 * target_index + 1):
        index = min(row, 2 * target_index - row)
        current_letter = chr(ord("A") + index)
        outer_spaces = " " * (target_index - index)

        if index == 0:
            line = outer_spaces + "A" + outer_spaces
        else:
            inner_spaces = " " * (2 * index - 1)
            line = (
                outer_spaces
                + current_letter
                + inner_spaces
                + current_letter
                + outer_spaces
            )

        result.append(line)

    return result