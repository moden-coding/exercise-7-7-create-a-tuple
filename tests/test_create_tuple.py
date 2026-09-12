import unittest

from src.create_tuple import create_tuple


class TestCreateTuple(unittest.TestCase):
    """create_tuple(x, y, z) -> (min, max, sum) of the three arguments."""

    def test_returns_a_tuple(self):
        result = create_tuple(1, 2, 3)
        self.assertIsInstance(
            result,
            tuple,
            msg="create_tuple(1, 2, 3) must return a tuple. Got %r." % (result,),
        )

    def test_worked_example(self):
        result = create_tuple(1, 4, 2)
        self.assertEqual(
            result,
            (1, 4, 7),
            msg="create_tuple(1, 4, 2) should be (1, 4, 7): the smallest "
            "value (1), the largest value (4), and the sum (1+4+2=7), in "
            "that order.",
        )

    def test_unordered_arguments(self):
        result = create_tuple(10, 8, 5)
        correct = (min(10, 8, 5), max(10, 8, 5), sum((10, 8, 5)))
        self.assertEqual(
            result,
            correct,
            msg="create_tuple(10, 8, 5) should be %r: the tuple order is "
            "always (min, max, sum), regardless of the order the arguments "
            "were passed in." % (correct,),
        )

    def test_negative_numbers(self):
        result = create_tuple(-10, -11, -12)
        correct = (min(-10, -11, -12), max(-10, -11, -12), sum((-10, -11, -12)))
        self.assertEqual(
            result,
            correct,
            msg="create_tuple(-10, -11, -12) should be %r: min/max/sum must "
            "work correctly with negative numbers too." % (correct,),
        )

    def test_large_numbers(self):
        result = create_tuple(55, 550, 5500)
        correct = (55, 5500, 6105)
        self.assertEqual(
            result,
            correct,
            msg="create_tuple(55, 550, 5500) should be (55, 5500, 6105): "
            "(min=55, max=5500, sum=55+550+5500=6105).",
        )

    def test_all_equal_arguments(self):
        result = create_tuple(4, 4, 4)
        self.assertEqual(
            result,
            (4, 4, 12),
            msg="create_tuple(4, 4, 4) should be (4, 4, 12): when all three "
            "arguments are equal, min and max are both that value, and the "
            "sum is three times the value.",
        )


if __name__ == "__main__":
    unittest.main()
