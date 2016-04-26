# Created on Apr 24, 2016
# 
# @author: aldobest

class Product:
    
    def __init__(self, length, numbers):
        self.length = length
        self.numbers = numbers
        assert(len(self.numbers) == self.length)
    
    def getMaxProduct(self):
        result = 0
        
        for i in range(0, self.length):
            for j in range(i+1, self.length):
                if self.numbers[i] * self.numbers[j] > result:
                    result = self.numbers[i] * self.numbers[j]

        return result
    
    def getMaxProductFaster(self):
        maxIndex1 = -1
        for i in range(0, self.length):
            if maxIndex1 == -1 or self.numbers[i] > self.numbers[maxIndex1]:
                maxIndex1 = i
        
        maxIndex2 = -1
        for j in range(0, self.length):
            if j != maxIndex1 and (maxIndex2 == -1 or (self.numbers[j] > self.numbers[maxIndex2])):
                maxIndex2 = j
        
        return self.numbers[maxIndex1] * self.numbers[maxIndex2]