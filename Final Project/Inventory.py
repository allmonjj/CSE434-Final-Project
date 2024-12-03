class Inventory:
    def __init__(self):
        self.items = {}

    def add_Item(self, item):
        if item not in self.items:
            self.items[item] = 0
        self.items[item] += 1

    def remove_Item(self, item):
        if item in self.items and self.items[item] > 0:
            self.items[item] -= 1
            if self.items[item] == 0:
                del self.items[item]
        else:
            print(f"Don't have enough {item.name}'s!")

    def get_Inventory(self):
        return self.items