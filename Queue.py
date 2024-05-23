class Queue: 
    def __init__ (self):
        self.items=[]
        self.rear=0
        self.front=0
        # self.Max=Max
    
    def enqueue(self, item):
        self.rear= self.rear+1 
        self.items.append(item)
    
    def dequeue(self):
        if(self.isEmpty):
            return "UnderFlow"
        else:
            self.front +=1
            return self.items.pop()
    
    def isEmpty(self):
        if(self.rear==self.front):
            return True
        else:
            return False

    def SizeOfQueue(self):
        return self.rear-self.front