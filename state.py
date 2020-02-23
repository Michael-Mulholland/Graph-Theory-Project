# Michael Mulholland
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
def regex_compile(infix):
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

def match(regex, s):
    # This function will return TRUE if the regular expression
    # regex (fully - not doing a partial match yet) matches the string s.
    # It returns FALSE otherwise

    # Complie the regular expression into an NFA
    nfa = regex_compile(regex)

    # Does the NFA match the string s
    # return nfa.match(s)

    # Ask the NFA if it matches the string s
    return nfa

print(match("a.d|b*", "bbbbbbbbbbb"))
