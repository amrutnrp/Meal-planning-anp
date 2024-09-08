# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 21:24:59 2024

@author: amrut
"""

import yaml, os

cwd = os. path. dirname(__file__)
food_folder =  cwd + '/food'
err_flag = not os.path.exists( food_folder )

if err_flag:
    raise SystemExit()

meal_files = os.listdir( food_folder )

meal_info = []

for file in meal_files:
    with open(food_folder+ '/'+ file, 'r') as file:
        meal_info_each = yaml.safe_load(file)
        meal_info .append ( meal_info_each )


if __name__ == "__main__":
    h= meal_info_each['steps']
    
    print ('\n'.join ( h))
    h = input ('continue')
