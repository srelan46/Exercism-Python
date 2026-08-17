"convert display value to egg using Binary"
def egg_count(display_value):
    "convert display value to egg using Binary"
    bin = []
    result = 0
    if display_value==0:
        return 0
    while(display_value>0):
        bin.append(display_value%2)
        display_value = display_value//2
    for value in bin:
        if value==1:
            result+=1
    return result
        
        
