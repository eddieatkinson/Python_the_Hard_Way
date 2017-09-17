x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

#Displays the literal contents of x
print "I said: %r." % x

#Displays y for the user, but then wraps it with the single quotations
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?: %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
