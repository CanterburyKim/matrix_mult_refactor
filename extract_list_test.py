import unittest
from extract_list import extract_from_list

class TestMatrixMult(unittest.TestCase):
    """
    test class
    """
    def test_do_extract(self):
        """
        """
        list_of_tuples = [ (0,0), (1,1), (2,2), (3,1), (4,0) ]
        expected_result_a = [0, 1, 2, 3, 4]
        expected_result_b = [0, 1, 2, 1, 0]

        result_a, result_b = extract_from_list(list_of_tuples)
        print(f'{list_of_tuples} => {result_a} and {result_b}')

        self.assertEqual(result_a, expected_result_a)
        self.assertEqual(result_b, expected_result_b)


if __name__ == '__main__':
    unittest.main()
