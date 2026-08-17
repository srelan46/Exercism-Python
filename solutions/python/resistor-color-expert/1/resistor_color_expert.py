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
color_to_tolerance = {
    "grey" : "0.05%",
    "violet" : "0.1%",
    "blue" : "0.25%",
    "green" : "0.5%",
    "brown" : "1%",
    "red" : "2%",
    "gold" : "5%",
    "silver" : "10%"
}

def resistor_label(colors):
    length = len(colors)
    units = ["ohms", "kiloohms", "megaohms", "gigaohms"]
    value = 0
    tolerance = 0
    unit_index = 0
    if length==1:
        return str(color_to_value[colors[0]])+" ohms"
    if length==4:    
        value = (color_to_value[colors[0]] * 10 + color_to_value[colors[1]])* (10 ** color_to_value[colors[2]])
        tolerance = color_to_tolerance[colors[3]]
    if length==5:
        value = (color_to_value[colors[0]] * 100 + color_to_value[colors[1]] *10 + color_to_value[colors[2]]) * (10 ** color_to_value[colors[3]])
        tolerance = color_to_tolerance[colors[4]]
    while value >= 1000 and unit_index < len(units) - 1:
        value /= 1000
        unit_index += 1
    if isinstance(value, float) and value.is_integer():
        value = int(value)
        
    return f"{value} {units[unit_index]} ±{tolerance}"
        
        
    
