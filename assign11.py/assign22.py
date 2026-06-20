class InvalidProductIndexError(Exception): pass
class OutOfStockError(Exception): pass
class InvalidQuantityError(Exception): pass
class EmptyInventoryError(Exception): pass

class Inventory:
    def __init__(self, quantities):
        if not quantities:
            raise EmptyInventoryError("EmptyInventoryError")
        self.quantities = quantities

    def purchase(self, index, quantity):
        if index < 0 or index >= len(self.quantities):
            raise InvalidProductIndexError("InvalidProductIndexError")
        if quantity <= 0:
            raise InvalidQuantityError("InvalidQuantityError")
        if quantity > self.quantities[index]:
            raise OutOfStockError("OutOfStockError")

        self.quantities[index] -= quantity
        print("Remaining stock:", self.quantities[index])


n = int(input())
qty = list(map(int, input().split()))
inv = Inventory(qty)

idx = int(input())
q = int(input())

try:
    inv.purchase(idx, q)
except Exception as e:
    print(e)