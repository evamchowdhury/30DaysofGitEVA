line1 = input("Y = mx + b :")
line1 = line1.replace(" ", "")
import re

def slope(line):
    search = re.search(r'y=(\-?\d*)x', line)
    if not search:
        return None
    m = search.group(1)
    if m == "":
        return 1
    elif m == "-":
        return -1
    else:
        return int(m)

print(slope(line1))