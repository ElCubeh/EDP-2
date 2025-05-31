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
    
    def test_poll_empty(self):
        empty_set = TreeSet()
        self.assertIsNone(empty_set.poll_first())
        self.assertIsNone(empty_set.poll_last())
        
    def test_clone(self):
        cloned_set = self.set.clone()
        self.assertNotEqual(id(self.set), id(cloned_set))
        self.assertEqual(self.set.size(), cloned_set.size())
        self.assertEqual(list(self.set), list(cloned_set))
    
    def test_add_null(self):
        with self.assertRaises(TypeError):
            self.set.add(None)
    
    def test_remove_non_existing(self):
        self.assertFalse(self.set.remove(10))
    
    def test_first_last_empty(self):
        empty_set = TreeSet()
        self.assertIsNone(empty_set.first())
        self.assertIsNone(empty_set.last())
    
    def test_large_set(self):
        large_set = TreeSet(range(1, 10001))
        self.assertEqual(large_set.size(), 10000)
        self.assertTrue(large_set.contains(5000))
        self.assertEqual(large_set.first(), 1)
        self.assertEqual(large_set.last(), 10000)
    
    def test_poll_empty_set(self):
        empty_set = TreeSet()
        self.assertIsNone(empty_set.poll_first())
        self.assertIsNone(empty_set.poll_last())
    
    def test_add_all(self):
        new_elements = [9, 10, 11]
        self.assertTrue(self.set.add_all(new_elements))
        self.assertEqual(self.set.size(), 8)
        self.assertTrue(self.set.contains(9))
        self.assertTrue(self.set.contains(10))
    
    def test_iter_empty_set(self):
        empty_set = TreeSet()
        asc = list(empty_set)
        self.assertEqual(asc, [])
        
        desc = list(empty_set.descending_iterator())
        self.assertEqual(desc, [])
    
if __name__ == '__main__':
    unittest.main()
