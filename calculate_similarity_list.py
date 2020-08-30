#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on -- 08/07/2019 --

@author: -- Navid Shadman Bhuiyan --

ZID: z5260384

Program Description
-------------------
    The function 'calculate_similarity_list' is expected to compute
    similarity values for data segments from the data_series list
    when compared to a pattern list, and then compile all of these 
    values into a seperate list, which the function returns. 
    Slicing a data list to match the size of the pattern will be done within 
    this function, whilst calculating similarity values of data segments 
    will be executed by importing the 'calculating_similarity' function.

Parameters
----------
    data_series : [float]
        - A list of float values representing a data series. 
    pattern : [float]
        - A list of float values representing the pattern.

Data Dictionary
---------------
    data_segment : [float]
        - A sliced list of float values from the data_series, which
          is of the same size as the pattern list.
    sliced_similarity : [float]
        - A list of float similarity values correlating to a 
          data_segment.
    
Return Outputs
--------------
    similarity_list:
        - A compiled float list of calculated similarity values.
"""
#Import calculate_similarity to implement it later.
import calculate_similarity as cs

def calculate_similarity_list(data_series, pattern):
    #list for appending similarity values of data segments.
    similarity_list=[]
    #For loop to undergo repitative calculations.
    for k in range(len(data_series)):
        #Breaking the for-loop here so bugs/errors arent produced
        #i.e. splicing data with a outer bound larger
        #then the length of the data_series list would
        #create an error.
        if k+len(pattern)>len(data_series):
            break
        #Slicing data to calculate the similarity values among segments
        #using the calculate_similarity function.
        data_segment=data_series[k:k+len(pattern)]
        sliced_similarity=cs.calculate_similarity(data_segment,pattern)
        similarity_list.append(sliced_similarity)
    return similarity_list