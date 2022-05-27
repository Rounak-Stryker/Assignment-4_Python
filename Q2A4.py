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

Year=int(input("Enter Year = "))
if(Year%4==0):
    if(Year%100==0):
        if(Year%400==0):
            print("Year is a leap year.")
        else:
            print("Year is not a leap year")
    else:
        print("Year is a leap year")
else:
    print("Year is not a leap year")