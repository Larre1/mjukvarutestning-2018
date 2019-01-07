import unittest
import itertools as it
import Helpfunctions
import operator

class Tests(unittest.TestCase):
    
    ##Document contains tests for functions:
    ## accumulate
    ## count
    ## takewhile
    ## islice


    ## Function accumuluate(iterable[,func]) makes an iterator that returns accumulated sums
    ## or accumulated results if func is supplied
    def test_accumulate(self):
        list_0 = [1]
        list_1 = [1,2,3]
        list_2 = [1,2,3,4]
        list_3 = [1,2,3,4,5]
        list_4 = [1,2,3,4,5,6]
        list_5 = [3,4,5,1,2,8,2]
 
 
        #accumulate returns a list where [1] = [1], [2]=[1]+[2] etc.
        self.assertEqual(list(it.accumulate(list_0)),[1])
        self.assertEqual(list(it.accumulate(list_1)),[1,3,6])
        self.assertEqual(list(it.accumulate(list_2)),[1,3,6,10])
        self.assertEqual(list(it.accumulate(list_3)),[1,3,6,10,15])
        self.assertEqual(list(it.accumulate(list_4)),[1,3,6,10,15,21])

        #Return the maximum value encountered when iterating through a list
        self.assertEqual(list(it.accumulate(list_1,max)),[1,2,3])
        self.assertEqual(list(it.accumulate(list_5,max)),[3,4,5,5,5,8,8])

        #Return the minimum value encountered
        self.assertEqual(list(it.accumulate(list_1,min)),[1,1,1])
        self.assertEqual(list(it.accumulate(list_5,min)),[3,3,3,1,1,1,1])
        
        #multiply values
        self.assertEqual(list(it.accumulate(list_1,operator.mul)),[1,2,6])

        ##Can only take one function
        with self.assertRaises(TypeError):
            it.accumulate(list_1, max, operator.mul)
   
   
    ## Function count(start,step) makes an iterator that returns evenly spaced
    ## values starting with number start, with space step between them.
    ## If no values are given start is set to 0 and step to 1.
    ## count will keep on counting endlessly so to test it we need to make it stop.
    ## We use a helpfunction called count_stop which takes a start, step and a value to tell the
    ## function how many steps it should count.
    def test_count(self):
        start_1 = 0
        start_2 = 10
        step_1 = 1
        step_2 = 3
        number_of_steps_1 = 5
        number_of_steps_2 = 8
        
        expected_output_1 = [0,1,2,3,4,5]
        expected_output_2 = [10,13,16,19,22,25,28,31,34]

        self.assertEqual(Helpfunctions.count_stop(start_1,step_1,number_of_steps_1), expected_output_1)
        self.assertEqual(Helpfunctions.count_stop(start_2,step_2,number_of_steps_2), expected_output_2)

    ## count only takes two arguments, we use 3 arguments above to be able to use our helpfunction
        with self.assertRaises(TypeError):
            it.count(1,2,3)


    ##function takewhile(predicate, iterable) makes an iterator that returns elements from the iterable as long as the predicate is true
    def test_takewhile(self):
    
        self.assertEqual(list(it.takewhile(lambda x: x < 5, [1,2,3,4,5,6,7])), [1,2,3,4])
        self.assertEqual(list(it.takewhile(lambda x: x < 8, [1,2,3,4,5,6,7])), [1,2,3,4,5,6,7])
        self.assertEqual(list(it.takewhile(lambda x: x > 5, [6,7,8,1])), [6,7,8])
        self.assertEqual(list(it.takewhile(lambda x: x > -1, [1,2,3,4])), [1,2,3,4])
        self.assertEqual(list(it.takewhile(lambda x: x == 1, [1,2,3])), [1])


    

    ## function islice(iterable, stop), islice(iterable,start,stop[,step])
    ## makes an iterator that returns selected elements from the iterable.
    ## With one arg, takes all elements untill the given stop.
    ## With two args, first arg is start value and second stop
    ## with three args, first is stop, second is stop and third step value
    ## if start is None iteration starts at 0, if step is None, step deafults to 1
    def test_islice(self):
        slice_input = "ABCDEFG"
        start_1 = 2
        start_2 = 0
        start_3 = 8
        stop_1 = None
        stop_2 = 2
        step_1 = 2
        
        negative = -1

        expected_output_1 = ['A', 'B']
        expected_output_2 = ['C', 'D', 'E', 'F','G' ]
        expected_output_3 = ['A', 'C', 'E', 'G']
        expected_output_4 = ['A', 'B', 'C', 'D', 'E', 'F','G']

        self.assertEqual(Helpfunctions.help_islice(slice_input, stop_2), expected_output_1)
        self.assertEqual(Helpfunctions.help_islice_2(slice_input, start_1, stop_1), expected_output_2)
        self.assertEqual(Helpfunctions.help_islice_3(slice_input, start_2, stop_1,step_1), expected_output_3)
        self.assertEqual(Helpfunctions.help_islice(slice_input, start_3), expected_output_4)
        
        ##None of the arguments can be negative
        with self.assertRaises(ValueError):
            it.islice(slice_input, negative)
        with self.assertRaises(ValueError):
            it.islice(slice_input, start_1, negative)
        with self.assertRaises(ValueError):    
            it.islice(slice_input, start_1, stop_1, negative)
            

if __name__ == '__main__':
	unittest.main()
        