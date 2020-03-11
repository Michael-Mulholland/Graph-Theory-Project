# G00362383 - Michael Mulholland
# Classes used in Thomspon's construction

class State:
    # Every State has a 0, 1, or 2 edges from it
    edges = []

    # Label for the arrows. None means epsilon(e)
    # None is the same as Null
    label = None

    # Constructor for the class
    # self is the same as the keyword 'this' in java
    def __init__(self, label=None, edges=[]):
        self.edges = edges
        self.label = label

# NFA Fragment
# Fragment - an NFA in its own right
class Fragment:
    # Start state of NFA fragment
    start = None

    # Accept state of NFA fragment
    accept = None

    # Constructor
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept

def shunt(infix):
    # Convert input to a stack list
    infix = list(infix)[::-1]

    # Operator Stack
    opers = []

    # Output List
    postfix = []

    # Operator Precedence
    prec = {'*':100, '.':80, '|':60, ')':40, '(':20}

    # Loop through the input one character at a time
    while infix:
        # Pop a character from the input
        c = infix.pop()

        # Decide what to do based on the character
        if c == '(':
            # Push the open bracket to the opers stack
            opers.append(c)

        elif c == ')':
            # Pop the operators stack until you find an (
            while opers[-1] != '(':
                postfix.append(opers.pop())
            # Get rid of the (
            opers.pop()

        elif c in prec:
            # Push any operators on the opers stack with higher prec to the output
            while opers and prec[c] < prec[opers[-1]]:
                postfix.append(opers.pop())
            # Push c to the operator stack
            opers.append(c)

        else:
            # Puch the character to the output
            postfix.append(c)

    # Pop all operators to the output
    while opers:
        postfix.append(opers.pop())

    # Convert output list to string
    return ''.join(postfix)

# Takes a regular expression and changes it to a Postfix expression
def compile(infix):
    postfix = shunt(infix)

    # Reverse postfix
    postfix = list(postfix)[::-1]

    nfa_stack = []

    # Loop through postfix while it's not empty
    while postfix:
        # Pop a character from postfix
        c = postfix.pop()

        if c == '.':
            # Pop two fragments off the stack
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()

            # Point frag2's accept state at frag1's start state
            frag2.accept.edges.append(frag1.start)

            # Create a new instance of Frag to represent the new NFA
            # newfrag - joins two NFA's into one NFA
            newfrag = Fragment(frag2.start, frag1.accept)

        elif c == '|':
            # Pop twp fragments of the stack
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()

            # Create a new start and accept state 
            accept = State()
            start = State(edges=[frag2.start, frag1.start])

            # Point the old accept states at the new accept state
            frag2.accept.edges.append(accept)
            frag1.accept.edges.append(accept)

            # Create a new instance of Fragment to represent the new NFA
            newfrag = Fragment(start, accept)

        elif c == '*':
            # Pop a single fragment off the stack
            frag = nfa_stack.pop()

            # Create a new start and accept states
            accept = State()
            start = State(edges=[frag.start, accept])

            # Point the arrows
            frag.accept.edges = [frag.start, accept]

            # Create new instance of Fragment to represent the new NFA
            newfrag = Fragment(start, accept)

        else:
            # New instance of the State class
            accept = State()

            # initial fragment for a single(normal) character read from the postfix regular expression
            start = State(label=c, edges=[accept])

            # Create new instance of Fragment to represent the new NFA
            newfrag = Fragment(start, accept)

        # Push the new NFA to the NFA stack
        nfa_stack.append(newfrag)

    # The NFA stack should have exactly one NFA on it
    return nfa_stack.pop()

# Add a state to a set, and follow all of the e arrows
def followes(state, current):
    # Only do something when we haven't already seen the state
    if state not in current:
        # Put the state itself into current
        current.add(state)
        # See whether state is labelled by e(psilon)
        if state.label is None:
            # Loop through the states pointed to by this state
            for x in state.edges:
                #Follow all of their e(psilon)s too
                followes(x, current)

def match(regex, s):
    # This function will return TRUE if the regular expression
    # regex (fully - not doing a partial match yet) matches the string s.
    # It returns FALSE otherwise

    # Complie the regular expression into an NFA
    nfa = compile(regex)

    # Try to Match the regular expression to the string s
    # Reference to the set data structure
        # https://docs.python.org/3.8/library/stdtypes.html#set-types-set-frozenset
        # https://realpython.com/python-sets/

    # The current set of states
    current = set()

    # Add the first state and follow all e(psilon) arrows.
    followes(nfa.start, current) # Passed by reference

    # Loop through characters in s
    for c in s:
        # Pointers - previous is pointing to current and then current to pointing to something new(a new empty set)
        # Keep track of where we were
        previous = current
        # Create a new empty set for states we're about to be in
        current = set()

        # Loop throught the previous states
        for state in previous:
            # Only follow arrows not labelled by e(psilon)
            if state.label is not None:
                # If the label of the state is equal to the character we've read:
                if state.label == c:
                    # Add the state at the end of the arrow to current
                    followes(state.edges[0], current)

    # Does the NFA match the string s
    # return nfa.match(s)

    # Ask the NFA if it matches the string s
    # If nfa accept state is in the current set of  states, then we accept, otherwise we don't
    # returns TRUE or FAlSE
    return nfa.accept in current

# when imported - it won't do the below
# It will if regex.py gets run as a script
# checks if the script has been run as a script by itself
if __name__ == "__main__":
    print(match("a.d|b*", "bbbbbbbbbbb"))

# prints out the name of the python file
print(__name__)


















