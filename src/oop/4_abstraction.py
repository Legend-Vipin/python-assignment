# 5. Abstraction
# Concept: Hiding complexity, showing only essential features
from abc import ABC, abstractmethod

class AbstractVehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def get_info(self):
        print("This is some type of vehicle.")

class GasolineCar(AbstractVehicle):
    def start(self):
        print("Turning key, engine ignites (Gasoline Car).")

    def stop(self):
        print("Applying brakes, engine off (Gasoline Car).")

class Bicycle(AbstractVehicle):
    def start(self):
        print("Start pedaling (Bicycle).")

    def stop(self):
        print("Apply hand brakes (Bicycle).")

car = GasolineCar()
bike = Bicycle()

def operate_vehicle(vehicle: AbstractVehicle):
    vehicle.start()
    vehicle.stop()

operate_vehicle(car)
operate_vehicle(bike)
