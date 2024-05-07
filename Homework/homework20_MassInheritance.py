class Vehicle:
    vehicle_type = "none"

class Car:
    price = 1000000

    def horse_powers(self):
        return 200

class Nissan(Car, Vehicle):
    price = 2000000
    vehicle_type = 'Хэтчбек'

    def horse_powers(self):
        return  150

new_car = Nissan()
print(f'Машина типа "{new_car.vehicle_type}", стоит {new_car.price}')