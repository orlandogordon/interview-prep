import pytest
from arrays.test1 import coin_func
from arrays.min_stack import MinStack, use_min_stack

# https://realpython.com/pytest-python-testing/#what-makes-pytest-so-useful


class TestNumArrays:
    empty_arr = []
    short_arr = [1, 3, 2]
    long_arr = [1000, 21, 2, 54506, 33, 2, 3, 423, 65654, 76, 35, 67, 43, 76,21,123,56567,545345366, 34,56,32,76,12,15,16,17,342,54,87,67,123,45,3,764,85,367,35,67,95,94,93,15,19,19,]
    simple_arr = [6, 4, 1, 8, 2, 5, 16, 100]
    negative_arr = [-12, -1545, -1, -33, -765, -43, -81, -19]
    combo_arr = [-34, 500, -4, 12, 4, 67, 32, -14, 2, 89, 43]

    def test_array1(self):
        assert coin_func([1,2,3]) == 6

    def test_array2(self):
        assert coin_func([1,3,4]) == 8

    def test_minstack(self):
        input1a = ["MinStack","push","push","push","getMin","pop","top","getMin"]
        input1b = [[],[-2],[0],[-3],[],[],[],[]]
        excepted = [None,None,None,None,-3,None,0,-2]
        assert use_min_stack(input1a, input1b) == excepted
        


