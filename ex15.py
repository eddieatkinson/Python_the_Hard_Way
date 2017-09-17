filename = raw_input("What's the name of the file?: ")

#This will tell the user the file that is to be opened.
print "Here's your file %r:" % filename
#We are opening the file.
txt = open(filename)
#This prints the contents of the file input to the command line.
print txt.read()

#This prompts the user to give another file name (or the same one).
print "Type the filename again:"
#This assigns the variable file_again to the new (or same) file we just input.
file_again = raw_input("> ")
#This assigns the variable txt_again to the contents of the file we just named.
txt_again = open(file_again)

#This will print the contents of that file.
print txt_again.read()
