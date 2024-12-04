# Theme Park Task
class Attraction:
    def __init__(self,name,capacity):
        self._name = name
        self._capacity = capacity
    def get_details(self):
        details = {"Attraction": self._name,
        "Capacity": self._capacity}
        return details
    def start(self):
        print("The attraction is starting")
class ThrillRide(Attraction):
    def __init__(self,name,capacity,min_height):
        super().__init__(name,capacity)
        self._min_height = min_height
    def start(self):
        print(f"Thrill ride,{self._name}, is now starting")
    def is_eligible(self,visitor):
        if visitor._height >= self._min_height:
            return True
        else:
            return False
class FamilyRide(Attraction):
    def __init__(self,name,capacity,min_age):
        super().__init__(name,capacity)
        self._min_age = min_age
    def start(self):
        print(f"Family ride, {self._name}, is now starting")
    def is_eligible(self,visitor):
        if visitor._age >= self._min_age:
            return True
        else:
            return False

class Staff:
    def __init__(self,name,role):
        self._name = name
        self._role = role
    def work(self):
        print(f"{self._name} is working their job of {self._role}")
class Visitor:
    def __init__(self,name,age,height):
        self._name = name
        self._age = age
        self._height = height
    def ride_attraction(self,attraction):
        if attraction.is_eligible(self):
            attraction.start()
        else:
            print("Sorry, you can't do that")

thrill = ThrillRide("Scooby Doo Ride",10,140)
family = FamilyRide("Spiderman Ride",20,6)
visitor1 = Visitor("Nikhil",16,160)
visitor1.ride_attraction(family)
visitor1.ride_attraction(thrill)
staff1 = Staff("Archie","cleaning the toilet")
staff1.work()
# DONE!!