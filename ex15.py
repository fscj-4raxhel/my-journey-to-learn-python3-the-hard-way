# Imports the features in the argv module
from sys import argv

# Unpacks the command line arguments
script, filename = argv

# Use the open built-in function to return a file object
txt = open(filename)

# print the format string
print(f"Here is your file {filename}")
# reads the contenct of the file, assuming it's less than twice the system's memory and print it.
print(txt.read())

# Print a line for the user
print("Type the filename again:")
# Store the user input and in a variable named file_again
file_again = input("> ")

# Read the file agian and read its content into a variable named txt_again
txt_again = open(file_again)

# print the string txt_again
print(txt_again.read())

# close the resources
txt.close()
txt_again.close()