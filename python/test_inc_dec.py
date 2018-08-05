import unittest
import inc_dec


class Test_IncrementDecrement(unittest.TestCase):
    def test_increment(self):
        result = inc_dec.increment(3)
        self.assertEquals(result, 4)

    def test_decrement(self):
        result = inc_dec.decrement(3)
        self.assertEquals(result, 2)


if __name__ == '__main__':
    unittest.main()
