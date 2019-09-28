import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):
    #MAX INT TESTS
    def test_max_all_positions(self):
        tlist = [10, 9, 4]
        self.assertEqual(max_list_iter(tlist), 10)
        tlist = [9, 10, 4]
        self.assertEqual(max_list_iter(tlist), 10)
        tlist = [5, 8, 10]
        self.assertEqual(max_list_iter(tlist), 10)
    def test_multiple_max(self):
        # All 3 equal
        tlist = [10, 10, 10]
        self.assertEqual(max_list_iter(tlist), 10)
        # 2 equal
        tlist = [10, 10, 4]
        self.assertEqual(max_list_iter(tlist), 10)
        tlist = [9, 10, 10]
        self.assertEqual(max_list_iter(tlist), 10)
    def test_negatives(self):
        # Testing negatives
        tlist = [-10, -4, -1]
        self.assertEqual(max_list_iter(tlist), -1)
    def test_max_of_three_floats(self):
        self.assertAlmostEqual(max_list_iter([1.1,1.2,1.3]), 1.3)
        self.assertAlmostEqual(max_list_iter([1.2,1.3,1.1]), 1.3)
        self.assertAlmostEqual(max_list_iter([1.1,1.2,1.3]), 1.3)
    def test_none_or_null(self):
        #Test function names must start with TEST!!!
        """add description here"""

        # List is None
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        # List is empty
        tlist = []
        self.assertEqual(max_list_iter(tlist), None)


        '''
        tList = ['a', 'b', 'c']
        #TODO typeerror if it doesnt pass
        
        with self.assertRaises(TypeError):
            max_list_iter(tlist)
        '''


    #REVERSE TESTS
    def test_reverse_none_or_empty(self):
        # List ie None
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)
        # List is empty
        tlist = []
        self.assertEqual(reverse_rec(tlist), [])

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,4,3]), [3,4,1])
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    def test_reverse_floats(self):
        self.assertEqual(reverse_rec([1.1,2.2,3.3]), [3.3,2.2,1.1])
        self.assertEqual(reverse_rec([1.1,4.4,3.3]), [3.3,4.4,1.1])

    def test_reverse_negatives(self):
        self.assertEqual(reverse_rec([-1,-2,-3]), [-3,-2,-1])
        self.assertEqual(reverse_rec([-1.1,4.4,-3.3]), [-3.3,4.4,-1.1])

    def test_reverse_strings(self):
        self.assertEqual(reverse_rec(['a','b','c']), ['c','b','a'])
        self.assertEqual(reverse_rec(['hello', 'world', 'python3']), ['python3', 'world', 'hello'])

    #BINARY SEARCH TESTS
    def test_list_is_none(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(4, 0, 2, tlist)
    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)

        list_val = [4,5,6,7,8,9,10,11,12,13,14,15]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(13, low, high, list_val), 9)

    def test_bin_search_only_one(self):
        list_val = [1]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(1, 0, len(list_val) - 1, list_val), 0)

    def test_bin_search_0(self):
        list_val = [0]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(0, 0, high, list_val), 0)

    def test_bin_search_negatives(self):
        list_val = [-4,-3,-2,-1,0,1,2,3,4,5]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(-3, 0, high, list_val), 1)

    def test_bin_search_none(self):
        list_val = [7,8,9,10,11,12,13,14]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(19, 0, high, list_val), None)

        list_val = [7, 8, 9, 10, 11, 12, 13, 14]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(3, 0, high, list_val), None)

        list_val = [1, 3, 4, 6, 7, 9, 11, 15]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(5, 0, high, list_val), None)

        list_val = [1, 3, 4, 6, 7, 9, 11, 15]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(14, 0, high, list_val), None)

        list_val = []
        low = 0
        high = len(list_val) -1
        self.assertEqual(bin_search(1, 0, high, list_val), None)

    def test_bin_search_two(self):
        list_val = [2,4]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(4, 0, high, list_val), 1)

        list_val = [2, 4]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(2, 0, high, list_val), 0)

        list_val = [2, 4]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(3, 0, high, list_val), None)
if __name__ == "__main__":
        unittest.main()


