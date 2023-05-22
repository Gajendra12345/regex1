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
    money = 1000

    def show(self):
        print("Parent Class Instance Method")

    @classmethod
    def showmoney(cls):
        print("Parent Class Class Method:", cls.money)

class Son(Father):
    def disp(self):
        print("Child Class Instance Method")

s = Son()
s.disp()
s.show()
s.showmoney()











