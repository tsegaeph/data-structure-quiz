class LinearQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = []
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def is_full(self):
        return len(self.queue) == self.max_size
    
    def enqueue(self, data):
        if self.is_full():
            print("Queue is full. Cannot enqueue element.")
        else:
            self.queue.append(data)
            print("Enqueued:", data)
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue element.")
            return None
        else:
            data = self.queue.pop(0)
            print("Dequeued:", data)
            return data
queue = LinearQueue(5)  # Create a queue of size 5

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

dequeued_element = queue.dequeue()
print("Dequeued element:", dequeued_element)

queue.enqueue(40)
queue.enqueue(50)

if not queue.is_full():
    queue.enqueue(60)

while not queue.is_empty():
    dequeued_element = queue.dequeue()
    ###print("Dequeued element:", dequeued_element)
class CircularQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * max_size
        self.front = -1
        self.rear = -1
        self.current_size = 0

    def is_empty(self):
        return self.current_size == 0

    def is_full(self):
        return self.current_size == self.max_size

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full. Cannot enqueue element.")
        else:
            if self.front == -1:
                self.front = 0
            self.rear = (self.rear + 1) % self.max_size
            self.queue[self.rear] = data
            self.current_size += 1
            print("Enqueued:", data)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue element.")
            return None
        else:
            data = self.queue[self.front]
            self.queue[self.front] = None
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front + 1) % self.max_size
            self.current_size -= 1
            print("Dequeued:", data)
            return data
queue = CircularQueue(5)  # Create a circular queue of size 5

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

dequeued_element = queue.dequeue()
print("Dequeued element:", dequeued_element)

queue.enqueue(40)
queue.enqueue(50)

if not queue.is_full():
    queue.enqueue(60)

while not queue.is_empty():
    dequeued_element = queue.dequeue()
    ###print("Dequeued element:", dequeued_element)
class LinearQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def enqueue(self, data):
        self.stack1.append(data)
        print("Enqueued:", data)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue element.")
            return None

        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())

        data = self.stack2.pop()
        print("Dequeued:", data)
        return data
queue = LinearQueue()  # Create a linear queue using stacks

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

dequeued_element = queue.dequeue()
print("Dequeued element:", dequeued_element)

queue.enqueue(40)
queue.enqueue(50)

while not queue.is_empty():
    dequeued_element = queue.dequeue()
    print("Dequeued element:", dequeued_element)
