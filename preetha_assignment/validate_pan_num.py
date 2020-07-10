import re
def validate_pan_num(num):
    if re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]$',num):
        return True
    else:
        return False
num=input("Enter the PAN number: ")
print(validate_pan_num(num))
