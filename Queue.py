class Queue:
    def __init__(self):
        self.queue = list()
        self.size = len(self.queue)
        
    def enqueue(self, data):
        self.queue.append(data)
   
    def dequeue(self):
        if self.size == 0:
            return "There is no Data."
        return del self.queue[0]
        
    def getQueue(self):
        return self.queue
    
    def is_empty(self):
        if self.size == 0:
            return "There is no data removed."
        self.queue = list()
        return "Queue is empty now."
