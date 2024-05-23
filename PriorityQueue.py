class data:
    def __init__(self , priority , item):
        self.priority=priority
        self.item=item





class PriorityQueue:
    def __init__(self , Max):
        self.pQueue=[]
        self.rear=0
        self.front=0
        self.Max=Max
    def enqueue(self, item, priority):
        if (self.rear == self.Max):
             return "over flow"
        elif(self.isEmpty):
            self.item=data(priority , item)
            self.pQueue.insert(0 , item)
        else:
            self.item=data(priority , item)
            for i in range(0 , len(pQueue)):
                if(pQueue[i].priority<= item.priority):
                    self.queue.insert(i ,item)
                    self.rear+=1
    
        def dequeue(self):
            if(self.isEmpty):
                return "UnderFlow"
            else:
                self.pQueue.pop(0)
                self.front-=1
    def isEmpty(self):
        if(self.rear==self.front):
            return True
        else:
            return False

    def SizeOfQueue(self):
        return self.rear-self.front