class Order:
    def __init__(self, product, qty):
        self.product = product
        self.qty = qty

    def total_prise(self):
        return self.product.price * self.qty