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

import threading

class call(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

obj= call(name= 'sending msg helloo')
obj1= call(name = 'rec.msg byee')
obj.start()
obj1.start()
