##This file contains the help functions for the tests of itertools functions:
## - Cycle
## - Permutations
## - Chain
## - Chain.from_iterable
## - filterfalse
## - tee
## - zip_longest
## - Combinations (White box tests)

from itertools import cycle
from itertools import permutations
from itertools import chain
from itertools import filterfalse
from itertools import combinations

def cyclestop(input, cycle_for):
	#Stops cycle after n=cycle_for elements and puts items iterated through
	# in list
	cycle_items = []
	for i, item in enumerate(cycle(input)):
		if i < cycle_for:
			cycle_items.append(item)
		else:
			break

	return cycle_items

def permhelp(to_permutate):
	#Puts each permutation as an element in a list
	result = permutations(to_permutate)
	list_permutations = []
	for each in result:
		list_permutations.append(list(each))

	return list_permutations


def chainhelp(*iterables):
	#Puts all results generated from chain in list
	all_iterable_elements = []
	for item in chain(*iterables):
		all_iterable_elements.append(item)

	return all_iterable_elements

def chainhelp_single(iterables):
	all_iterable_elements_fi = []
	for item in chain.from_iterable(iterables):
		all_iterable_elements_fi.append(item)

	return all_iterable_elements_fi

#Returns items filtered through filterfalse in list
def filterfalsehelp(predicate, iterable):
	filtered_elements = []

	for item in filterfalse(predicate, iterable):
		filtered_elements.append(item)

	return filtered_elements

#Predicate function used in filterfalse to filter out list iterable
def filterfalse_pred1(input):
	iterable = ['b','d','c']
	if input in iterable:
		return True
	else:
		return False

#Predicate function used in filterfalse to filter out list iterable
def filterfalse_pred2(input):
	iterable = ["abcdef","ghi","lmnopjk","123"]
	if input in iterable:
		return True
	else:
		return False

#Predicate function used in filterfalse to filter out list iterable
def filterfalse_pred3(input):
	iterable = [[1,2],['d','e','f'],["test1","test2","test3"]]
	if input in iterable:
		return True
	else:
		return False

def comb_help(to_permutate, comb_length):
	result = combinations(to_permutate, comb_length)
	list_combinations = []
	for each in result:
		list_combinations.append(list(each))

	return list_combinations


def comb_help_length(to_permutate, comb_length):
	result = combinations(to_permutate, comb_length)
	iterations = 0
	for each in result:
		iterations = iterations + 1

	return iterations







