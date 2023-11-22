from models.product import Product
class ShoppingCart:
    def __init__(self) -> None:
        #si un atributo empieza con __ es privado
        # self.__products = list()
        self.__products: List[Product] = []
    
    @property
    def products(self):
        return self.__products.copy()
    
    @property
    def total(self) -> float:
        total = sum([(product.price - product.discount) for product in self.__products])
        return total

    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    def empty(self) -> bool:
        return len(self.__products) == 0
    
    def has_products(self) -> bool:
        return not self.empty()
    
    def remove_product(self, product: Product) -> None:
        self.__products.remove(product)