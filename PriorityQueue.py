class PriorityQueue:
    def __init__(self , Max):
        self.pQueue=[]
        self.rear=-1
        self.front=-1
        self.Max=Max
        self.q=Queue(self.Max)
    # def enqueue(self, item, priority):
    #     if (self.rear == self.Max):
    #          return "over flow"
    #      else:
    #         self.queue.append(item)
    #         self.rear+=1