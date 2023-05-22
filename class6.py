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
def decor(fun):
    def inner():
        a = fun()
        add = a+5
        return add
    return inner

def num():
    return 10

result_fun = decor(num)
print(result_fun())











