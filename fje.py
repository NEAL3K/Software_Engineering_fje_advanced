import argparse
import json
from container import Container, Leaf
from style import TreeStyleFactory, RectangleStyleFactory
from icon_family import icon_families
from iterator import ComponentIterator
from strategy import TreeDisplayStrategy, RectangleDisplayStrategy


class FunnyJsonExplorer:
    def __init__(self, style_factory, icon_family, display_strategy):
        self.style_factory = style_factory
        self.icon_family = icon_family
        self.display_strategy = display_strategy

    def show(self, data):
        builder = JSONBuilder()
        root = builder.build(data)
        style = self.style_factory.create_style()
        iterator = ComponentIterator(root)
        result = self.display_strategy.display(iterator, style, self.icon_family)
        print(result)

    def load(self, filepath):
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)


class JSONBuilder:
    def build(self, data, name="root", level=0):
        if isinstance(data, dict):
            container = Container(name, level)
            for key, value in data.items():
                child = self.build(value, key, level + 1)
                container.add(child)
            return container
        else:
            return Leaf(name, data)

# python fje.py -f example.json -s rectangle -i poker
def main():
    parser = argparse.ArgumentParser(description="Funny JSON Explorer")
    parser.add_argument(
        "-f", "--file", type=str, required=True, help="Path to the JSON file"
    )
    parser.add_argument(
        "-s",
        "--style",
        choices=["tree", "rectangle"],
        default="tree",
        help="Visualization style",
    )
    parser.add_argument(
        "-i",
        "--icon_family",
        choices=list(icon_families.keys()),
        default="basic",
        help="Icon family to use",
    )
    args = parser.parse_args()

    selected_icon_family = icon_families[args.icon_family]
    style_factory = (
        TreeStyleFactory() if args.style == "tree" else RectangleStyleFactory()
    )
    display_strategy = (
        TreeDisplayStrategy() if args.style == "tree" else RectangleDisplayStrategy()
    )

    explorer = FunnyJsonExplorer(style_factory, selected_icon_family, display_strategy)
    data = explorer.load(args.file)
    explorer.show(data)


if __name__ == "__main__":
    main()
