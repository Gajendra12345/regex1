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
    c = a/b
    print(c)
    print('Inside try')

except ZeroDivisionError:
    print('Division by Zero Not Allowed')
print('rest of the code')












