class Product:

    def __init__(self, prod_id, prod_name, mfg, qty, cost, category, warranty):  # parameters
        self.id_product = prod_id     #  attributes
        self.name = prod_name
        self.manufacturer = mfg
        self.quantity = qty

        self.amount = cost
        self.category = category
        self.warranty = warranty
    def __str__(self):   # this magic ,dunder or special method used to print(show) data of instances(object)
        return f"{self.id_product} -> {self.manufacturer} -> {self.name}"
        # return f"{self.__dict__}"   # return function must be string

        # return f"product_name={self.name}\nmanufacturer={self.manufacturer}\nquntity = {self.quantity}\n"\
        #        f"price={self.amount}\ncategory ={self.category}\nwarranty ={self.warranty}"

                   # return self.name + " => " + self.manufacturer  # can concatenate only string
    def __repr__(self):
        return str(self)

# instances(objects)
iron = Product(prod_id=1, prod_name="steam iron", mfg="Bajaj", qty=10, cost=750, category="electrical", warranty=1)
cell_phone = Product(prod_id=2, prod_name="G4", mfg="OPPO", qty=5, cost=7500, category="electronics", warranty=2)
watch = Product(prod_id=3, prod_name="wristwatch", mfg="timex", qty=10, cost=5000, category="accessories", warranty=3)
energy_drink = Product(prod_id=4, prod_name="boost", mfg="unilever", qty=10, cost=75, category="grocery", warranty=1)


print(iron)  #ans:- <__main__.Product object at 0x000002B140DF8400>...syntax= <dunder>class<object at>memory location<
print()
print(cell_phone)
print()
print(energy_drink)
print(type(energy_drink))  #<class '__main__.Product'>


print(iron.name)
print(iron.amount)
print(cell_phone.category)
print(cell_phone.warranty)
print(watch.manufacturer)
print(watch.quantity)
print(energy_drink.id_product)
print(energy_drink.name)

