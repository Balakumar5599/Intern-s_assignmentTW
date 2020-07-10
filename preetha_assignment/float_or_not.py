#given number is float or not

import re
def float_or_not(num):
    if(re.search('[+-]?[0-9]+\.[0-9]+',num)):
       return True
    else:
        return False
num=input("Enter the number: ")
print(float_or_not(num))
