class Comodity:
    def __init__(self, id, name, price, purchase_price):
        self.id = id
        self.name = name
        self.price = price
        self.purchase_price = purchase_price

    def cost_ratio(self):
        ratio = (self.purchase_price / self.price)
        return ratio

    