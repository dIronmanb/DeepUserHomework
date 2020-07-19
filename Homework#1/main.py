####################################################################################
# File Name :                                                                      #  
# Date  : 2020/00/00                                                               #  
# OS : Windows 10                                                                  #  
# Author :                                                                         #
# -------------------------------------------------------------------------------  #  
# requirements : python 3.x                                                        #
#                                                                                  #
####################################################################################   

import random                      
import numpy as np 
import matplotlib.pyplot as plt                    
import pandas as pd                                 

if __name__ == '__main__':
    
    #Read Data
    sepal = pd.read_csv("C:\\Users\\PAN\\Desktop\\MachineLearningFromScratch\\Homework\\Homework#1\\data.csv")
    sepal_x = sepal["Sepal width"]
    sepal_y = sepal["Sepal length"]

    #Use matplotlib
    plt.plot(sepal_x, sepal_y, 'o')
    plt.xlabel("width")
    plt.ylabel("length")
    plt.title("Sepal info")    
    plt.show()
