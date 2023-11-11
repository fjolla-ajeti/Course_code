
#Task3
class Product:
    def __init__(self, product_type: str, name: str, price: float):
        self.type = product_type
        self.name = name
        self.price = price

class ProductStore:
    def __init__(self):
        self.products = {}
        self.income = 0

    def add(self, product: Product, amount: int):
        if product.name not in self.products:
            self.products[product.name] = {"type": product.type, "price": product.price * 1.3, "amount": 0}
        self.products[product.name]["amount"] += amount

    def set_discount(self, identifier: str, percent: float, identifier_type: str = 'name'):
        for product_name, product_info in self.products.items():
            if identifier_type == 'name' and product_name == identifier:
                product_info["price"] *= (1 - percent / 100)
            elif identifier_type == 'type' and product_info["type"] == identifier:
                product_info["price"] *= (1 - percent / 100)

    def sell_product(self, product_name: str, amount: int):
        if product_name not in self.products or self.products[product_name]["amount"] < amount:
            raise ValueError(f"Not enough {product_name} in stock")
        else:
            self.products[product_name]["amount"] -= amount
            self.income += amount * self.products[product_name]["price"]

    def get_income(self) -> float:
        return self.income

    def get_all_products(self) -> dict:
        return self.products

    def get_product_info(self, product_name: str) -> tuple:
        if product_name not in self.products:
            raise ValueError(f"{product_name} not found in the store")
        return product_name, self.products[product_name]["amount"]


product1 = Product("Electronics", "Laptop", 1000)
product2 = Product("Clothing", "T-shirt", 20)

store = ProductStore()

store.add(product1, 10)
store.add(product2, 50)

store.set_discount("Laptop", 10, identifier_type='name')
store.set_discount("Clothing", 5, identifier_type='type')

store.sell_product("Laptop", 5)
store.sell_product("T-shirt", 30)

print("Income:", store.get_income())
print("Product Information:", store.get_all_products())
print("Laptop Info:", store.get_product_info("Laptop"))
