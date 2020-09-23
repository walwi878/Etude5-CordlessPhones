import sys
import re
#from math import sqrt 
#from itertools import combinations
#import itertools
import smallestEnclosingCircle as sec

#Code written by:
#Brodie Bosecke, 5471718
#Meggie Morrison, 7777435
#Julian Fawcett, 3861924
#William Wallace, 1216661

telephones = []
tidyTelephones = []
diameters = []
third_diameters = []
depth = 1
third_depth = 2
noDupes = []
third_noDupes = []
smaller = []

# This function takes the file as input from stdin and stores it into a list called
# temp
def file():
	temp = sys.stdin.readlines()
	for element in temp:
		if(element != "Telephone sites\n"):
			telephones.append(element.strip("\n").lstrip().rstrip())

#Formats input into a list of lists stored in tidyTelephones
def formatList(telephones):
	for i in telephones:
		temp = i.split()
		temp[0] = float(temp[0])
		temp[1] = float(temp[1])
		tidyTelephones.append(temp)

#WHAT DOES THIS DO - from Brodax
def check_list(tidyTelephones):
	tidyTelephones = list(dict.fromkeys(tidyTelephones))

#sendEleven takes the list of tidyTelephones and finds the largest enclosing circle
# also prints the maximum radius

"""
def sendEleven(tidyTelephones):
	currentLargest = 0
	
	# The following two lines remove duplicates from the list
	# Inspired from: https://stackoverflow.com/questions/2213923/removing-duplicates-from-a-list-of-lists
	tidyTelephones.sort()
	no_dupes = list(tidyTelephones for tidyTelephones,_ in itertools.groupby(tidyTelephones))
 
	manyCombos = combinations(no_dupes, 12)

	for i in manyCombos:
		current = minimum_enclosing_circle(i)
		if current[1] == 1000000000000000000:
			# If less than 12 telephone sites given, circle size 
			# can be infinite, so exit program
			if len(tidyTelephones) < 12:
				print("Maximum radius: INFINITE")
				sys.exit(0)
			continue
		currentRad = current[1]
		if(currentRad > currentLargest):
			currentLargest = currentRad
			#print(currentLargest)
	if(currentLargest == 0):
		print("Maximum radius: INFINITE")
	else:
		print("Maximum radius:", currentLargest)
"""

def take_third(elem):
	return elem[0][2]

def third_take_third(elem):
	return elem[2]

def find_best_circle(zippy_list, i):
	global tidyTelephones
	global smaller
	count = 0
	if (i < len(zippy_list)):
		for point in tidyTelephones:
			if sec.is_in_circle(zippy_list[i][0], point):
				count += 1
	if count == 12:
		return i
	elif(len(zippy_list) == i):
		#exits the function, without doing anything
		a = 1 + 2
	#This doesn't work. Could include " and i = 994" which is the final value before
	#recursion depth error
	#elif(count == 0 and len(tidyTelephones) == 13 and i == 993):
	#	print("hardcoded")
	#	sys.exit(0)
	elif count < 11:
		smaller.append(i)
		return find_best_circle(zippy_list, i + 1)
	else:
		return find_best_circle(zippy_list, i + 1)


#def third_count_points(points, i):
#	if(i < len(points)):
#		for point in 

#Draw a circle from the input data, using 3 points. This function only gets accessed when the find_best_circle function
# finds no circle that contains 12 points. 
# Fuck me Murray this was a hard etude. And my back is sore - from Meggie and Brodie 
def find_best_circle_three_points(tidyTelephones):
	global third_diameters
	global third_noDupes
	smallest_circle = 0
	third_depth = 2
	first_third_depth = 1
	flag = 0
	print("HELLO")
	for i in range(len(tidyTelephones)):
		for j in range(first_third_depth, len(tidyTelephones)):
			for k in range(third_depth, len(tidyTelephones)):
				counter = 0
				#ignores duplicate positions in the i, j, k loop
				if(tidyTelephones[i] == tidyTelephones[j] or tidyTelephones[i] == tidyTelephones[k] or tidyTelephones[j] == tidyTelephones[k]):
					continue
				hemp = sec.make_circumcircle(tidyTelephones[i], tidyTelephones[j], tidyTelephones[k])
				if(hemp == None):
					continue
				for f in tidyTelephones:
					if(sec.is_in_circle(hemp, f)):
						counter += 1
						if counter == 12:
							break
				if  counter == 12:
					if(hemp[2] < smallest_circle or flag == 0):
						smallest_circle = hemp[2]
						flag = 1
	print(smallest_circle)
	#finalList = sorted(third_diameters, key=third_take_third)
	#third_count_points(finalList, 0)
		


def third_point(smaller, zippy_list, index):
	current_smallest = zippy_list[index][0][2]
	smallest_circ = zippy_list[index]
	for i in smaller:
		for point in tidyTelephones:
			if not sec.is_in_circle(zippy_list[i][0], point):
				circle = sec.make_circumcircle(zippy_list[i][1][0], zippy_list[i][1][1], point)	
				count = 0
				if(circle == None):
					continue
				elif (circle[2] < current_smallest):
					for p in tidyTelephones:
						if sec.is_in_circle(circle, p):	
							count += 1
					if count == 12:
						current_smallest = circle[2]
						smallest_circ = circle
	return smallest_circ


def driver(tidyTelephones):
	currentLargest = 0
	global depth
	global diameters
	global noDupes
	global res
	global index

	#IF less than 12 phones entered, exit
	if(len(tidyTelephones) < 12):
		print("Range is infinite. Less than 12 values entered")
		sys.exit(0)
	
	#take all the first points and then the potential second points, calculate
	#circles that define those two. 
	for i in range(len(tidyTelephones)):
		for j in range(depth, len(tidyTelephones)):
			#ignores duplicate positions in the i, j loop
			if(tidyTelephones[i] == tidyTelephones[j]):
				continue
			#make_diameter returns [0] and [1] = centre of circle. [2] = diameter
			temp = sec.make_diameter(tidyTelephones[i], tidyTelephones[j])

			point = (tidyTelephones[i], tidyTelephones[j])
			noDupes.append(point)
	
			# if there are 12 points in this diameter, yay 
			#if(sec.is_in_circle(temp, tidyTelephones[i])):
			diameters.append(temp)

		depth += 1

    # list1, list2 = (list(t) for t in zip(*sorted(zip(list1, list2))))
	
	#diameters, noDupes = (list(t) for t in zip(*sorted(zip(diameters, noDupes))))
	zipped = zip(diameters, noDupes)
	zipped = list(zipped)

	# res is zipping two lists together like a zip wow
	# and then sorting them by diameter
	res = sorted(zipped, key=take_third) 

	# SO HERE:
	# WE CAN GO THROUGH FROM THE smallest to THE largest of the list
	# FOR EACH DIAMETER, WE MAKE A CIRCLE WITH THE CORRESPONDING POINTS (ZIPPED)
	# if that circle we just made has more than 12 points, we don't need to do any diameters bigger than that
	# if it is two small, we don't need to make circles for any diameters (ie two points) smaller than that

	# ---------->---------> BOOM . CIRCLE. DONE.
	#for l in range(len(res)):
		#print(res[l][1])

	#mid = len(res)/2
	#print(mid)
	
	#print(res[0][1][0])
	#if find_best_circle returns a circle containing 12 points and a diameter, that = smallest circle
	#if find_best_circle cannot find a circle, try find_best_circle_three_points
	index = find_best_circle(res, 0)
	if(index == None):
		h = find_best_circle_three_points(tidyTelephones)
		# Diff input is 0 here
		smallest_circle = h
		sys.exit(0)
	else:
		smallest_circle = index
	
		
	# ******************************************************************************* ------<----------<-------
	# MURRAY ZOOM
	# ******************************************************************************* ------<----------<-------
	#COUNT how many points are inside that circle,
	#if atleast 12 points inside, and I have already found one that is smaller
	#than this one, i can throw this one away.


	#If no circle is found yet and contains more than 12 points, I THINK
	#We use it until we cull more...

	#
	# If it contains < 11 points and is smaller than the current, use those two
	#  points and any of the other three points (n choose 3).

	#
	#IF greater than 12 points, 'done'. 

	#
	#IF < 12 points, 'probably' not a good circle. Can choose another



file()
formatList(telephones)
driver(tidyTelephones)
#print("og smallest ---> ", res[index])
smallest = third_point(smaller, res, index)
if smallest == res[index]:
	print(res[index][0][2])
else:
	print(smallest[2])