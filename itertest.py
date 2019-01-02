#!/usr/bin/env python
# -*- coding: utf-8 -*- 

##This file contains the tests of itertools functions:
## - Cycle
## - Permutations
## - Chain
## - Chain.from_iterable
## - filterfalse
## - tee
## - zip_longest
import itertools as it
import unittest
import iterhelp

#As Cycle loops endlessly, to test it we must simulate some kind of ending,
#While still letting it loop long enough to show possible supposed infinite duration
class ItertestCycle(unittest.TestCase):
    #Itertools.cycle testing class
    def test_cycle_general(self):
        sample_input = ['a','b','c','d']
        expected_output_20 = ['a','b','c','d',\
        'a','b','c','d','a','b','c','d','a','b'\
        ,'c','d','a','b','c','d']
        #Cycle through 20 items
        cycle_20_output = iterhelp.cyclestop(sample_input,20)
        self.assertEqual(cycle_20_output, expected_output_20)

    def test_cycle_large_set(self):
        #testing of large values to cycle
        sample_input = [1]
        expected_output_200 = \
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,\
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,\
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,\
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,\
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,\
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,\
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,\
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,\
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,\
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        #Cycle through 200 items
        cycle_200_output = iterhelp.cyclestop(sample_input,200)
        self.assertEqual(cycle_200_output, expected_output_200)

    def test_non_uniform_values(self):
        #testing multiple types in list as input
        a = "a"
        sample_input = ["this", "is", a, 1234]
        cycle_non_uniform = iterhelp.cyclestop(sample_input, 1)
        self.assertEqual(cycle_non_uniform, cycle_non_uniform)
        #testing that invalid inputs to cycle raises errors
        with self.assertRaises(TypeError):
            it.cycle(123)
        with self.assertRaises(TypeError):
            it.cycle()

class ItertestPermutations(unittest.TestCase):
        #Itertools.permutations testing class
    def test_permutations_general(self):
        sample_input = ['a','b','c']
        possible_permutation_1 = ['b','c','a']
        possible_permutation_2 = ['a','c','b']
        possible_permutation_3 = ['c','b','a']
        possible_permutation_4 = ['c','a','b']
        possible_permutation_5 = ['b','a','c']
        possible_permutation_6 = ['a','b','c']
        #Permutate the set sample_input and put it all in one list
        permutated_input = iterhelp.permhelp(sample_input)

        #Check if every permutation of sample_input is in the list of permutations
        self.assertTrue(sample_input in permutated_input)
        self.assertTrue(possible_permutation_1 in permutated_input)
        self.assertTrue(possible_permutation_2 in permutated_input)
        self.assertTrue(possible_permutation_3 in permutated_input)
        self.assertTrue(possible_permutation_4 in permutated_input)
        self.assertTrue(possible_permutation_5 in permutated_input)
        self.assertTrue(possible_permutation_6 in permutated_input)

        #Check that values that should not exist in permutation does not exist
        self.assertFalse(['b','c','c'] in permutated_input)

    def test_permutations_large_set(self):
        #testing that the number of permutations is correct for large values
        #a permutation of set C with elements n is n!
        sample_input = ['a','b','c','d','e','f','h','i']

        permutated_input = iterhelp.permhelp(sample_input)
        self.assertEqual(len(permutated_input), 40320)

    def test_non_uniform_values(self):
        #Try more "odd" values that might give a different response
        sample_input = ['',[1,2,3]]
        possible_permutation_1 = ['',[1,2,3]]
        possible_permutation_2 = [[1,2,3],'']

        permutated_input = iterhelp.permhelp(sample_input)

        self.assertTrue(possible_permutation_1 in permutated_input)
        self.assertTrue(possible_permutation_2 in permutated_input)
        #testing that invalid inputs to permutations raises typeerror
        with self.assertRaises(TypeError):
            it.permutations(1234)

        with self.assertRaises(TypeError):
            it.permutations()

class ItertestChain(unittest.TestCase):
    #Supposed to test multiple sequences as a single sequence
    def testchaingeneral(self):
        #Test chain function, adding multiple iterators to a single list or sequence
        sample_input_1 = ['a','b','c']
        sample_input_2 = [1,2,3,4,5]
        sample_input_3 = ["abcdef","ghijkl","mnopqr","stuvzåöä"]
        sample_input_4 = [[1,2,3],['d','e','f'],["test1","test2","test3"]]

        expected_output_chain = ['a','b','c',1,2,3,4,5,"abcdef","ghijkl","mnopqr","stuvzåöä",[1,2,3],['d','e','f'],["test1","test2","test3"]]

        chain_output = iterhelp.chainhelp(sample_input_1,sample_input_2,sample_input_3,sample_input_4)

        self.assertEqual(expected_output_chain,chain_output)

        with self.assertRaises(TypeError):
            it.chain(pow(2))

    def testchain_fromiterable(self):
        #Test chain.from_iterable, like above but only takes one iterator and not several
        sample_input_fi_1 = ['a','b','c']
        sample_input_fi_2 = ["abcdef","ghijkl"]
        sample_input_fi_3 = [[1,2,3],['d','e','f'],["test1","test2","test3"]]

        expected_output_chain_fi_1 = ['a','b','c']
        expected_output_chain_fi_2 = ['a','b','c','d','e','f','g','h','i','j','k','l']
        expected_output_chain_fi_3 = [1,2,3,'d','e','f',"test1","test2","test3"]

        chain_output_fi_1 = iterhelp.chainhelp_single(sample_input_fi_1)
        chain_output_fi_2 = iterhelp.chainhelp_single(sample_input_fi_2)
        chain_output_fi_3 = iterhelp.chainhelp_single(sample_input_fi_3)

        self.assertEqual(expected_output_chain_fi_1, chain_output_fi_1)
        self.assertEqual(expected_output_chain_fi_2, chain_output_fi_2)
        self.assertEqual(expected_output_chain_fi_3, chain_output_fi_3)

        #This version of chain should only accept 1 iterator and not several
        with self.assertRaises(TypeError):
            it.chain.from_iterable(['a','b','c'],['b','c','d'])

        with self.assertRaises(TypeError):
            it.chain.from_iterable()


class ItertestFilterfalse(unittest.TestCase):

    def testfalsefilter(self):
        #Filters an iterable by a condition, i.e filters out all elements > 10
        sample_input_ff_1 = ['a','b','c']
        sample_input_ff_2 = [1,2,3,4,5,6,7,8,9,10]
        sample_input_ff_3 = ["abcdef","ghijkl","lmnopjk"]
        sample_input_ff_4 = [[1,2,3],['d','e','f'],["test1","test2","test3"]]

        expected_output_ff_1 = ['a']

        #Test filterfalse with a function that is not lambda
        filterFalse_output_1 = iterhelp.filterfalsehelp(\
        iterhelp.filterfalse_pred1,sample_input_ff_1)

        #Test filterfalse with lambda, that is commonly used
        filterFalse_output_2 = iterhelp.filterfalsehelp(lambda x: x >4, sample_input_ff_2)

        #Testing for "odd" and different values
        filterFalse_output_3 = iterhelp.filterfalsehelp(\
        iterhelp.filterfalse_pred2,sample_input_ff_3)
        filterFalse_output_4 = iterhelp.filterfalsehelp(\
        iterhelp.filterfalse_pred3,sample_input_ff_4)

        self.assertEqual(expected_output_ff_1,filterFalse_output_1)
        self.assertEqual([1,2,3,4],filterFalse_output_2)
        self.assertEqual(["ghijkl"], filterFalse_output_3)
        self.assertEqual([[1,2,3]],filterFalse_output_4)


        #Testing invalid inputs
        with self.assertRaises(TypeError):
            it.filterfalse()

        with self.assertRaises(TypeError):
            it.filterfalse("asd")

        with self.assertRaises(TypeError):
            it.filterfalse(sample_input_ff_1, iterhelp.filterfalse_pred3)


class ItertestTee(unittest.TestCase):

    def testTee(self):
        #Tee should return n iterables from a single iterable with tee(iterable, n)
        Iterable_to_multiply = ['a','b','c',1,2,3,"hello","python",["word"]]

        Iterable_1,Iterable_2,Iterable_3,Iterable_4 = it.tee(Iterable_to_multiply,4)

        #Have to convert the iterables to lists as otherwise you cannot compare
        #an iterable object to a list, even though they are the same
        self.assertEqual(list(Iterable_1), Iterable_to_multiply)
        self.assertEqual(list(Iterable_2), Iterable_to_multiply)
        self.assertEqual(list(Iterable_3), Iterable_to_multiply)
        self.assertEqual(list(Iterable_4), Iterable_to_multiply)

        self.assertEqual(list(Iterable_1), list(Iterable_2))
        self.assertEqual(list(Iterable_1), list(Iterable_3))
        self.assertEqual(list(Iterable_1), list(Iterable_4))


        #Testing invalid inputs
        with self.assertRaises(TypeError):
            test_invalid = it.tee()

        with self.assertRaises(TypeError):
            test_invalid_2 = it.tee(123,4)

        with self.assertRaises(TypeError):
            test_invalid_3 = it.tee(4, Iterable_to_multiply)


class ItertestZipLongest(unittest.TestCase):

    def testZiplongest(self):

        #Iterators to be combined or zipped 
        sample_input_zipL = [1,2,3,4,5,6,7,8,9]
        sample_input_zipL2 = [1,2,3,4,5]
        sample_input_zipL3 = ['a','b','c','d','e','f','g','h']
        sample_input_zipL4 = ["an","apple","a","day","keeps","the","doctor","away"]
        sample_input_zipL5 = [123,["Hello", "World"], False]
        sample_input_zipL6 = ["Short", "Iterable"]


        output_zipL = list(it.zip_longest(sample_input_zipL, sample_input_zipL2, fillvalue = None))
        #Testing to see that when fillvalue is unspecified it results in fillvalue = None
        output_zipL2 = list(it.zip_longest(sample_input_zipL, sample_input_zipL3))
        #Testing iterators of very different lengths and specified fillvalue
        output_zipL3 = list(it.zip_longest(sample_input_zipL2, sample_input_zipL3, fillvalue = 100))
        #Testing two iterators of same length
        output_zipL4 = list(it.zip_longest(sample_input_zipL4, sample_input_zipL))
        #Testing weird iterator values and other fillvalue value
        output_zipL5 = list(it.zip_longest(sample_input_zipL5, sample_input_zipL6, fillvalue = "fillvalue"))
        #Testing weird iterator values and other fillvalue value
        output_zipL6 = list(it.zip_longest(sample_input_zipL2, sample_input_zipL6, fillvalue = [1,2,3]))

        expected_output_zipL = [(1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, None)\
        ,(7, None),(8, None),(9, None)]

        expected_output_zipL2 = [(1, 'a'),(2, 'b'),(3, 'c'),(4, 'd'),(5, 'e'),(6, 'f')\
        ,(7, 'g'),(8, 'h'),(9, None)]

        expected_output_zipL3 = [(1, 'a'),(2, 'b'),(3, 'c'),(4, 'd'),(5, 'e'),(100, 'f')\
        ,(100, 'g'),(100, 'h')]

        expected_output_zipL4 = [("an", 1),("apple", 2),("a", 3),("day", 4),("keeps", 5),("the", 6)\
        ,("doctor", 7),("away", 8),(None, 9)]
        
        expected_output_zipL5 = [(123, "Short"),(["Hello", "World"], "Iterable"),(False, "fillvalue")]

        expected_output_zipL6 = [(1, "Short"),(2, "Iterable"),(3, [1,2,3]),(4, [1,2,3]),(5, [1,2,3])]

        self.assertEqual(output_zipL, expected_output_zipL)
        self.assertEqual(output_zipL2, expected_output_zipL2)
        self.assertEqual(output_zipL3, expected_output_zipL3)
        self.assertEqual(output_zipL4, expected_output_zipL4)
        self.assertEqual(output_zipL5, expected_output_zipL5)
        self.assertEqual(output_zipL6, expected_output_zipL6)

        #Testing invalid inputs, such as non-iterator values
        with self.assertRaises(TypeError):
            it.zip_longest(100, 20000)

        with self.assertRaises(TypeError):
            it.zip_longest(123)

        with self.assertRaises(TypeError):
            it.zip_longest([1,2,3],False)

class CombinationsWhiteboxTesting(unittest.TestCase):

    def testtoolongcomb(self):
        #By the flowchart specification the function will return (nothing) if the length of the itertable
        #is shorter than the argument r (length of combinations)
        sample_iterable = [1,2,3]
        sample_iterable_2 = ["this","is","a","sample"]

        #Tests when r > length(iterable)
        output_from_comb_1 = iterhelp.comb_help(sample_iterable, 8)
        output_from_comb_2 = iterhelp.comb_help(sample_iterable_2, 6)

        #Tests combinations normally
        output_from_comb_3 = iterhelp.comb_help(sample_iterable, 2)
        output_from_comb_4 = iterhelp.comb_help(sample_iterable_2, 2)

        expected_output_1 = []
        expected_output_2 = [[1,2], [1,3], [2,3]]
        expected_output_3 = [['this','is'],['this','a'],['this','sample'],['is','a'],['is','sample'],['a','sample']]

        #Tests that the first two outputs are an empty list,
        #as the argument r is bigger than the length of the iterable
        self.assertEqual(output_from_comb_1, expected_output_1)
        self.assertEqual(output_from_comb_2, expected_output_1)
        #Simply tests that the function works as intended otherwise
        self.assertEqual(output_from_comb_3, expected_output_2)
        self.assertEqual(output_from_comb_4, expected_output_3)

    def testwhileloop(self):
        #Supposed to to test the while loop and its different branches in the combinations function
        #The end/return case is when insices[i] = i + n - r so index + length of iterable - length argument r
        #Where indices = list(range(r)) so if r = 5 indices = [0,1,2,3,4]
        # n = 4, r = 3, indices = [0,1,2] => 

        #The amount of times that the function goes through the left hand side of the flow chart ending with yield output
        #is the same amount as number of elements in the list from the help function comb_help in iterhelp.py so we can test
        #how many times the function goes through each branch when indices[i] != i + n - r. It is difficult to test however if
        #function takes the most left hand side route or "middle" route as the function outputs the same thing no matter which path is taken

        sample_iterable = [1,2,3]
        sample_iterable_2 = ["this","is","a","sample"]

        output_from_comb_1 = iterhelp.comb_help_length(sample_iterable, 2)
        output_from_comb_2 = iterhelp.comb_help_length(sample_iterable_2, 2)
        output_from_comb_3 = iterhelp.comb_help_length(sample_iterable_2, 4)
        output_from_comb_4 = iterhelp.comb_help_length(sample_iterable, 3)

        #Test that the function outputs 3 times and thereby goes through the loop 3 times.
        self.assertEqual(output_from_comb_1, 3)
        #Test that the function outputs 6 times and thereby goes through the loop 6 times.
        self.assertEqual(output_from_comb_2, 6)
        #Test that when r = n the end condition insice[i] = i + n - r is met and the function only outputs once before the loop
        self.assertEqual(output_from_comb_3, 1)
        self.assertEqual(output_from_comb_4, 1)



if __name__ == '__main__':
    unittest.main()




    