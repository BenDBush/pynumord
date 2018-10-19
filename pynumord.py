import unittest
import hypothesis
from hypothesis import given, assume, settings
import hypothesis.strategies as st

def sort_nums(incoming):
    """side effect: deletes incoming as it processes it. If we wanted to avoid that,
    we could copy incoming to a local variable."""
    sought = 1
    store_early = {}
    while len(incoming) > 0:
        key, value = incoming.popitem()
        if key == sought:
            yield value
            sought += 1
            for a, b in check_store(sought, store_early):
                yield a
                sought = b

        else:
            store_early[key] = value




def check_store(seek, store):
    while seek in store:
        found = store[seek]
        del store[seek]
        seek += 1
        yield found, seek



class TestOrders(unittest.TestCase):
    @settings(deadline=None, timeout=hypothesis.unlimited, suppress_health_check = hypothesis.HealthCheck.all())
    @given(test_dict = st.dictionaries(st.integers(min_value = 1),
                                        st.characters()))
    def test_sorting(self, test_dict):
        for i in range(len(test_dict) + 1):
            assume(i == 0 or i in test_dict)

        copy_of_test_dict = test_dict.copy()
        ordered_values = [i for i in sort_nums(test_dict)]
        if len(copy_of_test_dict) > 0:
            comparison_list = [copy_of_test_dict[i+1] for i in range(len(copy_of_test_dict))]
            self.assertEqual(ordered_values, comparison_list)
        else:
            self.assertEqual(ordered_values, [])





if __name__ == '__main__':
    unittest.main()