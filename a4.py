class ferrari:
    def fuel_type(self):
        print("petrol")
    def max_speed(self):
        print("max speed 350")
class BMW:
    def fuel_type(self):
        print("diesel")
    def max_speed(self):
        print("max speed 240")
Ferrari=ferrari()
bmw=BMW()

for car in(Ferrari,bmw):
    car.fuel_type()
    car.max_speed()