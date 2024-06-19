from container import Container


class ComponentIterator:
    def __init__(self, root):
        self.stack = [root]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stack:
            raise StopIteration
        current = self.stack.pop(0)
        if isinstance(current, Container):
            self.stack = list(current.children) + self.stack
        return current
