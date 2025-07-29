import unittest

from stack import Stack


class StackTest(unittest.TestCase):
    def test_new_stack_is_empty(self):
        s = Stack()
        self.assertTrue(s.is_empty())

    def test_stack_after_push_is_not_empty(self):
        s = Stack()
        s.push(0)
        self.assertFalse(s.is_empty())

    def test_stack_after_push_pop_is_empty(self):
        s = Stack()
        s.push(0)
        s.pop()
        self.assertTrue(s.is_empty())

    def test_stack_pop(self):
        s = Stack()
        s.push(7)
        self.assertEqual(s.pop(), 7)
