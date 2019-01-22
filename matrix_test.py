import unittest
from matrix_lib_REF import matrix_vector_mult

class TestMatrixMult(unittest.TestCase):
    """
    test class
    """
    def test_do_mult_OLD(self):
        """
        """

        matrix = [ [2,3],[4,5] ]
        vector = [  [1], [2] ]
        expected_result = [[8], [14]]

        result = matrix_vector_mult(matrix, vector)
        print(f'{matrix} * {vector} = {result}')

        self.assertEqual(result, expected_result)

    def test_do_mult_REFACTOR(self):
        """
        """

        matrix = [ [2,3],[4,5] ]
        vector = (1,2)
        expected_result = (8,14)

        result = matrix_vector_mult(matrix, vector)
        print(f'{matrix} * {vector} = {result}')

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
