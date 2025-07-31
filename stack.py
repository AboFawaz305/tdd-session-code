class Stack:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def push(self, e):
        self.elements.append(e)

    def pop(self):
        if self.is_empty():
            return None
        return self.elements.pop()
