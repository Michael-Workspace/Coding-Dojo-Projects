class Product:
    def __init__(self, product_name, price, category):
        self.product_name = product_name
        self.price = price
        self.category = category
    
    def update_price(self,percent_change, is_increased):
        self.percent_change = percent_change
        self.is_increased = is_increased
        if is_increased == True:
            self.price += (self.price * percent_change)
        else:
            self.price -= (self.price * percent_change)
        return self
        
    def print_info(self):
        print(f'{self.product_name} is a {self.category} and costs ${self.price}')
        return self
    
class Store: 
    def __init__(self, store_name):
        self.store_name = store_name
        self.products = []
        
    def add_product(self, new_product):
        self.products.append(new_product)
        return self
    
    def sell_product(self, id):
        self.products.pop(id)
        self.print_info
        return self
    
    def inflation(self, percent_increase):
        self.percent_increase = percent_increase
        self.update_price
        return self
    
    def set_clearance(self, category, percent_discount):
        self.percent_discount = self.percent_discount
        if self.category == category:
            self.is_increased == False
        return self
    
target = Store('Target')
ps5 = Product('PS5', 1000, 'Gaming Console')
xbox = Product('Xbox', 2, 'Gaming Console')

target.add_product(ps5).add_product(xbox)
ps5.update_price(.5,True).print_info()
xbox.print_info().update_price(.2,True).print_info()