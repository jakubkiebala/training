class Cart:
    def __init__(self):
        self.products = []
        

    def add(self, price, tag):
        if isinstance(price, (int, float)) and isinstance(tag, str):
            product = (price, tag)
            self.products.append(product)
        else:
            print('wrong data')


    def summary(self):
        return print(f'Your cart  includes : {self.products}')

