class Car:
    def __init__(self,make,colour,model,price,engine,seat=5):
        self.make =make
        self.colour_coat=colour
        self.model_year=model
        self.price_details=price
        self.engine_type=engine
        self.seat=seat

        if self.make.lower()=="tata":
            self.price_details -=12000.0
        print(f"congratulation on the purchase of brand new {self.make}'s {self.colour_coat} car.")
        print(f"please pay {self.price_details}")

    def service(self):
        if self.km < 500:
            print("no need to service now, u can wait for some more km")
        if self.km > 2000:
            print("second free service needed, engine quality is good")
        if self.km > 6000:
            print("you are exhausted with free services, this would be free service, do you wish to proceed ?")

    def resell_value(self):
        pass
#Object(instances)
nexon = Car(make="Tata", colour="Black", price=90000.0, engine="petrol", model="2020", seat=8)  #can pass keyword args.
i20 = Car("Hundayi", "Grey", "2014", 75000.0, "petrol", 7)  #(positional and default arguments(seat = 7))
nexon_d = Car(make="TATA", colour="Blue", price=95000.0, engine="diesel", model="2020")
altroz = Car("Tata", colour="Black-yellow", price=70000.0, engine="petrol", model="2020")

### way of call
nexon.sell()
i20.sell()
nexon_d.sell()
altroz.sell()
print(nexon.airbag)
print(i20.airbag)


print(i20.price)
print(i20.colour)
print(i20.make)
print()
print(nexon.price)
print(nexon.colour)
print(nexon.make)



neta_chi_Fortuner = Car("Toyota", "White")
hero_chi_Fortuner = Car("Toyota", "Black")

print(nexon.make)
print(neta_chi_Fortuner.colour)
print(hero_chi_Fortuner.make)