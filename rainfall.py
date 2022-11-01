from imaplib import Int2AP


inches_str = input("How many inches of ran have falllen: ")
inches_float = float(inches_str)
volume = (inches_float/12)*43560
gallons = volume * 7.48051945
gallons_int= int(gallons)
inches_int = int(inches_float)
inches_float = float(inches_str)
print(inches_float, " in. rain on 1 acre is", gallons, "gallons")
print(inches_int, " in. rain on 1 acre is", gallons_int, "gallons")