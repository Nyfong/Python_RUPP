class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
       return self.queue.pop(0)
    
#create instance
object = Queue()
for i in range(10):
    object.enqueue(i)
print(object.queue)
print(object.dequeue)