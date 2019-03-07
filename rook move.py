def rook_move(x1, y1, x2, y2):
    if x1 == x2 and x2 == y1 and y1 == y2:
        return False
    if x1 == x2 or y2 == y1:
        return True
    return False
