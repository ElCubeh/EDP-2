import unittest
from treeset import TreeSet

class TestTreeSet(unittest.TestCase):
    def setUp(self):
        self.set = TreeSet([5, 2, 8, 1, 3])
    
    def test_add(self):
        self.assertTrue(self.set.add(4))
        self.assertFalse(self.set.add(5))
        self.assertEqual(self.set.size(), 6)
    
    def test_contains(self):
        self.assertTrue(self.set.contains(2))
        self.assertFalse(self.set.contains(10))
    
    def test_ceiling(self):
        self.assertEqual(self.set.ceiling(4), 5)
        self.assertEqual(self.set.ceiling(8), 8)
    
    def test_floor(self):
        self.assertEqual(self.set.floor(4), 3)
        self.assertEqual(self.set.floor(1), 1)
    
    def test_size(self):
        self.assertEqual(self.set.size(), 5)
        self.set.add(10)
        self.assertEqual(self.set.size(), 6)
    
    def test_first_last(self):
        self.assertEqual(self.set.first(), 1)
        self.assertEqual(self.set.last(), 8)
    
    def test_poll(self):
        self.assertEqual(self.set.poll_first(), 1)
        self.assertEqual(self.set.poll_last(), 8)
        self.assertEqual(self.set.size(), 3)
    
    def test_clear(self):
        self.set.clear()
        self.assertTrue(self.set.is_empty())
    
    def test_iterators(self):
        asc = list(self.set)
        self.assertEqual(asc, [1, 2, 3, 5, 8])
        
        desc = list(self.set.descending_iterator())
        self.assertEqual(desc, [8, 5, 3, 2, 1])

if __name__ == '__main__':
    unittest.main()
