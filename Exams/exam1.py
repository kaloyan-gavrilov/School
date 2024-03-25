from abc import ABC, abstractmethod
import datetime


class Vehcle(ABC):
    def __init__(self, brand, model, max_velocity, name):
        self.__brand = brand
        self.__model = model
        self.__max_velocity = max_velocity
        self.__name = name

    @property
    def max_velocity(self):
        return self.__max_velocity

    @max_velocity.setter
    def max_velocity(self):
        return self.__max_velocity

    @property
    def name(self):
        return self.__name

    # @abstractmethod
    def print_info(self):
        print(f"Brand: {self.__brand}, Model: {self.__model}")

    # @abstractmethod
    def drive_sofia_burgas(self):
        return 360 / self.__max_velocity

    def __str__(self):
        return self.__brand + " " + self.__model


class Car(Vehcle):
    def change_oil(self, current_km):
        if current_km % 10000 > 9000:
            print("Change oil")
        elif current_km % 10000 < 9000:
            print("You don't need to change oil soon")


class Karuca(Vehcle):
    space_for_metal = 10
    current_metal = 0

    def get_the_horse_going(self):
        print("Horse is going Brrrr...")
        self.__max_velocity += 10
        print(f"The horse is currently going at {self.__max_velocity} km/h.")

    #ne rabotqt
    # def add_metal_to_karuca(self, metal_spaces):
    #     if Karuca.space_for_metal - metal_spaces > 0:
    #         Karuca.current_metal += metal_spaces
    #         self.max_velocity = self.max_velocity - metal_spaces * 2
    #         print(f"You can put the metal in the karuca, but you have slowed down by {metal_spaces * 2} km/h")
    #     else:
    #         print("You don't have enough space")
    #
    # def raztovari_metal(self, metal_spaces):
    #     if Karuca.current_metal - metal_spaces < 0:
    #         Karuca.current_metal -= metal_spaces
    #         self.max_velocity = self.max_velocity + metal_spaces * 2
    #         print(f"You have raztovaril {metal_spaces}")
    #         print(f"You are now faster with {metal_spaces * 2} km/h")
    #     else:
    #         print("There isn't enough metal to remove")


class Motorcycle(Vehcle):
    def get_boost(self):
        self.__max_velocity += 50
        print(f"Motorcycle is on fire, going at {self.__max_velocity} km/h.")


class AutoPark():
    current_spaces = 0
    vehicles_inside = []

    def __init__(self, number_of_spaces, opening_time, closing_time):
        self.__number_of_spaces = number_of_spaces
        self.__opening_time = opening_time
        self.__closing_time = closing_time

    def park_new_vehicle(self, vehicle):
        current_time = datetime.datetime.now().hour
        if AutoPark.current_spaces < self.__number_of_spaces and not (
                current_time > self.__closing_time or current_time < self.__opening_time):
            AutoPark.current_spaces += 1
            AutoPark.vehicles_inside.append(vehicle)
            print(f"The auto_park now has {self.__number_of_spaces - AutoPark.current_spaces} left")
        else:
            print("The auto_park is either closed or full!")

    def remove_vehicle(self, vehicle):
        in_parking = False
        for current_vehicle in AutoPark.vehicles_inside:
            if current_vehicle.name == vehicle:
                AutoPark.vehicles_inside.remove(current_vehicle)
                print(f"{current_vehicle} has been removed")
                AutoPark.current_spaces -= 1
                print(f"The auto_park now has {self.__number_of_spaces - AutoPark.current_spaces} left")
                in_parking = True

        if not in_parking:
            print("The vehicle isn't in the park")

    def fastest_car(self):
        max_speed = 0
        for car in AutoPark.vehicles_inside:
            if car.max_speed > max_speed:
                max_speed = car.max_speed
        return max_speed

    def fastest_karuca(self):
        max_speed = 0
        for karuca in AutoPark.vehicles_inside:
            if isinstance(karuca, Karuca):
                if karuca.max_velocity > max_speed:
                    max_speed = karuca.max_velocity

        return max_speed

    def print_vehicles(self):
        print("\n -----------\n")
        for vehicle in AutoPark.vehicles_inside:
            print(vehicle, end=", ")
        print("\n\n -----------\n")


park1 = AutoPark(number_of_spaces=10, opening_time=8, closing_time=20)
park1.park_new_vehicle(Karuca(brand="karuca", model="na pesho", max_velocity=10, name="karuca1"))
park1.park_new_vehicle(Car(brand="BMW", model="M3", max_velocity=200, name="gogo"))
park1.park_new_vehicle(Car(brand="Mazda", model="Mx-5", max_velocity=80, name="Vroom"))
park1.park_new_vehicle(Karuca(brand="karuca", model="na joro", max_velocity=30, name="karuca2"))
park1.park_new_vehicle(Motorcycle(brand="Kawasaki", model="Ninja125", max_velocity=120, name="motorcycle1"))

park1.print_vehicles()

park1.remove_vehicle("gogo")
park1.print_vehicles()

karucata_na_joro = Karuca(brand="karuca", model="na joro", max_velocity=30, name="karuca2")
# karucata_na_joro.add_metal_to_karuca(2)
# karucata_na_joro.add_metal_to_karuca(1)
# karucata_na_joro.raztovari_metal(1)
karucata_na_joro.drive_sofia_burgas()

car1 = Car(brand="BMW", model="M3", max_velocity=200, name="gogo")
car1.change_oil(24000)

