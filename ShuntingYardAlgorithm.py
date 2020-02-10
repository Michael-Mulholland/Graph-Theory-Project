# Michael Mulholland - G00362383
# 3rd Year Graph Theory
# The Shunting Yard Algorithm for regular expressions
# Turn infix strings into postfix strings versions

# HAVE SOME WAY ON THE COMMAND LINE THAT THE USER CAN ENTER REGULAR EXPRESSIONS TO TEST
# THE REGULAR EXPRESSION SHOULD NOT BE HARD CODED!!!!!!

# The input - should not be hard coded
# a or b followed by any number of c's
infix = "(a|b).c*"
print("Input is: ", infix)

#  Expected output: "ab|c*."
print("Expected output: ", "ab|c*.")

# Input
# Convert infix to a stack list and then Reverses the list
# [::-1] - [start : length : reverse]
infix = list(infix)[::-1]

# Operator stack
opers = []

# Output list
postfix = []

# Operator precedence - leave gaps of 20 incase I want to add more later on
# Add in the + operator later with value of 100(comparable) or 90
precendence = {'*':100, '.':80, '|':60, ')':40, '(':20}

# Loop through the input one character at a time
# Can use the python walrus operator instead of a while loop
while infix:
    # Pop a character from the input
    c = infix.pop()

    # Decide on what to do based on the character
    if c == '(':
        # Push an open bracket to the opers stack
        opers.append(c)
    elif c == ')':
        # while opers stack in reverse is not an open bracket
        # If the list is empty, you will get and error for opers[-1]
        while opers[-1] != '(':
            # Pop the operators stack until an open bracket is found
            postfix.append(opers.pop())
        # Get rid of open bracket '('
        opers.pop()
    elif c in precendence:
        # Push any operators on the opers stack with higher precendence to the output
        while opers and precendence[c] < precendence[opers[-1]]:
            # take whatever is on top of the opers stack and push it to the output
            postfix.append(opers.push())
        # Push c to the operator stack
        opers.append(c)
    else:
        # Push the character to the output
        postfix.append(c)

# Pop all operators to the output
while opers:
    postfix.append(opers.pop())

# Convert output list to string
# takes a list as its only arguement and it will join the elements of postfix and convert them to stings (which they are in this case)
# and join them to the string up front ('') - inserts an empty string between each string in postfix
postfix = ''.join(postfix)

# Print result
print("Output is: ", postfix)
















