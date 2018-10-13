import unittest

def sort_nums(incoming):
    sought = 1
    while len(incoming) > 0:
        key, value = incoming.popitem()
        if key == sought:
            yield value
        else:
            pass


class TestExtremeOrders(unittest.TestCase):
    def test_happy(self):
        dict_happy = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j'}
        array = [i for i in sort_nums(dict_happy)]
        self.assertEqual(array, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])


    def test_reversed(self):
        dict_reversed = {10: 'j', 9: 'i', 8: 'h', 7: 'g', 6: 'f',
                         5: 'e', 4: 'd', 3: 'c', 2: 'b', 1: 'a'}
        array = [i for i in sort_nums(dict_reversed)]
        self.assertEqual(array, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])


    def test_big(self):
        dict_big = {i: 'a' for i in range(10000)}
        del dict_big[0]
        array = [i for i in sort_nums(dict_big)]
        self.assertEqual(array, ['a' for i in range(9999)])


    def test_small(self):
        array = [i for i in sort_nums({1: 'a'})]
        self.assertEqual(array, ['a'])




if __name__ == '__main__':
    unittest.main()