# This is the function, named cheese_and_crackers, and taking the arguments
# cheese_count and boxes_of_crackers. Nothing happens, though, until the
# function is called.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # The arguments take whatever value is assigned to them when the function
    # is called.
    print "You have %d cheeses!" % cheese_count
    print "Your have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

print "We can just give the function numbers directly:"
# cheese_and_crackers is called. cheese_count is given the value 20 and
# boxes_of_crackers is given the value 30.
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
# A variable with the value 10.
amount_of_cheese = 10
# A variable with the value 50.
amount_of_crackers = 50

# The function cheese_and_crackers is called and given the variables
# amount_of_cheese and amount_of_crackers (10 and 50, respectively)
# as the arguments.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
# cheese_and_crackers is called and the argmuents are mathematical expressions.
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# Input from user, converting the input to a number with int().
a = int(raw_input("cheese?: "))
b = int(raw_input("boxes?: "))
# Passing in the variables a and b as the arguments to cheese_and_crackers.
cheese_and_crackers(a, b)
