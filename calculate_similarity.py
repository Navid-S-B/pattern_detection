"""
Created on -- 08/07/2019 --

@author: -- Navid Shadman Bhuiyan --

Program Description
-------------------
    The function is expected to return a float value
    which indicates the similarity between the data_segment
    and pattern list. 
    
Parameters
----------
    data_segment: [float]
        - A list of float values to compare against the pattern.
    pattern: [float]
        - A list of float values representing the pattern. 
    
Return Outputs
--------------
    similarity:
        - A float value i.e. the similarity score/value which
          is returned by the function.
    "Error":
        - If the data segment and pattern are not of the same length
          the program will return the string: "Error".
        - If a data_segment smaller than the pattern, there can be no 
          indication of a pattern at all according to the similarity 
          calculation used in this function.
"""
def calculate_similarity(data_segment, pattern):
    #Conditional statement to start for-loop, if true, then
    #for-loop is activated and returns the similarity value.
    if len(data_segment)==len(pattern):
        #Constant to sum/calculate similarity
        similarity=0
        #For-loop to do similarity calculation i.e. sum the multiples.
        for k in range(len(data_segment)):
            similarity+=data_segment[k]*pattern[k]
        return similarity
    #If len(data_segment)!=len(pattern) i.e. if the conditional statment
    #is false, return an error message.
    else:
        return 'Error'
