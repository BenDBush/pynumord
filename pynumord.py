import unittest
import hypothesis
from hypothesis import given, assume
import hypothesis.strategies as st

def sort_nums(incoming):
    sought = 1
    store_early = {}
    print("New!!!")
    while len(incoming) > 0:
        print("Top")
        key, value = incoming.popitem()
        if key == sought:
            yield value
            sought += 1
            for a, b in check_store(sought, store_early):
                yield a
                sought = b

        else:
            store_early[key] = value
            print("Stored!")




def check_store(seek, store):
    while seek in store:
        found = store[seek]
        print("Check!")
        del store[seek]
        seek += 1
        yield found, seek



class TestOrders(unittest.TestCase):
    @given(value_list = st.lists(st.characters()), integer_list = st.integers(1))  # how can I scramble the dict entries, while knowing what order I want them out in?
    def test_sorting(self, chars):
        test_dict = dict(zip(range(len(chars)), chars))
        if test_dict:
            del test_dict[0]
            del chars[0]

        array = [i for i in sort_nums(test_dict)]
        self.assertEqual(array, chars)




if __name__ == '__main__':
    unittest.main()