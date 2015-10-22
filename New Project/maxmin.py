import collections

class maxQueue():
    def __init__(self):
        self.size = 0
        self.q = collections.deque()
        self.mq = collections.deque()
        
    def push(self, num):
        while self.mq and self.mq[-1] < num:
            self.mq.pop()
        self.mq.append(num)
        self.q.append(num)
        self.size += 1
        
    def pop(self):
        if self.size == 0: 
            raise IndexError('pop from empty minQueue')
        r = self.q.popleft()
        if r == self.mq[0]: self.mq.popleft()
        self.size -= 1
        return r
    
    def max(self):
        if self.size == 0: 
            raise IndexError('pop from empty minQueue')
        return self.mq[0]
        
        
class minQueue():
    def __init__(self):
        self.size = 0
        self.q = collections.deque()
        self.mq = collections.deque()
        
    def push(self, num):
        while self.mq and self.mq[-1] > num:
            self.mq.pop()
        self.mq.append(num)
        self.q.append(num)
        self.size += 1
        
    def pop(self):
        if self.size == 0:
            raise IndexError('pop from empty minQueue')
        r = self.q.popleft()
        if r == self.mq[0]: self.mq.popleft()
        self.size -= 1
        return r
    
    def min(self):
        if self.size == 0: 
            raise IndexError('pop from empty minQueue')
        return self.mq[0]
        
class minStack():
    def __init__(self):
        self.stack = []
        self.min = None
        self.size = 0

    def push(self, x):
        if self.size == 0: self.min = x
        t = x - self.min
        if t < 0: self.min = x
        self.stack.append(t)
        self.size += 1

    def pop(self):
        if self.size == 0: 
            raise IndexError('pop from empty minQueue')
        r = self.stack.pop()
        if r < 0:
            old = self.min - r
            self.min = old
        self.size -= 1

    def top(self):
        if self.size == 0:
            raise IndexError('pop from empty minQueue')
        e = 0
        if self.stack[-1] >= 0: e = self.stack[-1]
        return self.min+e

    def getMin(self):
        if self.size == 0:
            raise IndexError('pop from empty minQueue')
        return self.min

class maxStack():
    def __init__(self):
        self.stack = []
        self.max = None
        self.size = 0

    def push(self, x):
        if self.size == 0: self.max = x
        t = x - self.max
        if t > 0: self.max = x
        self.stack.append(t)
        self.size += 1

    def pop(self):
        if self.size == 0: 
            raise IndexError('pop from empty minQueue')
        r = self.stack.pop()
        if r > 0:
            old = self.max - r
            self.max = old
        self.size -= 1

    def top(self):
        if self.size == 0:
            raise IndexError('pop from empty minQueue')
        e = 0
        if self.stack[-1] >= 0: e = self.stack[-1]
        return self.max+e

    def getMax(self):
        if self.size == 0:
            raise IndexError('pop from empty minQueue')
        return self.max


# q = minQueue()
# q.push(4)
# print q.min()
# q.push(2)
# q.push(2)
# print q.min()
# q.push(3)
# q.pop()
# q.pop()
# q.pop()
# q.pop()
# # q.push(1)
# print q.min()

# s = maxStack()
# s.push(4)
# s.push(2)
# s.push(5)
# print s.getMax()
# s.pop()
# print s.getMax()