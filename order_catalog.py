class OrderCatalog:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def add(self, order):
        self.orders.append(order)

    def get_info(self):
        if not self.orders:
            return "Savat bo'sh"
        text = f'{self.name}\n'
        for o in self.orders:
            text += f"{o.product.name} - {o.qty}\n"
        return text
