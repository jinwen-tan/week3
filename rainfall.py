#get input
inches_str = input("How many inches of ran have falllen: ")

#convert to integer/float
inches_float = float(inches_str)
inches_int = int(inches_float)


#volume of int and float calculate separately
volume_int = (inches_int/12)*43560
volume_float = (inches_float/12)*43560

#gallons of int and float calculate separately 
gallons_int = volume_int * 7.48051945
gallons_float = volume_float * 7.48051945

print(inches_int, " in. rain on 1 acre is", gallons_int, "gallons")
print(inches_float, " in. rain on 1 acre is", gallons_float, "gallons")