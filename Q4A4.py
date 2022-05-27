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

for no_of_candy in range(200):
    if(no_of_candy%5==2 and no_of_candy%6==3 and no_of_candy%7==2):
        print("Possible No of Candies: ",no_of_candy,"\n")