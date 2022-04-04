from range import Range
import unittest


class RangeTest(unittest.TestCase):
    def test_init_minmax(self):
        self.assertEqual(Range(1, 2)._end, [1, 2])

    def test_init_wrong_parameters(self):
        self.assertEqual(Range(2, 1)._end, [])

    def test_init_empty(self):
        self.assertEqual(Range()._end, [])

    def test_is_empty(self):
        self.assertTrue(Range().is_empty())

    def test_is_not_empty(self):
        self.assertFalse(Range(1, 2).is_empty())

    def test_is_inside(self):
        self.assertFalse(1 in Range(3, 2))

    def test_is_not_inside(self):
        self.assertFalse(1 in Range(3, 2))

    def test_range_equal(self):
        self.assertTrue(Range(1, -1) == Range(1, -1))

    def test_range_equal(self):
        self.assertFalse(Range(-1, 1) == Range(1, 3))

    def test_range_intersection(self):
        self.assertTrue(Range(1, 4).is_intersect(Range(3, 5)))

    def test_range_not_intersection(self):
        self.assertFalse(Range(1, 4).is_intersect(Range(4, 6)))

    def test_range_ingoing_to_first(self):
        self.assertTrue(Range(0, 3) > Range(1, 2))

    def test_range_ingoing_to_second(self):
        self.assertTrue(Range(1, 2) < Range(0, 3))

    def test_range_not_ingoing_to_first(self):
        self.assertFalse(Range(0, 3) > Range(1, 4))

    def test_range_not_ingoing_to_second(self):
        self.assertFalse(Range(1, 4) < Range(0, 3))

    def test_intersection(self):
        self.assertEqual(Range(1, 4) & Range(2, 6), Range(2, 4))

    def test_not_intersection(self):
        self.assertEqual(Range(1, 3) & Range(4, 6), [])

    def test_union(self):
        self.assertEqual(Range(1, 3) | Range(2, 6), Range(1, 6))

    def test_not_union(self):
        self.assertEqual(Range(1, 2) | Range(3, 4), [])

    def test_range_min(self):
        self.assertEqual(Range(1, 4).range_min(), 1)

    def test_range_max(self):
        self.assertEqual(Range(1, 4).range_max(), 4)

    def test_range_minmax_empty(self):
        self.assertIsNone(Range().range_min())

    def test_range_to_string(self):
        self.assertEqual(str(Range(1, 4)), "[1, 4]")

    def test_empty_range_to_string(self):
        self.assertEqual(str(Range()), "[]")

    def test_iterator(self):
        self.assertEqual([i for i in Range(-1, 2)], [-1, 0, 1, 2])

    def test_iterator_empty(self):
        self.assertEqual([i for i in Range()], [])

    def test_iterator_wrong_parameters(self):
        self.assertEqual([i for i in Range(1, -1)], [])


if __name__ == "__main__":
    unittest.main()
