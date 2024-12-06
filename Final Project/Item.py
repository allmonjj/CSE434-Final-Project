class Item:
    def __init__(self, name : str, description : str, effect : str):
        self.name = name
        self.description = description
        self.effect = effect

    def getName(self) -> str:
        return self.name

    def getDescription(self) -> str:
        return self.description

    def getEffect(self) -> str:
        return self.effect

    # Define __hash__ and __eq__ so that Item objects can be used as dictionary keys. (Has to be immutable)
    def __hash__(self):
        return hash((self.name, self.description))

    def __eq__(self, other) -> bool:
        return isinstance(other, Item) and self.name == other.name and self.description == other.description

    def __repr__(self) -> str:
        return f"Name : {self.name} - Description : {self.description} - Effect : {self.effect}"
