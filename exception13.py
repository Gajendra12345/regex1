#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      in
#
# Created:     03-05-2023
# Copyright:   (c) in 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
a = 10
b = 0
try:
    c = a/g
    print(c)
    print('Inside try')

except ZeroDivisionError as obj:
    print(obj)

except NameError as ob:
    print(ob)

print('Rest of the code')












