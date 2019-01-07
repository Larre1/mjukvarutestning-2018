import itertools
import unittest

def repeat_function(obj):
    items = []
    for i, item in enumerate(itertools.repeat(obj)):
        items.append(item)
        if i == 9:
            break
    return items


class TestItertools(unittest.TestCase):

    def test_whitebox_permutations(self):
        # These tests have been chosen with help of the flowchart to cover all edges and nodes.
        # Test 1 is for when r > n which is a prime path
        self.assertEqual(list(itertools.permutations('POBED', 34)), [])

        # Test 2 is the prime path for when we don't loop in any while or for loop
        self.assertEqual(list(itertools.permutations('P', 1)), [('P',)])

        # Test 3 runs the while loop once and also the for loop once. So this test covers two prime paths for when looping only once.
        self.assertEqual(list(itertools.permutations('PA', 1)), [('P',), ('A',)])

        # Test 4 runs both the while loop and for multiple times which covers our last prime paths.
        self.assertEqual(list(itertools.permutations('ABCD', 2)), [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'A'), ('B', 'C'), ('B', 'D'), ('C', 'A'), ('C', 'B'), ('C', 'D'), ('D', 'A'), ('D', 'B'), ('D', 'C')])


    def test_blackbox_dropwhile(self):
        # Dropwhile was tested with different values of first argument x, One 0, 6 which is bigger than any number in the list
        # and some other numbers inbetween. This way the outputs we expect to get returned should be empty for some cases and unchanged for some.
        self.assertEqual(list(itertools.dropwhile(lambda x: x < 5, [1, 4, 5, 4, 1])), [5, 4, 1])
        self.assertEqual(list(itertools.dropwhile(lambda x: x < 6, [1, 4, 5, 4, 1])), [])
        self.assertEqual(list(itertools.dropwhile(lambda x: x < 0, [1, 3, 4, 5, 4, 1])), [1, 3, 4, 5, 4, 1])
        self.assertEqual(list(itertools.dropwhile(lambda x: x < 4, [1, 4, 5, 4, 1])), [4, 5, 4, 1])

    def test_blackbox_compress(self):
        # Compress was tested with a different number of numbers and length of the second argument, since the second argument
        # is the one that compress and changes the first one. So there is a test case for when the second argument is shorter
        # than the first and one test case for when its longer.
        self.assertEqual(list(itertools.compress('ABCDCBA', [1, 0, 0, 1, 1])), ['A', 'D', 'C'])
        self.assertEqual(list(itertools.compress('ABCDCBA', [1])), ['A'])
        self.assertEqual(list(itertools.compress('ABCDCBA', [1, 0, 0, 1, 1, 1 , 1, 1])), ['A', 'D', 'C', 'B', 'A'])


    def test_blackbox_repeat(self):
        # Numbers and Strings was tested a finite number of times. Also infinite number of times was tested and with help
        # of the help function repeat_function it was limited to 10 times and the number 10 was used.
        self.assertEqual(list(itertools.repeat(20, 3)), [20, 20, 20])
        self.assertEqual(list(itertools.repeat('A', 10)), ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'])
        self.assertEqual(repeat_function(10), [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])


if __name__ == '__main__':
    unittest.main()