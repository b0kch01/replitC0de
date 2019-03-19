def bishop_move(x1, y1, x2, y2):
    if ((x1 - x2 == y1 - y2) and (x1 != x2 or y1 != y2)): 
        return True
    return False
