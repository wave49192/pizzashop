from enum import Enum


class PizzaSize(Enum):
    small = 180
    medium = 200
    large = 320
    jumbo = 450


class Pizza:
    """A pizza with a size and optional toppings."""

    def __init__(self, size: PizzaSize):
        if not isinstance(size, PizzaSize):
            raise TypeError("size must be a PizzaSize")
        self.size = size
        self.toppings = []

    def get_price(self):
        """Price of pizza depends on size and number of toppings."""
        return self.size.value + 20 * len(self.toppings)

    def add_topping(self, topping):
        """Add a topping to the pizza"""
        if topping not in self.toppings:
            self.toppings.append(topping)

    def __str__(self):
        description = self.size.name
        if self.toppings:
            description += " pizza with " + ", ".join(self.toppings)
        else:
            description += " plain cheese pizza"
            # print "A small pizza with seafood,mushroom"
        return description
