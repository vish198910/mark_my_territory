# -*- coding: utf-8 -*-
"""
Created on Wed May  5 07:52:48 2021

@author: vish1
"""


import myLibrary as my_lib
import numpy
import matplotlib.pyplot as plt 
#creating the dictionary for the chessboard
chess_dict = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}

#creating the MarkMyTerritory object
mark_my_territory = my_lib.MarkMyTerritory("input_image.png")

#testing the working of getting the image
mark_my_territory.get_input_image(mark_my_territory.input_image)


#size = input("Enter the size of the image : ")
#coordinate = input("Enter the coordinate name of the image : ")


#checking the display function 
mark_my_territory.display(mark_my_territory.input_image,"f6",800,chess_dict)

