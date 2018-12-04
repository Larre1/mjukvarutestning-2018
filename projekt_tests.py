import unittest
from itertools import accumulate 
from itertools import chain

class Tests(unittest.TestCase):
    
    def setUp(self):
        self.list_0 = [1]
        self.list_1 = [1,2,3]
        self.list_2 = [1,2,3,4]
        self.list_3 = [1,2,3,4,5]
        self.list_4 = [1,2,3,4,5,6]
        self.list_5 = [3,4,5,1,2,8,2]
    
    def test_accumulate(self):
        #accumulate returns a list where [1] = [1], [2]=[1]+[2] etc.
        self.assertEqual(list(accumulate(self.list_0)),[1])
        self.assertEqual(list(accumulate(self.list_1)),[1,3,6])
        self.assertEqual(list(accumulate(self.list_2)),[1,3,6,10])
        self.assertEqual(list(accumulate(self.list_3)),[1,3,6,10,15])
        self.assertEqual(list(accumulate(self.list_4)),[1,3,6,10,15,21])

        #Return the maximum value encountered when iterating through a list
        self.assertEqual(list(accumulate(self.list_1,max)),[1,2,3])
        self.assertEqual(list(accumulate(self.list_5,max)),[3,4,5,5,5,8,8])

        #Return the minimum value encountered
        self.assertEqual(list(accumulate(self.list_1,min)),[1,1,1])
        self.assertEqual(list(accumulate(self.list_5,min)),[3,3,3,1,1,1,1])

    def test_chain(self):
        #chain adds two lists together making the second lists first element come after the first lists last element
        self.assertEqual(list(chain(self.list_0, self.list_1)),[1,1,2,3])

if __name__ == '__main__':
	unittest.main()
        