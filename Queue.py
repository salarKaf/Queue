class Queue: 
    def __init__ (self , Max):
        self.queue=[]
        self.rear=0
        self.front=0
        self.Max=Max
    

    def enqueue(item , self):
        # if (self.rear == self.Max):
        #     return "over flow"
        # else:
        self.rear= self.rear+1 
        queue[rear] = item
    
    def dequeue(self):
        if(self.isEmpty):
            return "UnderFlow"
        else:
            self.front+=1
            return q[self.front]
    
    def isEmpty(self):
        if(self.rear==self.front):
            return True
        else:
            return False

    def SizeOfQueue(self):
        return self.rear-self.front