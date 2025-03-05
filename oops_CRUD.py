# CRUD => Create = Read = Update = Delete
# pep8 => used to mentioned python convention.
from product_example import Product

database = []
# print(database)

class ProductCRUD:


    def create(self, product):
        database.append(product)
        # print(product)

    def read(self):
        pass

    def read_one(self, product_id):
        for product in database:
            if product.id_product == product_id:
                return product

    def update(self):
        pass

    def delete(self, product_id):
        for product in database:
            if product.id_product == product_id:
                database.remove(product)


pc = ProductCRUD()

iron = Product(prod_id="sony", prod_name="steam iron", mfg="Bajaj", qty=10, cost=750, category="electrical", warranty=1)
cell_phone = Product(prod_id=2, prod_name="G4", mfg="OPPO", qty=5, cost=7500, category="electronics", warranty=2)
watch = Product(prod_id=3, prod_name="wristwatch", mfg="timex", qty=10, cost=5000, category="accessories", warranty=3)
energy_drink = Product(prod_id=4, prod_name="boost", mfg="unilever", qty=10, cost=75, category="grocery", warranty=1)

pc.create(iron)
pc.create(cell_phone)
pc.create(watch)
pc.create(energy_drink)

print(database)
# print(pc.read_one(3))

(pc.delete('vivo'))
print(database)
