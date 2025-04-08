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
    def summary(self):
        products_list = []
        for product in self.products:
            list_product = list(product)
            tuple_product = tuple([list_product[0] * 0.8, product[1]])
            products_list.append(tuple_product)
        return print(f'your cart with a discount : {products_list}')


class Above3ProductsCheapestFreeCart(Cart):
    def summary(self):
        if len(self.products) >= 3:
            cheapest = min(self.products, key=lambda item: item[0])
            products_list = [(0, name) if (price, name) == cheapest else (price, name) for price, name in self.products]
            return print(f'your cart with cheapest for free : {products_list}')
        else:
            print(f'Your normal cart : {self.products}')
