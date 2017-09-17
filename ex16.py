#Import the module argv
from sys import argv

#To run in the command line, give the script (ex16.py) and the filename.
script, filename = argv

print "We're going to erase %r." % filename
#CTRL-C gets out of the program.
print "If you don't want that, hit CTRL-C (^C)."
#RETURN continues.
print "If you don't want that, hit RETURN."

#This is where we'll choose to stop or go on.
raw_input("?")

print "Opening the file..."
#We're opening the filename we put in the command line. 'W' specifies we're
#writing in the file, and it also erases anything that's already there.
#'w' also lets us create a new file with the name that we entered for filename.
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
#We're erasing the file! But we already erased it with the 'w' argument above
#so we're going to 'comment' it out.
#target.truncate()

print "Now I'm going to ask you for three lines."
#These are the three lines we will be writing in to the now empty file.
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
#The lines that we input above are being written in to the file.
target.write("%s\n%s\n%s" % (line1, line2, line3))

print "And finally, we close it."
#We're closing the file.
target.close()
