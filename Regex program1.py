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
import re
crick_score='''Gajendra scores 65 and \n Santosh scores 40 and Rohit scores 56 Sankar scores 45'''

print(crick_score)

name=re.findall(r'[A-Z][a-z]*',crick_score)
print(name)


