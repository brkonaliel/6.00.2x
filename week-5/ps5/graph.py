# 6.00.2x Problem Set 5
# Graph optimization
#
# A set of data structures to represent graphs
#

class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other.name
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        # Override the default hash method
        # Think: Why would we want to do this?
        return self.name.__hash__()

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return '{0}->{1}'.format(self.src, self.dest)

class WeightedEdge(Edge):
    def __init__(self, src, dst, distance=1.0, outdoor=0.0):
        Edge.__init__(self, src, dst)
        self.distance = distance
        self.outdoor = outdoor
    def getTotalDistance(self):
        return self.distance
    def getOutdoorDistance(self):
        return self.outdoor
    def __str__(self):
        return '{0}->{1} ({2}, {3})'.format(self.src, self.dest, self.distance, self.outdoor)


class Digraph(object):
    """
    A directed graph
    """
    def __init__(self):
        # A Python Set is basically a list that doesn't allow duplicates.
        # Entries into a set must be hashable (where have we seen this before?)
        # Because it is backed by a hashtable, lookups are O(1) as opposed to the O(n) of a list (nifty!)
        # See http://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            # Even though self.nodes is a Set, we want to do this to make sure we
            # don't add a duplicate entry for the same node in the self.edges list.
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[str(k)]:
                res = '{0}{1}->{2}\n'.format(res, k, d)
        return res[:-1]
class WeightedDigraph(Digraph):
    """
    A weighted directed graph
    """
    def __init__(self):
        Digraph.__init__(self)

    def addEdge(self, weighted_edge):
        src = weighted_edge.getSource()
        dest = weighted_edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        weight = (float(weighted_edge.getTotalDistance()), float(weighted_edge.getOutdoorDistance()))
        self.edges[src].append([dest, weight])
        # self.edges[src].append(weight)
    def childrenOf(self, node):
        result = list()
        for n in self.edges[node]:
            result.append(n[0])
        return result
    def __str__(self):
        res = ''
        for node in self.edges:
            for n in self.edges[node]:
                weight = (float(n[1][0]), float(n[1][1]))
                res = "{0}{1}->{2} {3}\n".format(res, node, n[0], weight)
        return res[:-1]

nh = Node('h')
nj = Node('j')
nk = Node('k')
nm = Node('m')
ng = Node('g')
g = WeightedDigraph()
g.addNode(nh)
g.addNode(nj)
g.addNode(nk)
g.addNode(nm)
g.addNode(ng)

randomEdge = WeightedEdge(nj, nh, 77, 44)
g.addEdge(randomEdge)
randomEdge = WeightedEdge(nh, nm, 32, 26)
g.addEdge(randomEdge)
randomEdge = WeightedEdge(nk, nj, 18, 8)
g.addEdge(randomEdge)
randomEdge = WeightedEdge(nj, nh, 35, 32)
g.addEdge(randomEdge)
randomEdge = WeightedEdge(nk, nm, 22, 15)
g.addEdge(randomEdge)
randomEdge = WeightedEdge(nh, nm, 23, 19)
g.addEdge(randomEdge)
randomEdge = WeightedEdge(nj, nh, 91, 58)
g.addEdge(randomEdge)
randomEdge = WeightedEdge(nm, nk, 16, 6)
g.addEdge(randomEdge)
# print g.childrenOf(nh)
# print g.childrenOf(nj)
# print g.childrenOf(nk)
# print g.childrenOf(nm)
# print g.childrenOf(ng)
#
# nx = Node('x')
# ny = Node('y')
# nz = Node('z')
# e1 = WeightedEdge(nx, ny, 18, 8)
# e2 = WeightedEdge(ny, nz, 20, 1)
# e3 = WeightedEdge(nz, nx, 7, 6)
# g = WeightedDigraph()
# g.addNode(nx)
# g.addNode(ny)
# g.addNode(nz)
# g.addEdge(e1)
# g.addEdge(e2)
# g.addEdge(e3)
# print g