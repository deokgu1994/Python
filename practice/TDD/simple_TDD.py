import unittest

def add(x,y):
    return x+y


class SimpleTest(unittest.TestCase):
    def testadd(self):
        self.assertEqual(add(4,5), 9)

    @unittest.expectedFailure
    def testaddfail(self):
        self.assertEqual(add(-0.5, 1), 1.5)
    pass

if __name__ == "__main__":
    unittest.main()
    
