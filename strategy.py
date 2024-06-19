from abc import ABC, abstractmethod


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, component, style, icon_family):
        pass


class TreeDisplayStrategy(DisplayStrategy):
    def display(self, component, style, icon_family):
        result = ""
        for i, child in enumerate(component):
            result += child.draw(style, icon_family, "", i == len(list(component)) - 1)
        return result


class RectangleDisplayStrategy(DisplayStrategy):
    def display(self, component, style, icon_family):
        result = ""
        for i, child in enumerate(component):
            result += child.draw(style, icon_family, "", i == len(list(component)) - 1)
        return result
