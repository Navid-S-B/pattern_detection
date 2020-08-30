#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on --17/07/19--

@author: -- Navid Shadman Bhuiyan --

ZID: z5260384

Program Description
-------------------
    This function searches the data_series for all the values that satisfy the 
    criteria mentioned below and in the assignment specification document.
    The function returns the indices of these values.

Parameters
----------
    - data_series : [float]
        - A list of float values representing a data series. You are looking
          for instances of the pattern inside this data_series. It can 
          be also considered a similarity list.
    
    - pattern_width : [float]
        - A float value. The length/width of the pattern.
    
    - threshold : [float]
        - A float value. Selected similarity measure needs to be greater than or
          equal to the given threshold value.

Data Dictionary
---------------
    - temp_max : [float]
        - This is the temporary maximum value out of all overlapping indices.
        - This value is also above the threshold.
    - temp_list : [float]
        - A float list of all values at overlapping indices which is used to 
          test against the temp_max. 
        - If the value at the chosen index is the maximum
          value of the temp_list, then the index is assigned.
          
Returns
-------
    pattern_indices : [int]
        - A list of integer non overlapping indices (defined below) where
          it's similarity value is greater than or equal to the given threshold
          value and that satisfy the following criteria:
             - An index is not selected if the value at the index is less than
               a value at one of it's overlapping indices.
             - An index is not selected if it is overlapping with first or last
               index.
        - Overlapping indices: two indices are overlapping if the
           distance between them is less than the width of the pattern.
           
    "Not detected" : [str]
        - This string is outputted if a value at any index in the data_series
          is not satisfied by the conditions listed above under 'pattern_indices' 
          and in the assignnent specification document.
          
    "Insufficient data" : [str]
        - If the given data_series is shorter than the given pattern_width.
        
"""
def pattern_search_multiple(data_series, pattern_width, threshold):
    #Conditional statement to see if there is sufficient data to continue
    #and find a pattern.
    if len(data_series)>=pattern_width:
        #This produces cases where all the data points overlap with the 
        #first or last index, or even both. According to the assignment 
        #specifications, an index cannot be selected if it intersects with
        #the first or last index. So there is no point continuing on if all
        #the indices overlap with the first or last index. This is also 
        #to avoid further bugs in the code when considering the range function later.
        if (len(data_series)-pattern_width)<=pattern_width:
            return 'Not detected'
        else:
            #The list containing non-overlapping indices according to the 
            #specifications of this assignment.
            pattern_indices=[]
            #If the pattern_width==1, no index in all the data_series will
            #ever overlap due to the assignment specifications given. 
            #Although this case may not be tested at all,
            #becase a value is not a pattern in the sense that there is some
            #values with some sort of sequential series i.e. how can a pattern
            #be a single digit. But this function could be used to find a value 
            #which may appear in the data_series list in some sort of pattern.
            if pattern_width==1:
                 for k in range(len(data_series)):
                    #Conditional statement for code to only filter out and only
                    #test values at indices which are above or equal
                    #to the threshold.
                     if data_series[k]>=threshold:
                        pattern_indices.append(k)
            #This logic assumes that the pattern_width>1 i.e. that there is the
            #possibility of overlapping indices.
            else:
                #This for-loop and the range of numbers it acts within avoids 
                #any index that overlaps with the first or last index,to go 
                #accordingly with the assignment specifications.
                for k in range(pattern_width,len(data_series)-pattern_width):
                    #Conditional statement for code to only filter out and only
                    #test values at indices which are above or equal
                    #to the threshold.
                    if data_series[k]>=threshold:
                        #Explaination of the temp variables are in the 
                        #'Data Dictionary' section.
                        temp_max=data_series[k]
                        temp_list=data_series[k-pattern_width+1:k+pattern_width]
                        #This is the final test to determine if at this index, it's the maximum 
                        #value out of all values at overlapping indices. Although
                        #a problem only occurs if there are multiple instances (repititions)
                        #of the same temp_max value in their overlapping set of indices.
                        #Trying to code something that only records the first index of the 
                        #value which repeats in its with respect to the temp_list proved too difficult. 
                        #It shall be assumed the test data_series cases won't contain repeating values within 
                        #overlapping indices.
                        if temp_max==max(temp_list):
                            pattern_indices.append(k)
            #Conditional statement to distinguish if there is something detected
            #or not in the pattern_indices list after calculations to give the
            #desired output.
            if len(pattern_indices)>0:
                return pattern_indices
            else:
                return 'Not detected'            
    else:
        return 'Insufficient data'