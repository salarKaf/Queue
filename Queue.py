class Queue: 
    def __init__ (self , Max):
        self.queue=[]
        self.rear=-1
        self.front=-1
        self.Max=Max
    

    def enqueue(item , self):
        if (self.rear == self.Max):
         return "over flow"
         else:
            self.queue.append(item)
            self.rear+=1
    
    def dequeue(self):
        if(self.isEmpty):
            return "UnderFlow"
        else:
            self.queue.pop(0)
            self.front-=1
    
    def isEmpty(self):
        if(self.rear==self.front):
            return True
        else:
            return False

    def SizeOfQueue(self):
        return self.rear-self.front