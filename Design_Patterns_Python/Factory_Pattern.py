


class Product():
    
    def __init__(self) -> None:
        pass
    
    def do_product_stuff(self):
        print("Product")
        
class Product_A(Product):
    
    def do_product_stuff(self):
        print("Product A")
        
class Product_B(Product):
    
    def do_product_stuff(self):
        print("Product B")


class Creator():
    
    def __init__(self) -> None:
        pass
    
    def do_stuff(self):
        p = self.create_product()
        p.do_product_stuff()
    
    def create_product(self) -> Product:
        raise NotImplementedError("This function is not implemented for this class.")
    
    
class Creator_A(Creator):
    
    def create_product(self) -> Product:
        return Product_A()
    
class Creator_B(Creator):
    
    def create_product(self) -> Product:
        return Product_B()
        
        
c_a = Creator_A()
c_a.do_stuff()
