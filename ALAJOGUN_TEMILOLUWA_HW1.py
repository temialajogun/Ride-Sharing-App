import math

class Location:         #Class representing location
    def __init__(self, x, y):      #Assigns the given parameters to the corresponding data attributes
        self.x = x
        self.y = y

    def __str__(self):        #Returns a string representation of the location of the object
        return f'({self.x},{self.y})'
    
class Car:                  #Class representing Car
    def __init__(self, car_name, location, cost_per_mile):      #Constructor of the class Car
        self.car_name = car_name
        self.location = location
        self.cost_per_mile = cost_per_mile

    def __str__(self):               #Returns a string representation of the car object
        return f'[{self.car_name}, {self.location}, {self.cost_per_mile}]'
    
    def move_to(self, new_x, new_y):        #Updates the x and y coordinates of the location attribute
        self.location.x = new_x
        self.location.y = new_y

class Passenger:                 #Class representing passenger
    def __init__(self, passenger_name, location):          #Constructor of the class Passenger
        self.passenger_name = passenger_name
        self.location = location

    def __str__(self):            #Returns a string representation of a passenger object
        return f'[{self.passenger_name}, {self.location}]'
    
    def move_to(self, new_x, new_y):             #Updates the x and y coordinates of the location attribute
        self.location.x = new_x
        self.location.y = new_y

class RideSharingApp:               #Class representing Ride Sharing App
    def __init__(self):
        #Set the cars and passengers attributes to empty lists
        self.cars = []
        self.passengers = []
    
    def add_car(self,car):       
        #Adds the given car object to the cars attribute
        self.cars.append(car)

    def add_passenger(self, passenger):
        #Adds the given passenger object to the passengers attribute
        self.passengers.append(passenger)

    def remove_car(self, car):
        #Removes the given car object from the cars attribute
        if car in self.cars:
            self.cars.remove(car)

    def remove_passenger(self, passenger):
        #Removes the given passenger objects from the passengers attribute
        if passenger in self.passengers:
            self.passengers.remove(passenger)

    def find_cheapest_car(self):
        #Finds the car with the lowest cost per mile and prints the string represntation of that car
        if not self.cars:
            print('Cars not available.')      #Prints when there are no cars available
            return
        cheapest_car = min(self.cars, key=lambda car: car.cost_per_mile)
        print(f'Cheapest Car Available: {cheapest_car.car_name}, Cost per mile: {cheapest_car.cost_per_mile}')

    def find_nearest_car(self, passenger):    
        #Finds the nearest car for the given passenger and print the string representation for that car
        if not self.cars:
            print('Cars not avaialable')   #Print when there are no cars available
            return
        nearest_car = min(self.cars, key=lambda car: self.distance(car.location, passenger.location))
        nearest_distance = self.distance(nearest_car.location, passenger.location)
        print(f'Nearest car for {passenger.passenger_name}: {nearest_car.car_name}, Distance: {nearest_distance:.2f}')

    def distance(self, location1, location2):
        #Calculate distance between two locations
        return math.sqrt((location2.x - location1.x) ** 2 + (location2.x - location1.y) ** 2)
    
print('---------------------Object Creation------------------')
location1 = Location(2,1)
location2 = Location(-4,1)
car1 = Car('car1', location1, 0.61)
car2 = Car('car2', location2, 0.50)
print('Car object 1 created:',car1)
print('Car object 2 created:', car2)

location3 = Location(-2,3)
location4 = Location(0,0)
passenger1 = Passenger('passenger1', location3)
passenger2 = Passenger('passenger2', location4)
print('Passenger object 1 created:', passenger1)
print('Passenger object 2 created:', passenger2)

mobileApp = RideSharingApp()
mobileApp.add_car(car1)
mobileApp.add_car(car2)
mobileApp.add_passenger(passenger1)
mobileApp.add_passenger(passenger2)

print('-----------------------Scenario 1---------------------')
mobileApp.find_cheapest_car()
mobileApp.find_nearest_car(passenger1)
mobileApp.find_nearest_car(passenger2)

print('-----------------------Scenario 2---------------------')
car1.move_to(0,-5)
passenger1.move_to(0,3)
print('car1\'s location has been updated:',car1)
print('passenger1\'s location has been updated:', passenger1)

mobileApp.find_cheapest_car()
mobileApp.find_nearest_car(passenger1)
mobileApp.find_nearest_car(passenger2)

print('-----------------------Scenario 3---------------------')
car3 = Car('car3', Location(0,2), 0.3)
mobileApp.add_car(car3)
print('New car added:',car3)

mobileApp.find_cheapest_car()
mobileApp.find_nearest_car(passenger1)
mobileApp.find_nearest_car(passenger2)