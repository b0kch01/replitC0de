max_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def next_day(month, day):
    if(month == 12 and day == 31):
        return "1/1"
    if(day == max_days[month]):
       return("{}/1".format(month + 1))
    return("{}/{}".format((month), (day + 1)))
