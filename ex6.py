# Define a variable named types_of_people with initial value 10
types_of_people = 10
# Define a variable named x with initial value being a format string that contains another variable types_of_people
x = f"There are {types_of_people} types of people."

# Define a variable named binary with intial value being a string literal "binary"
binary = "binary"
# Define a variable named do_not with intial value being a string literal "don't"
do_not = "don't"
# Define a variable named y with intial value being a format string that contains other variables binary and do_not
y = f"Those who know {binary} and those who {do_not}."

# Print string x
print(x)
# Print string y
print(y)

# Print the format string that contains the value of variable x
print(f"I said: {x}")
# Print the format string that contains the value of variable y
print(f"I also said: '{y}'")

# Define a variable named hilarious with initial value False
hilarious = False
# Define a variable named joke_evaluation with initial value being a format string.
joke_evaluation = "Isn't that joke so funny!?{}"

# Format the sthring joke_evaluation with variable hilarious and print it.
print(joke_evaluation.format(hilarious))

# Define a string literal w
w = "This is the left side of..."
# Define a string literal e
e = "a string with a right side."

# Concatenate string w and e then print the resulting string.
print(w + e)