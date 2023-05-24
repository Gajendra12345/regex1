#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      in
#
# Created:     24-05-2023
# Copyright:   (c) in 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from threading import *

class Hello(Thread):
    def run(self):
        for i in range(10):
            print("hello")

class hi(Thread):
    def run(self):
        for i in range(10):
            print("hi")

t1 =Hello()
t2=hi()
t1.start()
t2.start()
