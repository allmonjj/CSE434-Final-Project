from Item import Item

class Inventory:
    def __init__(self):
        self.items = {}

    def add_Item(self, item: Item):
        if item not in self.items:
            self.items[item] = 0
        self.items[item] += 1

    def remove_Item(self, item: Item):
        if item in self.items and self.items[item] > 0:
            self.items[item] -= 1
            if self.items[item] == 0:
                del self.items[item]
        else:
            print(f"Don't have enough {item.name}'s!")

    def get_Inventory(self) -> dict:
        return self.items

    def __repr__(self) -> str:
        inventory_str = "Inventory:\n"
        for item, count in self.items.items():
            inventory_str += f"{item.__repr__()} - Quantity: {count}\n\n"
        return inventory_str
