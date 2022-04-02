from range import Range
import unittest


class RangeTest(unittest.TestCase):
    def test_init(self):
        self.assertEqual(Range(1, 2).unit, [1, 2])
        self.assertEqual(Range(-2, -1).unit, [-2, -1])
        self.assertEqual(Range(-1, 1).unit, [-1, 1])

    def test_is_empty(self):
        self.assertTrue(Range().is_empty())
        self.assertFalse(Range(1, 2).is_empty())
        self.assertTrue(Range(1, 1).is_empty())
        self.assertTrue(Range(2, 1).is_empty())

    def test_is_inside(self):
        self.assertTrue(Range(1, 2).is_inside(1))
        self.assertFalse(Range(3, 2).is_inside(1))
        self.assertTrue(Range(1, 3).is_inside(2))

    def test_range_equal(self):
        self.assertTrue(Range(-1, 1) == Range(-1, 1))
        self.assertTrue(Range(1, -1) == Range(1, -1))
        self.assertFalse(Range(-1, 1) == Range(1, 3))

    def test_range_intersection(self):
        self.assertTrue(Range(1, 4) & Range(3, 5))
        self.assertTrue(Range(0, 2) & Range(-1, 1))
        self.assertFalse(Range(1, 4) & Range(4, 6))
        self.assertFalse(Range(1, 4) & Range())

    def test_range_ingoing(self):
        self.assertTrue(Range(0, 3) > Range(1, 2))
        self.assertTrue(Range(0, 3) < Range(-1, 4))
        self.assertFalse(Range() > Range(1, 2))
        self.assertFalse(Range(0, 3) > Range(1, 4))

    def test_intersection(self):
        self.assertEqual(Range(1, 4) * Range(2, 6), [2, 4])
        self.assertEqual(Range(1, 3) * Range(4, 6), [])
        self.assertEqual(Range() * Range(2, 6), [])

    def test_ingoiong(self):
        self.assertEqual(Range(1, 2) + Range(3, 4), [])
        self.assertEqual(Range(1, 4) + Range(), [])
        self.assertEqual(Range(1, 3) + Range(2, 6), [1, 6])

    def test_print_range(self):
        self.assertEqual(Range(-1, 2).print_range(), "-1, 0, 1, 2")

    def test_range_minmax(self):
        self.assertEqual(Range(1, 4).rmax(), 4)
        self.assertEqual(Range(1, 4).rmin(), 1)
        self.assertIsNone(Range().rmin())

    def test_range_to_string(self):
        self.assertEqual(Range(1, 4).to_string(), "[1, 4]")
        self.assertEqual(Range().to_string(), "[]")


if __name__ == "__main__":
    unittest.main()
