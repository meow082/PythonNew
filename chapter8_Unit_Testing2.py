import chapter8_Unit_Testing as cap
import unittest

class MyTest(unittest.TestCase):
    def test_one(self):
        test = "sample"
        result = cap.cap_text(test)
        self.assertEqual(result, "Sample")

    def test_two(self):
        test = "just testing"
        result = cap.cap_text(test)
        self.assertEqual(result, "Just Testing")



if __name__ == '__main__':
    unittest.main()