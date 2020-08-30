#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 16:37:53 2019

@author: Navid

"""
import unittest
import pattern_search_multiple as psm

# ------- TEST CASES ------------------
# Some example test data defined below.
# You need to create some more of your own.
# Copy the format, but change the values.
# To change which test case is used, skip below to the main module.
#Test 1 and 2 are the school testing modules given to see if your function
#can do the basics.

class Test_Data(unittest.TestCase):

	def test1(self):
		threshold = 15
		pattern_width = 4
		data_series = [-1, 5, 4, 8, 3, 21, 18, 16, 3, 2, 3, 1, 4, 5, 17, 22, 36, 33, 34, 9, 1, -2]
		data_series = data_series + [-2, 4, -1, 7, 13, 12, 3, 1, 4, 5, 26, 22, 28, 27, 26, 2, 8, 6]
		expected_answer = [5, 16, 34]
		result = psm.pattern_search_multiple(data_series,pattern_width,threshold)
		self.assertEqual(result,expected_answer)

	def test2(self):
		threshold = 10
		pattern_width = 3
		data_series = [-1, 5, 4, 8, 3, 21, 18, 16, 3, 2, 3, 1, 4, 5, 17, 22, 36, 33, 34, 9, 1, -2]
		data_series = data_series + [-2, 4, -1, 7, 13, 12, 3, 1, 4, 5, 26, 22, 28, 27, 26, 2, 8, 6]
		expected_answer = [5, 16, 26, 34]
		result = psm.pattern_search_multiple(data_series,pattern_width,threshold)
		self.assertEqual(result,expected_answer)

	#Non-overlapping indices with the first and last index.
	def test3(self):
		threshold = 10
		pattern_width = 3
		data_series = [90, 90, 90, 6, 3, 18, 21, 16, 3, 2, 3, 1, 4, 5, 27, 22, 7, 33, 34, 9, 1, -2]
		data_series = data_series + [-2, 4, -1, 7, 9, 12, 3, 1, 4, 5, 26, 22, 3, 2, 6, 90, 90, 90]
		expected_answer = [6, 14, 18, 27, 32]
		result = psm.pattern_search_multiple(data_series,pattern_width,threshold)
		self.assertEqual(result,expected_answer)

	#To double check if your function doesn't spurt out overlapping indices.
	def test4(self):
		threshold = 10
		pattern_width = 3
		data_series = [0, 10, 20, 30, 40, 50, 40, 30, 20, 10, 0]
		expected_answer = [5]
		result = psm.pattern_search_multiple(data_series,pattern_width,threshold)
		self.assertEqual(result,expected_answer)

	#Not detected, although there is an obvious pattern here, with the pattern
	#width being three and for your function to go through this data_series, it will
	#cannot output overlapping indices as indicated by the assignment. This also
	#tests if your function checks for values within the pattern_width to see whether or not
	#if there are values within it that are larger than the value at the selected index.    
	def test5(self):
		threshold = 10
		pattern_width = 3
		data_series = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
		expected_answer = 'Not detected'
		result = psm.pattern_search_multiple(data_series,pattern_width,threshold)
		self.assertEqual(result,expected_answer)

	#Similar module as last test.
	def test6(self):
		threshold = 1
		pattern_width = 3
		data_series = [1, 2, 3, 4, 5, 6]
		expected_answer = 'Not detected'
		result = psm.pattern_search_multiple(data_series,pattern_width,threshold)
		self.assertEqual(result,expected_answer)


	#Weird one, although very unlikely to test considering a pattern which has a length of 1 is kind of
	#stupid. This case makes no value in the data_series not overlap whatsoever; i.e. no value will ever overlap
	#with the last or first index. This to me seems an unlikely case to be tested by the school, if you want to
	#implement a safe-measure for this case then go ahead, although it does not make any sense to consider it.
	def test7(self):
		threshold = 3
		pattern_width = 1
		data_series = [1, 2, 5, 5, 5, 6]
		expected_answer = [2, 3, 4, 5]
		result = psm.pattern_search_multiple(data_series,pattern_width,threshold)
		self.assertEqual(result,expected_answer)

	#Insufficent data case.
	def test8(self):
		threshold = 3
		pattern_width = 10
		data_series = [1, 2, 3, 4]
		expected_answer = 'Insufficient data'
		result = psm.pattern_search_multiple(data_series,pattern_width,threshold)
		self.assertEqual(result,expected_answer)

	#Not detected complex case: if the len(data_series)-pattern_width<=pattern_width,
	#takes time to think about (think about this example) but essentially every value in
	#the data_series overlaps with the first or last index, so no index cannot be selected by default.
	def test9(self):
		threshold = 10
		pattern_width = 20
		data_series = [-1, 5, 4, 8, 3, 21, 18, 16, 3, 2, 3, 1, 4, 5, 17, 22, 36, 33, 34, 9, 1, -2]
		data_series = data_series + [-2, 4, -1, 7, 13, 12, 3, 1, 4, 5, 26, 22, 28, 27, 26, 2, 8, 6]
		expected_answer = 'Not detected'
		result = psm.pattern_search_multiple(data_series,pattern_width,threshold)
		self.assertEqual(result,expected_answer)

	#This is to test whether or not your function can find indices in this list which do not overlap with the 
	#first or last index.
	def test10(self):
		threshold = 10
		pattern_width = 20
		data_series = [-1, 5, 4, 8, 3, 21, 18, 16, 3, 2, 3, 1, 4, 5, 17, 22, 36, 33, 34, 9, 100, -2]
		data_series = data_series + [-2, 4, -1, 7, 13, 12, 3, 1, 4, 5, 26, 22, 28, 27, 26, 2, 8, 6,67]
		expected_answer = [20]
		result = psm.pattern_search_multiple(data_series,pattern_width,threshold)
		self.assertEqual(result,expected_answer)
	    
if __name__=="__main__":
	unittest.main()