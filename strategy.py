from abc import ABC, abstractmethod
from style import TreeStyle, RectangleStyle


class Context:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def display(self, component, style, icon_family):
        return self.strategy.display(component, style, icon_family)


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, component, icon_family):
        pass


class TreeDisplayStrategy(DisplayStrategy):
    def display(self, component, style, icon_family):
        result = ""
        while component.has_more():
            result += component.get_next().draw(
                style, icon_family, "", not component.has_more()
            )
        return result


class RectangleDisplayStrategy(DisplayStrategy):
    def display(self, component, style, icon_family):
        result = ""
        while component.has_more():
            result += component.get_next().draw(
                style, icon_family, "", not component.has_more()
            )
        return result
