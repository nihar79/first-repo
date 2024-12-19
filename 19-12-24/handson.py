class Car:
    def __init__(self):
        self.color="red"
        self.max_speed=200
        self.acceleration=4
        self.tyre_friction=5
        self.is_engine_started=False
        self.current_speed=0.0 
    
    def start_engine(self):
        self.is_engine_started=True
    def stop_engine(self):
        self.is_engine_started=False
    def accelerate(self):
        self.current_speed+=self.acceleration
    def apply_brakes(self):
        self.current_speed-=self.acceleration
    def sound_horn(self):
        print("Honk")


class Truck(Car):
    max_cargo_weight=1100
    current_cargo_weight=0

    def __init__(self):
        super().__init__()
        self.current_cargo_weight=0

    def start_engine(self):
        super().start_engine()

    def stop_engine(self):
        super().stop_engine()

    def accelerate(self):
        super().accelerate()

    def apply_brakes(self):
        super().apply_brakes()

    def sound_horn(self):
        if(super().is_engine_started==True):
            print("Honk Honk")
        else:
            print("Car has not started yet")

    def load_cargo(self,cargo_weight):
        if self.is_engine_started:
            print("Cannot load cargo during motion")
        else:
            if (self.current_cargo_weight+cargo_weight)<=self.max_cargo_weight:
                self.current_cargo_weight += cargo_weight
                print("Cargo Loaded")
            else:
                print("Cannot load cargo more than max limit:",self.max_cargo_weight)
            

    def unload_cargo(self,cargo_weight):
        if self.is_engine_started:
            print("Cannot unload cargo during motion")
        else:
            if (self.current_cargo_weight-cargo_weight)>=0:
                self.current_cargo_weight -= cargo_weight
                print("Cargo Unloaded")
            else:
                print("Cannot unload cargo that is not present")
            
truck=Truck()
#truck.start_engine()
truck.load_cargo(500)
truck.start_engine()
truck.unload_cargo(89)