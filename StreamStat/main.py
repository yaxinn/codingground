# Hello World program in Python
import sys, heapq
class StreamStat():
    def __init__(self):
        self.min = sys.maxint
        self.max = -sys.maxint
        self.sum = 0
        self.n = 0
        self.maxheap = [sys.maxint]
        heapq.heapify(self.maxheap)
        self.minheap = [sys.maxint] # default heap
        heapq.heapify(self.minheap)
        self.maxsize = 0
        self.minsize = 0
    
    def add(self, new):
        self.sum += new
        self.n += 1
        # update min, max
        if self.min > new:
            self.min = new
        if self.max < new:
            self.max = new
        self._updateheap(new)
        self._display()
    
    def display(self):
        self._display()
    
    def _display(self):
        print "   "
        print "min value: " + str(self.min)
        print "max value: " + str(self.max)
        print "size: " + str(self.n)
        # temp = [ -i for i in self.maxheap ]
        # print "maxheap: "
        # print temp
        # print "minheap: "
        # print self.minheap
        # print "maxheap size: " + str(self.maxsize)
        # print "minheap size: " + str(self.minsize)
        print "median: " + str(self._median())
        print "average: " + str(self._average())
        
    def _updateheap(self, new):
        if self.maxsize == self.minsize:
            if self.minheap[0] < new:
                heapq.heappush(self.minheap, new)
                self.minsize += 1
            else:
                heapq.heappush(self.maxheap, -new)
                self.maxsize += 1
        elif self.maxsize > self.minsize:
            if new >= -self.maxheap[0]:
                heapq.heappush(self.minheap, new)
            else:
                temp = heapq.heapreplace(self.maxheap, -new)
                heapq.heappush(self.minheap, -temp)
            self.minsize += 1
        else:
            if new <= self.minheap[0]:
                heapq.heappush(self.maxheap, -new)
            else:
                temp = heapq.heapreplace(self.minheap, new)
                heapq.heappush(self.maxheap, -temp)
            self.maxsize += 1
    
    def _median(self):
        if self.maxsize == self.minsize:
            return (-self.maxheap[0] + self.minheap[0])*1.0 / 2
        elif self.maxsize > self.minsize:
            return -self.maxheap[0]
        else: 
            return self.minheap[0]
    
    def _average(self):
        return 0 if not self.n else self.sum*1.0/self.n
    
def test (inp):
    statistic = StreamStat()
    for i in inp: statistic.add(i)
    statistic.display()

test([1, 5, 4, 3, 8, 9, 7])
test([1, 1, 1, 1])
test([])