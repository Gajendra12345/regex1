#-------------------------------------------------------------------------------
#
# Author:      in
#
# Created:     24-05-2023
# Copyright:   (c) in 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import smtplib as s
ob =s.SMTP('smtp.gmail.com',587)
ob.ehlo()

ob.starttls()

ob.login('gmishra587@gmail.com','krqfhphjrzwrdmxj')

subject="test python"
body="i love python"

message="Subject:{}\n\n{}".format(subject,body)

listaddress=['gm0702@srmist.edu.in',"gajendramishra20@gmail.com"]
ob.sendmail('gmishra587@gmail.com',listaddress,message)
print("send mail")
ob.quit()
