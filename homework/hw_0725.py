# numbers = [1,2,3,4,5]
# numbers = iter(numbers)
# for i in numbers:
#     print(i)

# try : 
#     fruits = ['apple','banana','cherry']
#     fruits = iter(fruits)
#     for i in range(5):
#         print(next(fruits))

# except StopIteration :
#     pass


# num_cycle = ( i for i in range(11) if i % 2 ==0)
# for j in num_cycle:
#     print(j)


class MyRange:
    def __init__(self,start, stop ,step=1):
        self.start = start
        self.stop = stop
        self.step = step
    
    def __iter__(self):
        return self
    
    def __next__(self): 
        if self.start <= self.stop-1 :
            result = self.start   
        else :
            raise StopIteration
        
        self.start = 1*self.step + self.start 
        
        return result
    
my = MyRange(1,10)
for j in my :
    print(j)