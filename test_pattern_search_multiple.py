#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 16:37:53 2019

@author: ashesh

"""

import pattern_search_multiple as psm
import matplotlib.pyplot as plt


# ------- TEST CASES ------------------
# Some example test data defined below.
# You need to create some more of your own.
# Copy the format, but change the values.
# To change which test case is used, skip below to the main module.
#Test 1 and 2 are the school testing modules given to see if your function
#can do the basics.

def test1():
    threshold = 15
    pattern_width = 4
    data_series = [-1, 5, 4, 8, 3, 21, 18, 16, 3, 2, 3, 1, 4, 5, 17, 22, 36, 33, 34, 9, 1, -2]
    data_series = data_series + [-2, 4, -1, 7, 13, 12, 3, 1, 4, 5, 26, 22, 28, 27, 26, 2, 8, 6]

    expected_answer = [5, 16, 34]

    return threshold, pattern_width, data_series, expected_answer


def test2():
    threshold = 10
    pattern_width = 3
    data_series = [-1, 5, 4, 8, 3, 21, 18, 16, 3, 2, 3, 1, 4, 5, 17, 22, 36, 33, 34, 9, 1, -2]
    data_series = data_series + [-2, 4, -1, 7, 13, 12, 3, 1, 4, 5, 26, 22, 28, 27, 26, 2, 8, 6]

    expected_answer = [5, 16, 26, 34]

    return threshold, pattern_width, data_series, expected_answer

#Non-overlapping indices with the first and last index.
def test3():
    threshold = 10
    pattern_width = 3
    data_series = [90, 90, 90, 6, 3, 18, 21, 16, 3, 2, 3, 1, 4, 5, 27, 22, 7, 33, 34, 9, 1, -2]
    data_series = data_series + [-2, 4, -1, 7, 9, 12, 3, 1, 4, 5, 26, 22, 3, 2, 6, 90, 90, 90]

    expected_answer = [6, 14, 18, 27, 32]

    return threshold, pattern_width, data_series, expected_answer

#To double check if your function doesn't spurt out overlapping indices.
def test4():
    threshold = 10
    pattern_width = 3
    data_series = [0, 10, 20, 30, 40, 50, 40, 30, 20, 10, 0]

    expected_answer = [5]

    return threshold, pattern_width, data_series, expected_answer

#Not detected, although there is an obvious pattern here, with the pattern
#width being three and for your function to go through this data_series, it will
#cannot output overlapping indices as indicated by the assignment. This also
#tests if your function checks for values within the pattern_width to see whether or not
#if there are values within it that are larger than the value at the selected index.    
def test5():
    threshold = 10
    pattern_width = 3
    data_series = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    expected_answer = 'Not detected'

    return threshold, pattern_width, data_series, expected_answer

#Similar module as last test.
def test6():
    threshold = 1
    pattern_width = 3
    data_series = [1, 2, 3, 4, 5, 6]

    expected_answer = 'Not detected'

    return threshold, pattern_width, data_series, expected_answer

#Weird one, although very unlikely to test considering a pattern which has a length of 1 is kind of
#stupid. This case makes no value in the data_series not overlap whatsoever; i.e. no value will ever overlap
#with the last or first index. This to me seems an unlikely case to be tested by the school, if you want to
#implement a safe-measure for this case then go ahead, although it does not make any sense to consider it.
def test7():
    threshold = 3
    pattern_width = 1
    data_series = [1, 2, 5, 5, 5, 6]

    expected_answer = [2, 3, 4, 5]

    return threshold, pattern_width, data_series, expected_answer

#Insufficent data case.
def test8():
    threshold = 3
    pattern_width = 10
    data_series = [1, 2, 3, 4]

    expected_answer = 'Insufficient data'

    return threshold, pattern_width, data_series, expected_answer

#Not detected complex case: if the len(data_series)-pattern_width<=pattern_width,
#takes time to think about (think about this example) but essentially every value in
#the data_series overlaps with the first or last index, so no index cannot be selected by default.
def test9():
    threshold = 10
    pattern_width = 20
    data_series = [-1, 5, 4, 8, 3, 21, 18, 16, 3, 2, 3, 1, 4, 5, 17, 22, 36, 33, 34, 9, 1, -2]
    data_series = data_series + [-2, 4, -1, 7, 13, 12, 3, 1, 4, 5, 26, 22, 28, 27, 26, 2, 8, 6]

    expected_answer = 'Not detected'

    return threshold, pattern_width, data_series, expected_answer

#This is to test whether or not your function can find indices in this list which do not overlap with the 
#first or last index.
def test10():
    threshold = 10
    pattern_width = 20
    data_series = [-1, 5, 4, 8, 3, 21, 18, 16, 3, 2, 3, 1, 4, 5, 17, 22, 36, 33, 34, 9, 100, -2]
    data_series = data_series + [-2, 4, -1, 7, 13, 12, 3, 1, 4, 5, 26, 22, 28, 27, 26, 2, 8, 6,67]

    expected_answer = [20]

    return threshold, pattern_width, data_series, expected_answer
# --- CHECK OUTPUT ------------------
# This function compares the value of two lists.
# Check your output against expected output, and report the result

def check_output(selected_indices, expected_answer):
    # Let's print your output
    print('This is the output your function gave --> ', selected_indices)
    # Let's print expected output
    print('This is the expected output --> ', expected_answer)

    if type(selected_indices) is str:
        if selected_indices==expected_answer:
            print('GOOD JOB your output matches the expected outputs. YAY!!!!! =)')
            return
        else:
            print('Oh noooo, your output does NOT match expected output. Please try again.')
            return
    else:
        is_correct = True
        for i in range(0, len(expected_answer)):
            if abs(selected_indices[i] - expected_answer[i]) > 0.00001:
                    is_correct = False
    
        if is_correct is True:
                print('GOOD JOB your output matches the expected outputs. YAY!!!!! =)')
        else:
                print('Oh noooo, your output does NOT match expected output. Please try again.')


# --- plot_results ------------------
# This is just a helper function that graphs the results.
# Let's plot the data_series, the threshold line
# and the seleted indices (green circles)
def plot_results(data_series, selected_indices, threshold):

    # Let's check whether the first two parameters are lists or not?
    if not(type(selected_indices) is list):
        print('')
        print("No need to plot data, since your function doesn't return a list of inputs for python to plot. If you got the right answer, WELL DONE, if you didn't, reconsider your function and what it outputs for a certain case.")
        return
    selected_values = [ data_series[i] for i in selected_indices]
    threshold_list = [threshold] * len(data_series)
    x_list = [ i for i in range(0,len(data_series))]

    width = 1/2.5
    plt.grid(True)
    plt.rc('grid', linestyle="-", color='lightgray')
    plt.rc('axes', axisbelow=True)
    plt.bar(x_list, data_series, width)
    plt.plot(x_list, threshold_list, 'r' )
    plt.plot(selected_indices, selected_values,'go',label='Peaks')
    plt.xlabel('index')
    plt.ylabel('data values')
    plt.title('Fig: pattern_search_multiple \n(threshold = ' + str(threshold) + ', pattern_width = ' + str(pattern_width) + ')') # title of the graph
    plt.minorticks_on()
    plt.grid(b=True, which='major',linestyle='-')
    plt.show()
# --------------------------------

# ---- MAIN MODULE --------------------
# This is the main code that performs the test
print('TESTING FUNCTION: pattern_search_multiple')

# Select Your Test, you can select one at a time
# TODO change the test<number> to run a different test at a time
threshold, pattern_width, data_series, expected_answer = test5()

# Let's call your function!
selected_indices = psm.pattern_search_multiple(data_series, pattern_width, threshold)

# Let's check your output against expected output, and report the result
check_output(selected_indices, expected_answer)

# ------------------------------------------------
# Let's plot the data_series, the threshold line
# and the seleted indices (green circles)
plot_results(data_series, selected_indices, threshold)
# -------- end ---------------
