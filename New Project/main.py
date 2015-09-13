# Hello World program in Python
    
# Hello World program in Python
    
# import copy
# a = {1: 'a', 2: 'b', 3: 'c'}

# print a.viewitems()
# a.update( [(3, 'C'), (4, 'D')])
# print a
# print a.pop(5, None)
# print a
# it = iter(a)
# for i in it:print i
    
# b = set([1, 2, 3])
# c = b.copy()

# print b is c
# b.add(4)
# print b, c

class Node():
    def __init__(self, aa, bb):
        self.aa = aa
        self.bb = bb
    def change(self):
        self.aa = 10
    def __str__(self):
        return str(self.aa) + str(self.bb)

# e = set([Node(1, 2), Node(3, 4)])
# f = e.copy()
# print e.pop() is f.pop()
# e.add(Node(2,3))
# print e, f

# g = [Node(1, 2), Node(3, 4)]
# h = copy.copy(g)
# g[0].change()
# print g, h

# i = set([1, 2, 3])
# j = set([2, 3, 4, 5])
# print i.union(j)
# print i.intersection(j)
# print i.difference(j)
# print i.symmetric_difference(j)
# print i.isdisjoint(j)
# print zip(i, j)

# print dict.fromkeys(i, 0)

# string
# print "jihuiug87879".title()
# print "they're bill's friends from the UK".title()
# print "they're bill's friends from the UK".capitalize()
# print 'read this short text'.translate(None, 'aeiou')
# print '%(language)s has %(number)03d quote types.' %{"language": "Python", "number": 2}

# x = str(raw_input('What is your name? '))
# print x
# x = input('what are the first 10 perfect squares?')
# print x

import collections
c = collections.Counter()
# print c
c = collections.Counter('gallahad')
# print c
c = collections.Counter(cats=4, dogs=8)
# print c
c = collections.Counter({'red': 4, 'blue': 2})
# print c
# print list(c.elements())
d = c.copy()
# print d

q = collections.deque([1, 2, 3])
q.append(4)
# print q


import heapq
l = [5, 23, 3, 6, 7, 25]
# print heapq.nlargest(1, l)
heapq.heapify(l)
# print l
# print l[0]
# print heapq.heappushpop(l, 2)
# print l[0]

h = []
heapq.heappush(h, (5, 'write code'))
heapq.heappush(h, (7, 'release product'))
heapq.heappush(h, (1, 'write spec'))
heapq.heappush(h, (3, 'create tests'))
# print h


from math import pi, sin
sine_table = dict((x, sin(x*pi/180)) for x in range(0, 91))
# print sine_table


def generate(data):
    for i in range(len(data)): yield data[i]
        
# for i in generate("heliefef"): print i+i
  
class animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print "animal"
        
    def run(self):
        print "running"
    
    def eat(self):
        print "eating food"
        
class dog(animal):
    def __init__(self, name, age, dtype):
        animal.__init__(self, name, age)
        self.dtype = dtype
        print "dog"
        
    def run(self):
        animal.run(self)
        print "dog running"
        
    def eat(self):
        print self.name + " is eating bone"
    
    def bark(self):
        print "whoof whoof"
        
a = animal("a1", 14)
# a.run()
# a.eat()
# print isinstance(a, animal) or isinstance(a, dog)

b = dog("sky", 13, "lab")
b.run()
b.eat()
b.bark()
# print isinstance(b, animal)
