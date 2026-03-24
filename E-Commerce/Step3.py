class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name + ": " + str(self.price)

    def get_information(self):
        return "Product: " + self.name + " | Price: " + str(self.price)


o1 = Product("Chair", 90)
o2 = Product("Laptop", 1200)
o3 = Product("Scarf", 24)

print(o1.get_information())
print(o2.get_information())
print(o3.get_information())