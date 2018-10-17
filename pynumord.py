import unittest
import hypothesis
from hypothesis import given, assume, settings
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
    @settings(deadline=None, timeout=300, suppress_health_check = hypothesis.HealthCheck.all())
    @given(value_list = st.lists(st.characters()))  # how can I scramble the dict entries, while knowing what order I want them out in?
    def test_sorting(self, value_list):
        test_dict = dict(zip(range(len(value_list)), value_list))
        if test_dict:
            del test_dict[0]
            del value_list[0]

        if test_dict:
            @given(order_dict_out = st.lists(st.integers(min_value = 1, max_value = len(test_dict)), 
                                            min_size = len(test_dict), 
                                            max_size = len(test_dict),
                                            unique = True))
            def test_orders(self, order_dict_out):
                assume(i == 0 or i in order_dict_out for i in range(len(test_dict)))
                scrambled_dict = {}
                for key in order_dict_out:  # create a dictionary identical to test_dict, but entering key/value pairs in random order
                    scrambled_dict[key] = test_dict[key]
            
                array = [i for i in sort_nums(scrambled_dict)]
                self.assertEqual(array, value_list)


            test_orders(self)
        else:
            array = [i for i in sort_nums(test_dict)]
            self.assertEqual(array, value_list)





if __name__ == '__main__':
    unittest.main()