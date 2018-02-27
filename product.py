
class Product:
    """Class with product information"""

    def __init__(self, name, price, quantity, description):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description

    @property
    def productInfo(self):
        return 'Product: {}\nDescription: {}\n'.format(self.name, self.description)

    def __repr__(self):
        return '''
        Product:     {:}
        Price: $     {:.2f}
        Quantity:    {:}
        Description: {:}
        '''.format(self.name, self.price, self.quantity, self.description)