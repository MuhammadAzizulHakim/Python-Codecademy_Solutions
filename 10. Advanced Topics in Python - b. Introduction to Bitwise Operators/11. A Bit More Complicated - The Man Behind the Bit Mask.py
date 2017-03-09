def check_bit4(x):
    mask = 0b1000
    if mask & x > 0:
        return "on"
    else:
        return "off"

check_bit4(0b1111)
