#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Rounak Chatterjee
#
# Created:     27-05-2022
# Copyright:   (c) Rounak Chatterjee 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

Marks=int(input("Enter Marks: "))
if(Marks<100 and Marks>=0):
    if(Marks<25):
        print("Grade = F")
    elif(Marks>=25 and Marks<45):
        print("Grade = E")
    elif(Marks>=45 and Marks<50):
        print("Grade = D")
    elif(Marks>=50 and Marks<60):
        print("Grade = C")
    elif(Marks>=60 and Marks<80):
        print("Grade = B")
    elif(Marks>=80):
        print("Grade = A")
else:
    print("Invalid Input of Marks")
