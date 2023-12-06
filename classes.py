class Vehice:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    def moves(self):
        print(f"Moves along...")
        
    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}")
        
my_car = Vehice("Tesla", "Model 3")


print(my_car.make)
print(my_car.model)
my_car.moves()
my_car.get_make_model()


your_car = Vehice("Mescerdes", "Top 1")
your_car.get_make_model()


class Airplane(Vehice):
    def __init__(self, make, model ,id):
        super().__init__(make,model)
        self.id = id
        
    def moves(self):
        print(f"Flies along... {self.id}")
        
class Truck(Vehice):
    def moves(self):
        print("Run along...")


class CatRun(Vehice):
    pass

Ebus = Airplane("Ebus", "Model 1", "19287623")
Mescerdes = Truck("Mescerdes", "Model 2")
catrun = CatRun("YellowCatRun", "Model 3")


Ebus.get_make_model()
Ebus.moves()
Mescerdes.get_make_model()
Mescerdes.moves()
catrun.get_make_model()
catrun.moves()


print('\n\n')


for v in (my_car, your_car, Ebus, Mescerdes, catrun):
    v.get_make_model()
    v.moves()