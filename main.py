class Vehicle:
    def __init__(self,seating_capacity):
        self.seating_capacity=seating_capacity
    def fare(self):
        return self.seating_capacity*100
class Bus(Vehicle):
    def fare(self):
        totalf=super().fare()
        mcharge=0.1*totalf
        return totalf+mcharge
bus=Bus(50)
print(bus.fare())