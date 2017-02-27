def using_control_once():
    if True:
        return "Success #1"

def using_control_again():
    if True or False or 2+2!=4:
        return "Success #2"

print using_control_once()
print using_control_again()
