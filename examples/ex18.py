import unittest
from myutils import subtotal


class TestMyutilsSubtotal(unittest.TestCase):
    
    def test_sum_of_valid_inputs(self):
        expected = 100
        actual = subtotal(1, 10, 40, 50)
        self.assertEqual(expected, actual)

    def test_sum_of_negative_inputs(self):
        want = -3
        got = subtotal(1, -1, -1, -1)
        self.assertEqual(want, got)

    def test_for_invalid_kind(self):
        try:
            subtotal(10, 1, 2, 3)
            self.fail('was expecting a ValueErorr; didn\'t get one!')
        except ValueError:
            pass

    def test_for_invalid_type_of_kind(self):
        with self.assertRaises(TypeError) as e:
            subtotal("asdf", 1, 2, 3)


if __name__ == '__main__':
    unittest.main()