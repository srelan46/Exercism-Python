"Calculates OCR based on Input Grid"
digits ={
    (" _ ",
     "| |", 
     "|_|", 
     "   "):"0",
    ("   ", 
     "  |", 
     "  |", 
     "   "):"1",
    (" _ ",
     " _|",
     "|_ ",
     "   "):"2",
    (" _ ",
     " _|",
     " _|",
     "   "):"3",
    ("   ",
     "|_|",
     "  |",
     "   "):"4",
    (" _ ",
     "|_ ",
     " _|",
     "   "):"5",
    (" _ ",
     "|_ ",
     "|_|",
     "   "):"6",
    (" _ ",
     "  |",
     "  |",
     "   "):"7",
    (" _ ",
     "|_|",
     "|_|",
     "   "):"8",
    (" _ ",
     "|_|",
     " _|",
     "   "):"9"
}
def convert(input_grid):
    "Calculate OCR using Input Grid"
    if len(input_grid)%4!=0:
        raise ValueError("Number of input lines is not a multiple of four")
    if len(input_grid[0])%3!=0:
        raise ValueError("Number of input columns is not a multiple of three")
    row_result = []
    for rows in range(0, len(input_grid), 4):
        digit_result = ""
        block = input_grid[rows:rows + 4]
        for col in range(0, len(block[0]), 3):
            digit_pattern = (
                block[0][col:col + 3],
                block[1][col:col + 3],
                block[2][col:col + 3],
                block[3][col:col + 3],
            )
            digit_result += digits.get(digit_pattern, "?")
        row_result.append(digit_result)
    return ",".join(row_result)
        
