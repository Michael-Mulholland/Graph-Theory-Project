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
class Frag:
    # Start state of NFA fragment
    start = None

    # Accept state of NFA fragment
    accept = None

    # Constructor
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept

# calling the class Constructor - label set to 'a' and edges[] is set to default
myinstance = State(label='a', edges = [])

# calling the class Constructor - label set to default and edges[] is set to a class containing myinstance
myotherinstance = State(edges=[myinstance])
myfrag = Frag(myinstance, myotherinstance)

print(myinstance.label)
print(myotherinstance.edges[0])
print(myfrag)
