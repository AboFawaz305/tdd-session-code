class Stack:
    empty = True
    element = None

    def is_empty(self):
        return self.empty

    def push(self, e):
        self.empty = False
        self.element = e

    def pop(self):
        self.empty = True
        return self.element
