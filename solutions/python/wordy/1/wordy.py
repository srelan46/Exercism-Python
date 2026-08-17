"Parse and evaluate simple math word problems returning the answer as an integer."
VALID_OPERATIONS = ("plus","minus","multiplied","divided")
def manual_calculate(operation,num1,num2):
    "calculates operation"
    if operation=="plus":
        return num1+num2
    elif operation=="minus":
        return num1-num2
    elif operation=="multiplied":
        return num1*num2
    elif operation=="divided":
        return num1/num2

def answer(question):
    "answers question"
    tokens = question.removesuffix("?").lower().split()
    result = None
    operation = None
    for token in tokens:
        if token in {"what", "is", "by"}:
            continue
        if token in VALID_OPERATIONS:
            if result is None or operation is not None:
                raise ValueError("syntax error")
            operation = token
            continue
        try:
            number = int(token)
        except ValueError:
            raise ValueError("unknown operation")
        if result is None:
            result = number
        elif operation is None:
            raise ValueError("syntax error")
        else:
            result = manual_calculate(operation,result,number)
            operation = None
    if result is None or operation is not None:
        raise ValueError("syntax error")

    return result
