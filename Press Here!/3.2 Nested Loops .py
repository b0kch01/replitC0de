def array_of_x(x, y):
    string = ""
    for rows in range(x):
        for i in range(y):
            if i == y - 1:
                string += "x\n"
            else:
                string += "x "
    return string

def alternate_x_o(rows, columns):
    string = ""
    x = rows
    y = columns
    for rows in range(x):
        char = "x" if rows%2==0 else "o"
        for i in range(y):
            if i == y - 1:
                string += "{}\n".format(char)
            else:
                string += "{} ".format(char)
    return string
    
def increasing_triangle(n):
    string = ""
    max_num = n
    for i in range(1, max_num + 1):
        for num in range(1, i + 1):
            string += str(num)
        string += "\n"
    return string
