def draw_line(length,label=" "):
    if label:
        print('-'*length + label)
    else:
        print("-"*length)

def draw_interval(length):
    if length>1:
        draw_interval(length-1)
        draw_line(length)
        draw_interval(length-1)

def draw_ruler(inch,length):
    draw_line(length,"0")
    for i in range(1, 1+inch):
        draw_interval(length-1)
        draw_line(length,str(i))

draw_ruler(2,4)



