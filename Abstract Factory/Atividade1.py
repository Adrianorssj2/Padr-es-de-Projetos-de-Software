from abc import ABC, abstractmethod

class VehicleType(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_price(self) -> float:
        pass

class CarType(VehicleType):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price

class MotorcycleType(VehicleType):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price

class TruckType(VehicleType):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price

class VehicleTypeFactory(ABC):
    @abstractmethod
    def create_car_type(self) -> VehicleType:
        pass
   
    @abstractmethod
    def create_motorcycle_type(self) -> VehicleType:
        pass
   
    @abstractmethod
    def create_truck_type(self) -> VehicleType:
        pass

class ElectricVehicleTypeFactory(VehicleTypeFactory):
    def create_car_type(self) -> VehicleType:
        return CarType("Tesla Model 3", 50000)

    def create_motorcycle_type(self) -> VehicleType:
        return MotorcycleType("Zero SR/F", 20000)

    def create_truck_type(self) -> VehicleType:
        return TruckType("Rivian R1T", 70000)

class FuelVehicleTypeFactory(VehicleTypeFactory):
    def create_car_type(self) -> VehicleType:
        return CarType("Toyota Corolla", 20000)

    def create_motorcycle_type(self) -> VehicleType:
        return MotorcycleType("Honda CB 500F", 6000)

    def create_truck_type(self) -> VehicleType:
        return TruckType("Ford F-150", 30000)

class Vehicle:
    def __init__(self, vehicle_type: VehicleType):
        self.vehicle_type = vehicle_type

    def manufacture(self):
        print(f"Fabricando um {self.vehicle_type.get_name()}com um custo de {self.vehicle_type.get_price()} reais.")

def main():
    electric_factory = ElectricVehicleTypeFactory()
    fuel_factory = FuelVehicleTypeFactory()

    car1 = Vehicle(electric_factory.create_car_type())
    motorcycle1 = Vehicle(electric_factory.create_motorcycle_type())
    truck1 = Vehicle(electric_factory.create_truck_type())

    car2 = Vehicle(fuel_factory.create_car_type())
    motorcycle2 = Vehicle(fuel_factory.create_motorcycle_type())
    truck2 = Vehicle(fuel_factory.create_truck_type())

    car1.manufacture()
    motorcycle1.manufacture()
    truck1.manufacture()

    car2.manufacture()
    motorcycle2.manufacture()
    truck2.manufacture()

if __name__ == "__main__":
    main()
