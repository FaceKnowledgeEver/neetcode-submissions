class StoreItem:
    def __init__(self, name : str, price : float):
        self.name = name
        self.price = price

chips = StoreItem("Chips", 1.99) # Don't modify this line

# TODO: Access the attributes of the chips object and display them

chips_name = chips.name
chips_price = chips.price
print(chips_name)
print(chips_price)
