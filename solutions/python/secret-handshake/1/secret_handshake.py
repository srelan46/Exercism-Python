"Convert Binary String to Secret Coding Club"
actions = {
    0:"wink",
    1:"double blink",
    2:"close your eyes",
    3:"jump",
    4:"Reverse the order of the operations in the secret handshake."
}
def commands(binary_str: str) -> list[str]:
    "Secret Coding Club"
    result = []
    rev_str = "".join(reversed(binary_str))
    for index in range(len(rev_str)):
        if index < 4 and rev_str[index] == "1":
            result.append(actions[index])
    if len(rev_str) >= 5 and rev_str[4] == "1":
        result.reverse()
    
    return result