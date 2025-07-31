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

    def test_stack_after_3pushes_3pops_follow_lifo_strategy(self):
        """
        Note by this test we specified that the stack should have remember its
        previous elements so now we will have to make it store its previous
        elements in a list in stack.py
        """
        s = Stack()
        s.push(0)
        s.push(8)
        s.push(3)
        self.assertFalse(s.is_empty())
        self.assertEqual(s.pop(), 3)
        self.assertFalse(s.is_empty())
        self.assertEqual(s.pop(), 8)
        self.assertFalse(s.is_empty())
        self.assertEqual(s.pop(), 0)
        self.assertTrue(s.is_empty())
        # By this assertion we specified that poping an empty stack must returns
        # None
        self.assertIsNone(s.pop())
        self.assertTrue(s.is_empty())
