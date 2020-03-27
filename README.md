# Graph Theory Project 2020
3rd Year Graph Theory Project
Michael Mulholland - G00362383

## Introduction
<p>A program using the Python programming language that can build a non-deterministic finite automation (NFA) from a regular expression. This program will use the NFA to check if the regular expression matches any given string of text.<p>
  
<p>A regular expression is a string containing a series of characters, some of which may have a special meaning. <p>

==========================================================================

## Submission Contents

runner.py
--------------------------------------------------------------------------
I have imported the match function from regex.py into the runner.py

The code is run within a while True loop. This is to allow the user to run as many tests as they like without having to restart the program every time (there is an option to quit the program).

When the program runs the user will be prompted to select one of the following options:

Enter 1: to test your own regular expression and String.
Enter 2: to run pre-written tests.
Enter 3: to quit the program.

If option one is selected, the user will be asked to enter a regular expression of their choice. Then the user will have to enter a string. 

If option two is selected, pre-written tests will automatically run. I am using two arrays. One for the regular expressions and one for the strings. I've used a nested for loop to compare each index of the regex array with every index of the strings array to see if they match

If option three is selected, the program will exit.

If the user selects option 1 or option 2, the program will then call the match function and use the NFA to check if the regular expression matches any given string of text. If it does match, True will be returned. If it doesn't match, False will be returned.

==========================================================================

regex.py
--------------------------------------------------------------------------

Class State
A state with one or two edges, all edges labeled by label.
The State class contains a constructor that creates two variables, edges and labels. Every State has 0, 1, or 2 edges from it and a label for the arrows (None).

Class Fragment
An NFA fragment with a start state and an accept state.
The Fragment class contains a constructor that creates a start state of the NFA fragmant and the accept state of the NFA fragmant.

Shunt Function
The Shunt function reads in a string(infix regular expression) and return the infix regular expression in postfix. It loops through the input one character at a time and decides what to do based on the character.

if c == '(':
	Pushes the opening bracket to the stack
elif c == ')':
	Within the elif, the while loop checks to see if the last character on the list is not an opening bracket. 
	If it's not an opening bracket, pop all the characters from the opers stack and add them to the postfix.
	The open bracket is then popped and removed.
elif c in prec:
	Within the elif, the while loop checks to see which operator has higher precedence.
	The precedence of the operator decides if it'll be positioned before or after the symbol on the opers stack.
else
	The else pushes all other characters that aren't an operator, opening or closing bracket to the postfix.

After the if/elif statement, a while loop, loops through the opers stack and pops all operators to the ouput.

The shunt function then returns the converted output list to string

====

Complie Function
It takes the posfix regular expression created in the Shunt Function and turns it into an NFA.

The posfix regular expression is reversed and looped through.

A character will be popped from the postfix,

if the character is a '.':
	Two fragments are popped off the stack. (frag1 and frag2)
	Point frag2's accept state at frag1's start state
	The new start state is frag2's start state
	The new accept state is frag1's accept state

if the character is a '|':
        Pop two fragments of the stack. (frag1 and frag2)
	Creates a new start and accept state - the new start state is connected to both frag1 and frag2's start state
	Point frag1's and frag2's old accept states at the new accept state

if the character is a '*':
	Zero or More
        Pop a single fragment off the stack. (frag)
	Create a new start and accept states - but point the start state to to the old start state and the new accept state
	The old accept state is then connect to the old start state and the new accept state.	

if the character is a '?':
	Zero or one
        Pop a single fragment off the stack. (frag)
	Create a new start and accept state - but point the new start state to to the old start state and the new accept state
	The old accept state is then connect to the new accept state (only) - It doen't connect to the new start state at all.

if the character is a '+':
	Pop a single fragment off the stack. (frag)
	Creates a new start and accept state - the start state is connented to the old frag's start state
	The old accept state is then connect to the old start state and the new accept state.

The else statement is for all characters that are not special. A new accept and start state is created and nothing is popped off the stack.
The label is set to the character that is been read and the edges is connented to the new accept state.

A new instance of Frag is created to represent the new NFA and joins two NFA's into one NFA.
It then returns exactly one NFA

====

Followes Function
It's a recursive function that adds a state to a set, and follow all of the e(psilon) arrows but only if we haven't already seen the state.

Match Function



TALK ABOUT VIM - RESEARCH





	



















==========================================================================

## Research

I have alot of 

<b>Python:</b>
* [python.org](https://www.python.org/)
* [Tutorial](https://www.youtube.com/watch?v=rfscVS0vtbw)
* [Documentation](https://docs.python.org/3.8/index.html)

<b>Thompson's construction:</b>
* [Wikipedia](https://en.wikipedia.org/wiki/Thompson's_construction)
* [Regular Expression to NFA](https://www.youtube.com/watch?v=RYNN-tb9WxI)

<b>Regular Expression:</b>
* [Convert regular expressions to NFA's](https://cyberzhg.github.io/toolbox/regex2nfa?regex=YSti)
* [Regular Expressions - Computerphile](https://www.youtube.com/watch?v=528Jc3q86F8)
* [Regular Expression Syntax](https://docs.python.org/2/library/re.html#regular-expression-syntax)
* [Regular Expression Help](https://swtch.com/~rsc/regexp/regexp1.html)
* [Regexper](https://regexper.com/#)

<b>Data Structues</b>
* [python.org - Sets](https://docs.python.org/3.8/library/stdtypes.html#set-types-set-frozenset)
* [Real Python - Sets](https://realpython.com/python-sets/)
  
<b>Guidelines</b>
* [PEPs](https://www.python.org/dev/peps/)
***

<br>
