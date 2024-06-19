from abc import ABC, abstractmethod
from container import Container


class ComponentIterator(ABC):
    @abstractmethod
    def get_next(self):
        pass

    @abstractmethod
    def has_more(self):
        pass


class ContainerIterator(ComponentIterator):
    def __init__(self, root):
        self.stack = [root]

    def get_next(self):
        if self.has_more():
            current = self.stack.pop()
            return current
        return None

    def has_more(self):
        return len(self.stack) > 0
