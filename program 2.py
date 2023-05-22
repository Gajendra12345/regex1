#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      in
#
# Created:     03-05-2023
# Copyright:   (c) in 2023
# Licence:     <your licence>
#------------------------------------------------------------------------------
no=int(input("Input a number"))
dic = dict()

for x in range(1,no+1):
     dic[x]=x*x
print(dic)