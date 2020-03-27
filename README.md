# Graph Theory Project 2020
<hr>
<p>3rd Year Graph Theory Project</P>
Michael Mulholland - G00362383

## Introduction
<p>A program using the Python programming language that can build a non-deterministic finite automation (NFA) from a regular expression. This program will use the NFA to check if the regular expression matches any given string of text.<p>
  
<p>A regular expression is a string containing a series of characters, some of which may have a special meaning. <p>

## Submission Contents

**runner.py**

<p>I have imported the match function from regex.py into the runner.py<p>

<p>The code is run within a while True loop. This is to allow the user to run as many tests as they like without having to restart the program every time (there is an option to quit the program).<p>

When the program runs the user will be prompted to select one of the following options:
* Enter 1: to test your own regular expression and String.
* Enter 2: to run pre-written tests.
* Enter 3: to quit the program.

<p>If option one is selected, the user will be asked to enter a regular expression of their choice. Then the user will have to enter a string. <p>

<p>If option two is selected, pre-written tests will automatically run. I am using two arrays. One for the regular expressions and one for the strings. I've used a nested for loop to compare each index of the regex array with every index of the strings array to see if they match.<p>

<p>If option three is selected, the program will exit.<p>

<p>If the user selects option 1 or option 2, the program will then call the match function and use the NFA to check if the regular expression matches any given string of text. If it does match, True will be returned. If it doesn't match, False will be returned.<p>



**regex.py**

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
	Concatenation 
	Two fragments are popped off the stack. (frag1 and frag2)
	Point frag2's accept state at frag1's start state
	The new start state is frag2's start state
	The new accept state is frag1's accept state

if the character is a '|':
	OR
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
	One or many
	Pop a single fragment off the stack. (frag)
	Creates a new start and accept state - the start state is connented to the old frag's start state
	The old accept state is then connect to the old start state and the new accept state.

The else statement is for all characters that are not special. A new accept and start state is created and nothing is popped off the stack.
The label is set to the character that is been read and the edges is connented to the new accept state.

A new instance of Frag is created to represent the new NFA and joins two NFA's into one NFA.
It then returns exactly one NFA

====

Followes Function
It's a recursive function that adds a state to a set, and follows all of the e(psilon) arrows but only if we haven't already seen the state.

Match Function
The compile function is called and it compiles the regular expression into an NFA.
The followes function is then called and adds the first state and follows all e(psilon) arrows.
The for loop, loops through the string (s). If the label is equal to the character, then add the state arrow to the current set of states.
This function will return TRUE if the regular expression regex matches the string s, otherwise it returns FALSE.

Tests
A few hard coded test to see if my program works.
If you run the runner.py file, the tests within regex.py will not be executed.
If you run the regex.py file, the tests will be excuted.
The for loop, loops through all teh tests and out puts any errors.

VIM
Vim is a highly configurable text editor for efficiently creating and changing any kind of text. It is included as "vi" with most UNIX systems and with Apple OS X.

Vim is rock stable and is continuously being developed to become even better. Among its features are:
	persistent, multi-level undo tree
	extensive plugin system
	support for hundreds of programming languages and file formats
	powerful search and replace
	integrates with many tools

Insert, quiting, saving and copying (with some research) are easy enough but sometimes I struggled with vim. I was creating files that I didn't want to create and I don't know how I was creating them. After some research I found out that I was creating swap files. I just deleted them everytime I made one by accident until I found out that they can actually be useful. 
They store changes you've made to the buffer. If Vim or your computer crashes, they allow you to recover those changes. They also provide a way to avoid multiple instances of Vim from editing the same file. This can be useful on multi-user systems or just to know if you have another Vim already editing a file.

Now, after using vim for this project I find that I am capable of using vim without any problems and it's good to have in the locker.

==========================================================================

## Research

I have alot of research. Maybe too much but I just wanted to list everything that I found useful when trying to complete this project.

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

<b>VIM</b>
[Vim Wiki](https://en.wikipedia.org/wiki/Vim_(text_editor))
[Vim 101: A Beginners Guide](https://www.linux.com/training-tutorials/vim-101-beginners-guide-vim/)
[Swap Files on StackExchange](https://vi.stackexchange.com/questions/177/what-is-the-purpose-of-swap-files)
***

<br>
