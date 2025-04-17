from avl_tree import AVLTree
from collections.abc import Iterable, Iterator

class TreeSet:
    def __init__(self, collection=None):
        self.avl = AVLTree()
        self._size = 0
        
        if collection is not None:
            if not isinstance(collection, Iterable):
                raise TypeError("Argument must be iterable")
            for element in collection:
                self.add(element)
    
    def add(self, e):
        if not self.contains(e):
            self.avl.insert(e)
            self._size += 1
            return True
        return False
    
    def add_all(self, c):
        changed = False
        for element in c:
            if self.add(element):
                changed = True
        return changed
    
    def ceiling(self, e):
        current = self.avl.root
        ceil = None
        while current is not None:
            if current.value == e:
                return e
            elif current.value < e:
                current = current.right_child
            else:
                ceil = current.value
                current = current.left_child
        return ceil
    
    def clear(self):
        self.avl = AVLTree()
        self._size = 0
    
    def clone(self):
        new_set = TreeSet()
        new_set.avl = self.avl
        new_set._size = self._size
        return new_set
    
    def contains(self, o):
        return self.avl.search(o)
    
    def first(self):
        current = self.avl.root
        if current is None:
            return None
        while current.left_child is not None:
            current = current.left_child
        return current.value
    
    def last(self):
        current = self.avl.root
        if current is None:
            return None
        while current.right_child is not None:
            current = current.right_child
        return current.value
    
    def floor(self, e):
        current = self.avl.root
        floor = None
        while current is not None:
            if current.value == e:
                return e
            elif current.value > e:
                current = current.left_child
            else:
                floor = current.value
                current = current.right_child
        return floor
    
    def higher(self, e):
        current = self.avl.root
        higher = None
        while current is not None:
            if current.value > e:
                higher = current.value
                current = current.left_child
            else:
                current = current.right_child
        return higher
    
    def lower(self, e):
        current = self.avl.root
        lower = None
        while current is not None:
            if current.value < e:
                lower = current.value
                current = current.right_child
            else:
                current = current.left_child
        return lower
    
    def is_empty(self):
        return self._size == 0
    
    def poll_first(self):
        first = self.first()
        if first is not None:
            self.remove(first)
        return first
    
    def poll_last(self):
        last = self.last()
        if last is not None:
            self.remove(last)
        return last
    
    def remove(self, o):
        if self.avl.delete_value(o):
            self._size -= 1
            return True
        return False
    
    def size(self):
        return self._size
    
    def __iter__(self):
        return self.InOrderIterator(self.avl.root)
    
    def descending_iterator(self):
        return self.DescendingIterator(self.avl.root)
    
    class InOrderIterator(Iterator):
        def __init__(self, root):
            self.stack = []
            self._push_left(root)
        
        def _push_left(self, node):
            while node is not None:
                self.stack.append(node)
                node = node.left_child
        
        def __next__(self):
            if not self.stack:
                raise StopIteration
            node = self.stack.pop()
            self._push_left(node.right_child)
            return node.value
    
    class DescendingIterator(Iterator):
        def __init__(self, root):
            self.stack = []
            self._push_right(root)
        
        def _push_right(self, node):
            while node is not None:
                self.stack.append(node)
                node = node.right_child
        
        def __next__(self):
            if not self.stack:
                raise StopIteration
            node = self.stack.pop()
            self._push_right(node.left_child)
            return node.value
