from abc import ABC,abstractmethod
class vehicle(ABC):
    def drive(self):
        print("the vehicle is used for driving")
    

@abstractmethod
def start_engine(self):
    pass

class car(vehicle):
    def start_engine(self):
        print("car engine started")

def operate_vehicle(vehicle):
    vehicle.start_engine()

car1 = car()
operate_vehicle(car1)

