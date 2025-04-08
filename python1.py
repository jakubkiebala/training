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


class Discount20PercentCart(Cart):
    def __init__(self):
        super().__init__()

    
    def add(self, price, tag):
        super().add(price, tag)

    
    def summary(self):
        products_list = []
        for product in self.products:
            list_product = list(product)
            tuple_product = tuple([list_product[0] * 0.8, product[1]])
            products_list.append(tuple_product)
        return print(f'your cart with a discount : {products_list}')


