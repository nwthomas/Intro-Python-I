"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
with open("foo.txt") as f:
    for line in f:
        print(line, end="")

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open("bar.txt", "w") as b:
    b.write("The ships hung in the sky in much the same way that bricks don't.\n")
    b.write("Don't Panic.\n")
    b.write("If there's anything more important than my ego around, I want it caught and shot now.\n")
    b.close()

with open("bar.txt") as t:
    for line in t:
        print(line, end="")
