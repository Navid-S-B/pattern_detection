#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on --12/07/2019--

@author: -- Navid Shadman Bhuiyan --

ZID: z5260384

Program Description
-------------------
    The function 'pattern_search_max' returns the index of the maximum
    similarity measure (above a minimum threshold) from a 'similarity list' 
    i.e. a list of float similarity values, calculated from
    the comparison of a data segment to a pattern.This function does so by 
    importing the 'calculate_similarity_list' function which returns these 
    similarity values into a list, which the function 'pattern_search_max' then 
    deciphers to find the index which contains the most similar data segment to 
    the given patttern.

Parameters
----------
    data_series : [float]
        - A list of float values representing a data series.
    
    pattern : [float]
        - A list of float values representing the pattern.
    
    threshold : [float]
       - A float value. Selected similarity measure needs to be greater than or
         equal to the given threshold value.

Data Dictionary
---------------
    temp_sim_list: [float]
        - A temporary similarity list containing similarity float values for
          the given data series.
        - Returned from the 'calculated_similarity_list' function.
    
    max_sim_value : [float]
        - The maximum similarity float value of the temp_sl list.
        - Used to test against the threshold.
        - Used this value to test against the threshold as the task 
          only asked to 'find the index of the highest similarity
          value'.
Returns
-------
    "Insufficient data" : [str]
        - If the given data_series is shorter than the given pattern.
    
    "Not detected" : [str]
        - If all the similarity measures are (strictly) less than the given
          threshold value.
    
    max_sl_index : [float]
        - Index of the maximum similarity measure that is also greater than
          or equal to the given threshold value.

"""
#Import calculate_similarity_list to implement later.
import calculate_similarity_list as csl

def pattern_search_max(data_series, pattern, threshold):
    #Conditional statement as it is defined that the len(data_series)>
    #len(pattern), for the sufficient data case.
    if len(data_series)>=len(pattern):
        #Temporary similarity list calculated using the 
        #calculate_similarity_list function.
        temp_sim_list=csl.calculate_similarity_list(data_series,pattern)
        #Maximum value of temp_sl list, i.e. sorts list to find the max
        #similarity value.
        max_sim_value=max(temp_sim_list)
        #Conditional statement to decide what output is given: if the 
        #max similatiry value can be considered, i.e. is it above
        #the threshold?
        #If it is, return the index of which locates the pattern.
        if max_sim_value>=threshold:
            #Index of the maximum similarity value is exactly the 
            #same as the index where the pattern occurs in the data_series list.
            max_sim_index=temp_sim_list.index(max_sim_value)
            return max_sim_index
        #If not, nothing is detected.
        else:
            return 'Not detected'
    #Returns 'Insufficient data' when the conditional statement is proven
    #false.
    else:
        return 'Insufficient data'