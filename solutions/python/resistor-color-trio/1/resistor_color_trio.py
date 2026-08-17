color_to_value = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}


def label(colors):
    value = (
        color_to_value[colors[0]] * 10
        + color_to_value[colors[1]]
    )

    value *= 10 ** color_to_value[colors[2]]

    units = ["ohms", "kiloohms", "megaohms", "gigaohms"]
    unit_index = 0

    # Use a larger unit only when no decimal is needed.
    while value >= 1000 and value % 1000 == 0:
        value //= 1000
        unit_index += 1

    return f"{value} {units[unit_index]}"