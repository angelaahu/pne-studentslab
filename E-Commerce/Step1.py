class Product:
    def __init__(self, name = None, price = None):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name


o1 = Product("Tomato")
o2 = Product("Tomato",)
o3 = Product("Tomato")

print(o1)
print(o2)
print(o3)