"calculates rebase"
def rebase(input_base, digits, output_base):
    "calculate rebase based on the input_base,digits and output_base"
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if any(digit < 0 or digit >= input_base for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    number = 0 
    for digit in digits:
        number=number*input_base+digit
    if number == 0:
        return [0]
    result = []
    while number>0:
        result.append(number%output_base)
        number//=output_base
    return result[::-1]
