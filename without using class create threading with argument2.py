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

from threading import Thread
def disp(a,b):
    print("Thread Running", a, b)

t = Thread(target=disp, args=(10,20))

t.start()
