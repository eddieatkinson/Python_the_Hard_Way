from sys import argv

script, input_file = argv
# This funcrion prints the whole file when called.
def print_all(f):
    print f.read()
# This function brings us back to the beginning when called.
def rewind(f):
    f.seek(0)
# This function prints one line of the file at a time when called.
def print_a_line(line_count, f):
    print line_count, f.readline(),
# We're setting the variable current_file to be the opened file we put in.
current_file = open(input_file)

print "First let's print the whole file:\n"
# This is our first function, passing the argument as the opened input file.
print_all(current_file)

print "Now let's rewind, kind of like a tape."
# Now that we've printed the file, we need to return to the beginning of it.
rewind(current_file)

print "Let's print three lines:"
# Now we're printing each line individually.
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
