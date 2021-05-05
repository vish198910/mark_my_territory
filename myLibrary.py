# -*- coding: utf-8 -*-
"""
Created on Wed May  5 07:53:43 2021

@author: vish1
"""

import numpy
import cv2
import matplotlib.pyplot as plt
import re
import math


class MarkMyTerritory:
    def __init__(self,input_image):
        self.input_image = cv2.imread(input_image)
        
    #printing the Numpy array format of the  image
    def get_input_image(self,image):
        plt.imshow(image)
        plt.show()
        
    
    #resizing
    def resize_img(self,size,input_image_array):
        resized_image = cv2.resize(input_image_array,(size,size))
        return resized_image
    
    #drawing the circle
    def draw(self,input_image_array,color_of_tile,center_of_tile):
            cv2.circle(input_image_array,center_of_tile,
                       self.find_radius(per_square_shape=self.per_square_shape(input_image_array)),
                       (255 - int(color_of_tile[0]),255- int(color_of_tile[1]),255 - int(color_of_tile[2])),
                       -1,2)
            
    #displaying the circle on the chess board
    def display(self,input_image_array,coordinate_name,size,chess_dict):
       x_and_y = re.split('(\d+)', coordinate_name)
       x = x_and_y [0] #getting horzontal index part, which is a character
       y = int(x_and_y[1]) #geting the vertical index part, which is a number
       
       
       #First we will resize the board
       resized_image = self.resize_img(size,input_image_array)
      
       # 
       square_shape = self.per_square_shape(resized_image)
       
      
       #define radius of circle on the basis of the size of the square
       radius_of_circle = self.find_radius(self.per_square_shape(resized_image))
       
       
       #getting horizonatl and vertical position of the territory
       
       horizontal_position = (chess_dict[x] * square_shape[0] )- radius_of_circle
       vertical_position =  y * square_shape[1] - radius_of_circle
       
       #getting the color of  the image
       color_of_tile = resized_image[int(horizontal_position)][int(size - vertical_position)]
       
       #center coordinate of the territory to draw circle
       center_of_tile = (int(horizontal_position),int(size - vertical_position))
       
       print(color_of_tile)
       print(center_of_tile)
       #draw the circle on the resized image
       self.draw(resized_image,color_of_tile,center_of_tile)
       plt.imshow(resized_image)
       plt.show()
       
   
    #find shape of each square of the original or the resized image
    def per_square_shape(self,input_image):
        rows, cols , channel = input_image.shape
        return (rows / 8,cols / 8)
    
    #find the radius of the circe on the basis of the size of individual square on the chessboard
    def find_radius(self,per_square_shape):
        return int(per_square_shape[0] / 2) # can use any of the index given by the per_square_shape
    