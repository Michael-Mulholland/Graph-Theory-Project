# G00362383 - Michael Mulholland

# Ian, here's at great website that you might be interested in.
# Convert simple regular expressions to nondeterministic finite automaton.
# https://cyberzhg.github.io/toolbox/regex2nfa?regex=YSti

# import the match method from the regex.py file
from regex import match

# import unittest - it is a unit testing framework
import unittest

# import the test_program.py file
import test_program

# imported for the command-line interface
import argparse

def main():

    # writing to a file
    f = open("regExpResults.txt", "a")
   
    # command line argument -h 
    # program description
    parser = argparse.ArgumentParser(
        description = "A program using the Python programming language that\
                can build a non-deterministic finite automation (NFA) from\
                a regular expression. This program will use the NFA to check\
                if the regular expression matches any given string of text."
    )

    # command line argument group.
    # allows for us to specify options that conflict with each other.
    group = parser.add_mutually_exclusive_group()
    
    # command line argument -V or --version. Displays the python version
    group.add_argument("-V", "--version", help="show program version", 
            action="store_true")
    
    # command line argument -r or --run. 
    # Brief description on how to run the program
    group.add_argument("-r", "--run", help="how to run the program", 
            action="store_true")
    
    # command line argument -v or --verbose. 
    # Displays results of pre-written tests in more detail
    group.add_argument("-v", "--verbose", help="Displays results of\
         pre-written tests in more detail", action="store_true")
    
    # command line argument -q or --quite. 
    # Displays results of pre-written tests in less detail
    group.add_argument("-q", "--quite", help="Displays results of\
         pre-written tests in less detail", action="store_true")

    # parse the args
    args = parser.parse_args()

    print()
    # displays python version
    if args.version:
        print("Python Version: 3.8.2")
        print()
        exit()
    # Brief description on how to run the program
    elif args.run:
        print("How to run the program: Select one of the following options:")
        print("\tOption 1: enter your own regular expression and String. " +
                "If the regular expression regex matches the string, " +
                "TRUE will be returned. If it does not match, FALSE will be returned.")
        print("\tOption 2: runs a number pre-written tests.")
        print("\tOption 3: is to quit the program.")
        print()
        exit()

    while True:
        # user to select one of three options
        print()
        print("Select one of the following options:")
        print("Enter 1: to test your own regular expression and String.")
        print("Enter 2: to test pre-written tests.")
        print("Enter 3: to quit the program.")
        choice = input("Please select one of the above: ")   
       
        #If yes then ask for the following input and match it
        if choice == '1':
            print()
            #  input from console - 
            #  https://pynative.com/python-input-function-get-user-input/
            # get the regular expresson from user input
            regex = input("Enter the regular expression: ")

            # get the String from user input
            s = input("Enter string: ")
            print()

            if args.verbose:
                # The match() function will return TRUE 
                # if the regular expression regex matches the string.
                # It returns FALSE otherwise
                print("The regular expression is: " + regex, 
                    " the String is: " + s, " Match: ", match(regex, s))
            elif args.quite:
                print(regex, " " + s, " ", match(regex, s))
            else: 
                print("Regex: " + regex, " String: " + s, 
                    " Match: ", match(regex, s))

            strRegex = "Regex: "
            inputRegex = regex
            strString = " String: "
            inputString = s
            strMatch = " Match: "
            boolResult = match(regex, s)
            newLine = "\n"

            # concat all the variable to allow writing to file
            strConcat = strRegex + inputRegex + strString + inputString\
                    + strMatch + str(boolResult) + newLine

            # write the users input to a file
            f.write(strConcat)
           
        elif choice == '2':
            # Print out of the tests and expected result
            # just so the user can see something
            
            # Array of regular expressions
            regex = ["b.c", "a.b|b*", "a|c.b*", "c*.b", "a+b", "a+b.c", "b?"]
            # Array of strings 
            stringsArr = ["bcccc", "bbb", "abc", "bc", "ccccccb", 
                 "abccd", "a", ""]
            
            if args.verbose:
                # Nested for loop to compare each index of the regex array with 
                # every index of the strings array to see if they match
                for reg in regex:
                    print()
                    for s in stringsArr:
                        print("The regular expression is: " + reg, 
                            " the String is: " + s, " Match: ", match(reg, s))

            elif args.quite:
                # Nested for loop to compare each index of the regex array with 
                # every index of the strings array to see if they match
                for reg in regex:
                    print()
                    for s in stringsArr:
                        print("Regex: " + reg, " String: " + s, 
                            " Match: ", match(reg, s))

            else: 
                print()
                # The above tests will allow the user to see the tests and
                # expected result. The below test will only return OK if all 
                # tests pass or FAILED if one test fails
                # The below runs unittest from the test_progam.py
                # https://stackoverflow.com/questions/31559473/run-unittests-from-a-different-file
                print("unittest from the test_program.py file")
                print()
                suite = unittest.TestLoader().loadTestsFromModule(test_program)
                unittest.TextTestRunner(verbosity=2).run(suite)    

        else:
            print()
            # quiting the program
            print("The program has now finished.")
            exit()

    f.close()
main()
