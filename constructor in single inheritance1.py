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
class Father:
    def __init__(self):
       self.money = 2000
       print("Father Class Constructor")

    def show(self):
        print("Father Class Instance Method")

class Son(Father):
    def disp(self):
        print("Son Class Instance Method")

s = Son()
print(s.money)
s.disp()
s.show()












