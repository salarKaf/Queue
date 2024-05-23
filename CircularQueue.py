class CircularQueue:
    def __init__(self, max_size):
        self.max_size=max_size
        self.CircleQ=[]
        self.rear=0
        self.front=0

    
    def enqueue(self , item):
        if(self.SizeOfQueue==self.max_size):
            return "Over Flow"
        else:
            CircleQ[self.rear]=item
            self.rear= (self.rear % self.max_size)+1


    def dequeue(self):
        if(self.isEmpty):
            return "Queue is empty"
        else:
            x=CircleQ[self.front]
            self.front= (self.front% self.max_size)+1
            return x
            
    def isEmpty(self):
        if(self.rear==self.front):
            return True
        else:
            return False

    def SizeOfQueue(self):
        return (Max + (self.rear - self.front)) % Max;
