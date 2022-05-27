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

import random

for i in range(1,11):
  a = random.randint(1,10)
  b = random.randint(1,10)
  ans = int(input(f'Question{i}:{a}x{b}='))
  if ans==a*b:
    print("Correct")
  else:
    print(" Incorrect, try again ")