#100 cars!
cars = 100
#Only 4 per car
space_in_a_car = 4
#Thirty people driving
drivers = 30
#Ninety people need a ride
passengers = 90
#Assuming every driver is a car
cars_not_driven = cars - drivers
#Assuming the same
cars_driven = drivers
#How many total seats are available
carpool_capacity = cars_driven * space_in_a_car
#How many passengers are in each car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
