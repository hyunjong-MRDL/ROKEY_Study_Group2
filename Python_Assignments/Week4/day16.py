print()



class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return -1
    
    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return -1
    
    def is_empty(self):
        return len(self.queue) == 0

class FullQueueError(Exception):
    pass

class CircularQueue(Queue):
    def __init__(self, size):
        super().__init__()
        self.size = size
    
    def enqueue(self, data):
        if not self.is_full():
            return super().enqueue(data)
        else:
            raise FullQueueError
    
    def is_full(self):
        return len(self.queue) == self.size



print()