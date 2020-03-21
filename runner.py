# G00362383 - Michael Mulholland

# Ian, here's at great website that you might be interested in.
# Convert simple regular expressions to nondeterministic finite automaton.
# https://cyberzhg.github.io/toolbox/regex2nfa?regex=YSti

import sys

# import the match method from the regex.py file
from regex import match

def main():
    while True:
        #  input from console - 
        #  https://pynative.com/python-input-function-get-user-input/

        # get the regular expresson from user input
        regex = input("Enter the regular expression: ")

        # get the String from user input
        s = input("Enter string: ")

        # Returns true if all characters in the string are alphabetic 
        # and there is at least one character, false otherwise.
        # https://docs.python.org/2/library/stdtypes.html#str.isalpha
        # I permalinked the method in the above URL. If you scroll down
        # around one quarter of the page, you will see the method in yellow
        if s.isalpha():
            # The match() function will return TRUE if the regular expression
            # regex matches the string.
            # It returns FALSE otherwise
            print(match(regex, s), regex, s)
        else:
            print('Please enter a string')
    
main()