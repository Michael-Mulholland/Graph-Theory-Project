# G00362383 - Michael Mulholland

# Ian, here's at great website that you might be interested in.
# Convert simple regular expressions to nondeterministic finite automaton.
# https://cyberzhg.github.io/toolbox/regex2nfa?regex=YSti

# import the match method from the regex.py file
from regex import match

def main():
    while True:
        # user to select one of three options
        print()
        print("Select one of the following options:")
        print("Enter 1: to test your own regular expression and String.")
        print("Enter 2: to test pre-written tests.")
        print("Enter 3: to quit the program.")
        choice = input("Please select one: ")   
        
        #If yes then ask for the following input and match it
        if choice == '1':
            print()
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
            # around 1\4 of the page, you will see the method in yellow
            #if s.isalpha():
                #print()
                # The match() function will return TRUE 
                # if the regular expression regex matches the string.
                # It returns FALSE otherwise
                #print(match(regex, s), regex, s)
            print("Regex: " + regex, " String: " + s, " Match: ", match(regex, s))
            #else:
             #   print()
              #  print('A string was not entered.')
              
        elif choice == '2':
            # Array of regular expressions
            regex = ["b.c", "a.b|b*", "a|c.b*", "c*.b"]
            # Array of strings 
            stringsArr = ["bcccc", "bbb", "abc", "ccccccb", "abbc", "abbbbb", "abccd"]
            
            # Nested for loop to compare each index of the regex array with 
            # every index of the strings array to see if they match
            for reg in regex:
                print()
                for s in stringsArr:
                    print("Regex: " + reg, " String: " + s, " Match: ", match(reg, s))
                    
        else:
            print()
            # quiting the program
            print("The program has now finished.")
            exit()

main()