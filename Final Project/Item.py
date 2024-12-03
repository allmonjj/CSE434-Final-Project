class Item:
    def __init__(self, name, description, effect):
        self.name = name
        self.description = description
        self.effect = effect

    # Define __hash__ and __eq__ so that Item objects can be used as dictionary keys. (Has to be immutable)
    def __hash__(self):
        return hash((self.name, self.description))

    def __eq__(self, other):
        return isinstance(other, Item) and self.name == other.name and self.description == other.description

    def __repr__(self):
        return f"Item(name={self.name}, description={self.description}, effect={self.effect})"
